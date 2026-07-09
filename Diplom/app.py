import subprocess
import sys
import re
import os
import json
import signal
from pathlib import Path
from flask import Flask, send_file, jsonify, request, Response

app = Flask(__name__)

PROJECT_DIR = Path(__file__).parent.parent
DILOM_DIR = Path(__file__).parent
RESULTS_DIR = DILOM_DIR / 'results'

# Store running process for abort
_current_proc = None


@app.route('/')
def index():
    return send_file(PROJECT_DIR / 'index.html')


@app.route('/api/stop-tests', methods=['POST'])
def stop_tests():
    global _current_proc
    if _current_proc and _current_proc.poll() is None:
        try:
            _current_proc.kill()
            _current_proc.wait(timeout=5)
        except Exception:
            pass
        _current_proc = None
        return jsonify({'stopped': True})
    return jsonify({'stopped': False, 'message': 'No running tests'})


@app.route('/api/run-tests', methods=['POST'])
def run_tests():
    global _current_proc
    data = request.get_json()
    test_type = data.get('type', 'all')
    use_allure = data.get('allure', False)

    test_paths = {
        'api': 'Diplom/tests/api/',
        'ui': 'Diplom/tests/ui/',
        'unit': 'Diplom/tests/unit/',
    }

    if test_type == 'all':
        cmd = [sys.executable, '-m', 'pytest', '-v',
               'Diplom/tests/api/', 'Diplom/tests/ui/', 'Diplom/tests/unit/']
    elif test_type in test_paths:
        test_path = test_paths[test_type]
        full_path = PROJECT_DIR / test_path
        if not full_path.exists():
            return jsonify({'error': f'Path not found: {test_path}'}), 400
        cmd = [sys.executable, '-m', 'pytest', '-v', test_path]
    else:
        return jsonify({'error': f'Unknown test type: {test_type}'}), 400

    if use_allure:
        RESULTS_DIR.mkdir(exist_ok=True)
        cmd += [f'--alluredir={RESULTS_DIR}', '--clean-alluredir']

    env = os.environ.copy()
    env['PYTHONPATH'] = str(PROJECT_DIR)

    def generate():
        global _current_proc
        proc = subprocess.Popen(
            cmd, stdout=subprocess.PIPE, stderr=subprocess.STDOUT,
            cwd=str(PROJECT_DIR), env=env, text=True, bufsize=1,
            encoding='utf-8', errors='replace',
        )
        _current_proc = proc

        tests = []
        passed = failed = errors = skipped = 0
        duration = ''

        for line in proc.stdout:
            if proc.poll() is not None:
                break
            line = line.rstrip('\n')
            yield json.dumps({'type': 'line', 'text': line}, ensure_ascii=False) + '\n'

            stripped = line.strip()
            m = re.match(r'^(.+?)\s+(PASSED|FAILED|ERROR|SKIPPED)', stripped)
            if m:
                full_name = m.group(1)
                short_name = full_name.split('::')[-1]
                status_map = {'PASSED': 'passed', 'FAILED': 'failed',
                              'ERROR': 'failed', 'SKIPPED': 'skipped'}
                st = status_map.get(m.group(2), 'skipped')
                tests.append({'name': short_name, 'status': st, 'full_name': full_name})
                if st == 'passed': passed += 1
                elif st == 'failed': failed += 1
                elif st == 'skipped': skipped += 1

            if re.search(r'\d+ (passed|failed|error|skipped)', stripped):
                pm = re.search(r'(\d+) passed', stripped)
                if pm: passed = int(pm.group(1))
                fm = re.search(r'(\d+) failed', stripped)
                if fm: failed = int(fm.group(1))
                em = re.search(r'(\d+) error', stripped)
                if em: errors = int(em.group(1))
                sm = re.search(r'(\d+) skipped', stripped)
                if sm: skipped = int(sm.group(1))
                dm = re.search(r'in ([\d.]+)s', stripped)
                if dm: duration = dm.group(1) + 's'

        proc.wait()
        _current_proc = None

        was_killed = proc.returncode == -9 or proc.returncode == -signal.SIGTERM
        result = {
            'type': 'done',
            'success': proc.returncode == 0,
            'returncode': proc.returncode,
            'stopped': was_killed,
            'tests': tests,
            'stats': {
                'passed': passed,
                'failed': failed,
                'errors': errors,
                'skipped': skipped,
                'total': passed + failed + errors + skipped,
                'duration': duration,
            },
        }
        yield json.dumps(result, ensure_ascii=False) + '\n'

    return Response(generate(), mimetype='text/event-stream',
                   headers={'Cache-Control': 'no-cache', 'X-Accel-Buffering': 'no',
                            'Connection': 'keep-alive'})


if __name__ == '__main__':
    print('=' * 50)
    print('  QA Portfolio — Test Runner')
    print(f'  Open http://localhost:5000')
    print('=' * 50)
    app.run(port=5000, threaded=True)
