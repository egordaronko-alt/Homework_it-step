import pytest
from unittest.mock import MagicMock, patch, PropertyMock
from Diplom.pages.base_page import WebPage


class TestWebPageInit:
    def test_init_calls_get(self):
        mock_driver = MagicMock()
        with patch.object(WebPage, 'get') as mock_get:
            page = WebPage(mock_driver, 'https://example.com')
            mock_get.assert_called_once_with('https://example.com')

    def test_init_stores_driver(self):
        mock_driver = MagicMock()
        with patch.object(WebPage, 'get'):
            page = WebPage(mock_driver)
            assert page._web_driver == mock_driver


class TestWebPageSetAttr:
    def test_setattr_sets_element_value(self):
        mock_driver = MagicMock()
        with patch.object(WebPage, 'get'):
            page = WebPage(mock_driver)
            mock_element = MagicMock()
            object.__setattr__(page, 'my_field', mock_element)
            page.my_field = "some value"
            mock_element._set_value.assert_called_once_with(mock_driver, "some value")

    def test_setattr_private_attr(self):
        mock_driver = MagicMock()
        with patch.object(WebPage, 'get'):
            page = WebPage(mock_driver)
            page._private = "secret"
            assert page._private == "secret"


class TestWebPageGet:
    def test_get_navigates_to_url(self):
        mock_driver = MagicMock()
        with patch.object(WebPage, 'get'):
            page = WebPage(mock_driver)
            page._web_driver = mock_driver
        with patch.object(WebPage, 'wait_page_loaded') as mock_wait:
            page.get('https://example.com')
            mock_driver.get.assert_called_once_with('https://example.com')
            mock_wait.assert_called_once()


class TestWebPageGoBack:
    def test_go_back(self):
        mock_driver = MagicMock()
        with patch.object(WebPage, 'get'):
            page = WebPage(mock_driver)
            page._web_driver = mock_driver
        with patch.object(WebPage, 'wait_page_loaded') as mock_wait:
            page.go_back()
            mock_driver.back.assert_called_once()
            mock_wait.assert_called_once()


class TestWebPageRefresh:
    def test_refresh(self):
        mock_driver = MagicMock()
        with patch.object(WebPage, 'get'):
            page = WebPage(mock_driver)
            page._web_driver = mock_driver
        with patch.object(WebPage, 'wait_page_loaded') as mock_wait:
            page.refresh()
            mock_driver.refresh.assert_called_once()
            mock_wait.assert_called_once()


class TestWebPageScreenshot:
    def test_screenshot_default_name(self):
        mock_driver = MagicMock()
        with patch.object(WebPage, 'get'):
            page = WebPage(mock_driver)
            page.screenshot()
            mock_driver.save_screenshot.assert_called_once_with('screenshot.png')

    def test_screenshot_custom_name(self):
        mock_driver = MagicMock()
        with patch.object(WebPage, 'get'):
            page = WebPage(mock_driver)
            page.screenshot('custom.png')
            mock_driver.save_screenshot.assert_called_once_with('custom.png')


class TestWebPageScrollDown:
    def test_scroll_down_with_offset(self):
        mock_driver = MagicMock()
        with patch.object(WebPage, 'get'):
            page = WebPage(mock_driver)
            page.scroll_down(offset=500)
            mock_driver.execute_script.assert_called_once_with(
                'window.scrollTo(0, 500);'
            )

    def test_scroll_down_without_offset(self):
        mock_driver = MagicMock()
        with patch.object(WebPage, 'get'):
            page = WebPage(mock_driver)
            page.scroll_down()
            mock_driver.execute_script.assert_called_once_with(
                'window.scrollTo(0, document.body.scrollHeight);'
            )


class TestWebPageScrollUp:
    def test_scroll_up_with_offset(self):
        mock_driver = MagicMock()
        with patch.object(WebPage, 'get'):
            page = WebPage(mock_driver)
            page.scroll_up(offset=300)
            mock_driver.execute_script.assert_called_once_with(
                'window.scrollTo(0, -300);'
            )

    def test_scroll_up_without_offset(self):
        mock_driver = MagicMock()
        with patch.object(WebPage, 'get'):
            page = WebPage(mock_driver)
            page.scroll_up()
            mock_driver.execute_script.assert_called_once_with(
                'window.scrollTo(0, -document.body.scrollHeight);'
            )


class TestWebPageCookies:
    def test_get_cookies(self):
        mock_driver = MagicMock()
        mock_driver.get_cookies.return_value = [{"name": "test", "value": "123"}]
        with patch.object(WebPage, 'get'):
            page = WebPage(mock_driver)
            cookies = page.get_cookies()
            assert cookies == [{"name": "test", "value": "123"}]

    def test_add_cookie(self):
        mock_driver = MagicMock()
        with patch.object(WebPage, 'get'):
            page = WebPage(mock_driver)
            page.add_cookie("session", "abc123")
            mock_driver.add_cookie.assert_called_once_with(name="session", value="abc123")


class TestWebPageSwitchWindow:
    def test_switch_to_window(self):
        mock_driver = MagicMock()
        mock_driver.window_handles = ["handle0", "handle1", "handle2"]
        with patch.object(WebPage, 'get'):
            page = WebPage(mock_driver)
            page.switch_to_window(window=1)
            mock_driver.switch_to.window.assert_called_once_with("handle1")


class TestWebPageGetCurrentUrl:
    def test_get_current_url(self):
        mock_driver = MagicMock()
        mock_driver.current_url = "https://example.com/page"
        with patch.object(WebPage, 'get'):
            page = WebPage(mock_driver)
            assert page.get_current_url() == "https://example.com/page"


class TestWebPageExecuteScript:
    def test_execute_script(self):
        mock_driver = MagicMock()
        mock_driver.execute_script.return_value = "result"
        with patch.object(WebPage, 'get'):
            page = WebPage(mock_driver)
            result = page.execute_script("return 1 + 1")
            assert result == "result"
            mock_driver.execute_script.assert_called_once_with("return 1 + 1")


class TestWebPageGetPageSource:
    def test_get_page_source(self):
        mock_driver = MagicMock()
        mock_driver.page_source = "<html><body>Hello</body></html>"
        with patch.object(WebPage, 'get'):
            page = WebPage(mock_driver)
            source = page.get_page_source()
            assert source == "<html><body>Hello</body></html>"

    def test_get_page_source_returns_empty_on_exception(self):
        mock_driver = MagicMock()
        type(mock_driver).page_source = PropertyMock(side_effect=Exception("error"))
        with patch.object(WebPage, 'get'):
            page = WebPage(mock_driver)
            source = page.get_page_source()
            assert source == ""


class TestWebPageCheckJsErrors:
    def test_check_js_errors_no_errors(self):
        mock_driver = MagicMock()
        mock_driver.get_log.return_value = []
        with patch.object(WebPage, 'get'):
            page = WebPage(mock_driver)
            page.check_js_errors()

    def test_check_js_errors_with_ignored(self):
        mock_driver = MagicMock()
        mock_driver.get_log.return_value = [
            {"level": "SEVERE", "message": "Known issue"}
        ]
        with patch.object(WebPage, 'get'):
            page = WebPage(mock_driver)
            page.check_js_errors(ignore_list=["Known issue"])

    def test_check_js_errors_raises_on_severe(self):
        mock_driver = MagicMock()
        mock_driver.get_log.return_value = [
            {"level": "SEVERE", "message": "Unexpected error"}
        ]
        with patch.object(WebPage, 'get'):
            page = WebPage(mock_driver)
            with pytest.raises(AssertionError, match="JS error"):
                page.check_js_errors()

    def test_check_js_errors_ignores_warnings(self):
        mock_driver = MagicMock()
        mock_driver.get_log.return_value = [
            {"level": "WARNING", "message": "Some warning"}
        ]
        with patch.object(WebPage, 'get'):
            page = WebPage(mock_driver)
            page.check_js_errors()


class TestWebPageSwitchIframe:
    def test_switch_to_iframe(self):
        mock_driver = MagicMock()
        with patch.object(WebPage, 'get'):
            page = WebPage(mock_driver)
            page.switch_to_iframe("my_frame")
            mock_driver.switch_to.frame.assert_called_once_with("my_frame")

    def test_switch_out_iframe(self):
        mock_driver = MagicMock()
        with patch.object(WebPage, 'get'):
            page = WebPage(mock_driver)
            page.switch_out_iframe()
            mock_driver.switch_to.default_content.assert_called_once()


class TestWebPageSwitchToAlertAccept:
    def test_switch_to_alert_accept(self):
        mock_driver = MagicMock()
        with patch.object(WebPage, 'get'):
            page = WebPage(mock_driver)
            page.switch_to_alert_accept()
            mock_driver.switch_to.alert.accept.assert_called_once()
