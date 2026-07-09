import asyncio
import subprocess
import sys
import logging
from pathlib import Path
from telegram import Update
from telegram.ext import Application, CommandHandler, ContextTypes
from telegram.request import HTTPXRequest

logging.basicConfig(level=logging.INFO, format="%(asctime)s [%(levelname)s] %(message)s")
log = logging.getLogger(__name__)

PROJECT_DIR = Path(__file__).resolve().parent.parent
RESULTS_DIR = PROJECT_DIR / "Diplom" / "results"
LOCK_FILE = Path(__file__).resolve().parent / ".bot.lock"

TOKEN = "8866805088:AAGLcFuTrl8qY4OrMhmBlpVQnuTqP121-xM"


def _run_subprocess(cmd: str, timeout: int) -> str:
    try:
        result = subprocess.run(
            cmd, shell=True, capture_output=True, text=True,
            cwd=str(PROJECT_DIR), timeout=timeout,
        )
        output = f"STDOUT:\n{result.stdout.strip()}" if result.stdout else ""
        output += f"\nSTDERR:\n{result.stderr.strip()}" if result.stderr else ""
        return output.strip()
    except subprocess.TimeoutExpired:
        return f"Таймаут {timeout} сек"
    except Exception as e:
        return f"Ошибка: {e}"


async def execute_command(cmd: str, timeout: int = 300) -> str:
    loop = asyncio.get_event_loop()
    return await loop.run_in_executor(None, _run_subprocess, cmd, timeout)


def _clear_results():
    RESULTS_DIR.mkdir(exist_ok=True)
    for file in RESULTS_DIR.glob("*"):
        file.unlink()


def _format_result(result: str) -> str:
    failed = [line for line in result.split("\n")
              if "FAILED" in line or "ERROR" in line or "not recognized" in line
              or "Таймаут" in line or "Ошибка" in line]
    return "\n".join(failed)[:3000] if failed else ""


async def run_api_test(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text("Запуск API тестов...")
    _clear_results()
    result = await execute_command(
        f"{sys.executable} -m pytest -s -v Diplom/tests/api/ -n 4 --alluredir={RESULTS_DIR}"
    )
    short = _format_result(result)
    await update.message.reply_text(
        f"Результат API тестов:\n{short}" if short else "Все API тесты прошли успешно"
    )


async def run_ui_test(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text("Запуск UI тестов...")
    _clear_results()
    result = await execute_command(
        f"{sys.executable} -m pytest -s -v Diplom/tests/ui/ --alluredir={RESULTS_DIR}",
        timeout=600,
    )
    short = _format_result(result)
    await update.message.reply_text(
        f"Результат UI тестов:\n{short}" if short else "Все UI тесты прошли успешно"
    )


async def post_init(application):
    log.info("Bot started, polling updates...")


async def post_shutdown(application):
    log.info("Bot stopped.")


def main() -> None:
    import os

    if LOCK_FILE.exists():
        old_pid = LOCK_FILE.read_text().strip()
        log.warning("Lock file found (pid=%s). Another bot instance may be running.", old_pid)
        log.warning("If no other instance is running, delete: %s", LOCK_FILE)
    LOCK_FILE.write_text(str(os.getpid()))

    custom_request = HTTPXRequest(
        connect_timeout=30,
        read_timeout=30,
        write_timeout=30,
    )
    application = (
        Application.builder()
        .token(TOKEN)
        .post_init(post_init)
        .post_shutdown(post_shutdown)
        .request(custom_request)
        .build()
    )
    application.add_handler(CommandHandler("run_api_tests", run_api_test))
    application.add_handler(CommandHandler("run_ui_tests", run_ui_test))

    try:
        application.run_polling(drop_pending_updates=True, allowed_updates=Update.ALL_TYPES)
    finally:
        LOCK_FILE.unlink(missing_ok=True)


if __name__ == "__main__":
    main()
