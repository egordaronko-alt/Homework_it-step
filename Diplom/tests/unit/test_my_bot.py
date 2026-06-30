import pytest
import asyncio
from unittest.mock import MagicMock, patch, AsyncMock
from Diplom.my_bot import execute_command, run_api_test, help_command1, help_command2


class TestExecuteCommand:
    @pytest.mark.asyncio
    async def test_execute_command_success(self):
        mock_update = MagicMock()
        mock_proc = AsyncMock()
        mock_proc.communicate.return_value = (b"output line1\noutput line2", b"")

        with patch('asyncio.create_subprocess_shell', return_value=mock_proc):
            with patch('asyncio.wait_for', return_value=(b"output line1\noutput line2", b"")):
                result = await execute_command("echo hello", mock_update)
                assert "output line1" in result
                assert "output line2" in result

    @pytest.mark.asyncio
    async def test_execute_command_with_stderr(self):
        mock_update = MagicMock()
        mock_proc = AsyncMock()
        mock_proc.communicate.return_value = (b"stdout data", b"stderr data")

        with patch('asyncio.create_subprocess_shell', return_value=mock_proc):
            with patch('asyncio.wait_for', return_value=(b"stdout data", b"stderr data")):
                result = await execute_command("some command", mock_update)
                assert "stdout data" in result
                assert "stderr data" in result

    @pytest.mark.asyncio
    async def test_execute_command_timeout(self):
        mock_update = MagicMock()
        with patch('asyncio.create_subprocess_shell') as mock_create:
            with patch('asyncio.wait_for', side_effect=asyncio.TimeoutError()):
                result = await execute_command("long command", mock_update, timeout=5)
                assert "Таймаут 5 сек" in result

    @pytest.mark.asyncio
    async def test_execute_command_exception(self):
        mock_update = MagicMock()
        with patch('asyncio.create_subprocess_shell', side_effect=Exception("spawn error")):
            result = await execute_command("bad command", mock_update)
            assert "Ошибка" in result
            assert "spawn error" in result


class TestRunApiTest:
    @pytest.mark.asyncio
    async def test_run_api_test_success(self):
        mock_update = MagicMock()
        mock_update.message = AsyncMock()
        mock_context = MagicMock()

        with patch('Diplom.my_bot.execute_command', return_value="ALL TESTS PASSED"):
            with patch('pathlib.Path.mkdir'):
                with patch('pathlib.Path.glob', return_value=[]):
                    await run_api_test(mock_update, mock_context)

        mock_update.message.reply_text.assert_any_call("Запуск тестов api")
        mock_update.message.reply_text.assert_any_call("Все тесты прошли успешно")

    @pytest.mark.asyncio
    async def test_run_api_test_with_failures(self):
        mock_update = MagicMock()
        mock_update.message = AsyncMock()
        mock_context = MagicMock()

        failed_result = "FAILED tests/test_something.py::test_case\nERROR tests/test_other.py::test_fail"
        with patch('Diplom.my_bot.execute_command', return_value=failed_result):
            with patch('pathlib.Path.mkdir'):
                with patch('pathlib.Path.glob', return_value=[]):
                    await run_api_test(mock_update, mock_context)

        mock_update.message.reply_text.assert_any_call("Запуск тестов api")
        reply_calls = [call for call in mock_update.message.reply_text.call_args_list
                       if "Результат" in str(call)]
        assert len(reply_calls) > 0


class TestHelpCommands:
    @pytest.mark.asyncio
    async def test_help_command2(self):
        mock_update = MagicMock()
        mock_update.message = AsyncMock()
        mock_context = MagicMock()

        await help_command2(mock_update, mock_context)
        mock_update.message.reply_text.assert_called_once_with("Как у вас дела!13213213")

    @pytest.mark.asyncio
    async def test_help_command1(self):
        mock_update = MagicMock()
        mock_update.message = AsyncMock()
        mock_context = MagicMock()

        await help_command1(mock_update, mock_context)
        mock_update.message.reply_text.assert_called_once_with("Как у вас 3213213213214235634дела!")
