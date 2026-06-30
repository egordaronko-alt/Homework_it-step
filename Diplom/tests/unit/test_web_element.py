import pytest
from unittest.mock import MagicMock, patch
from Diplom.pages.elements import WebElement


class TestWebElementInit:
    def test_init_default_timeout(self):
        el = WebElement(id="test")
        assert el._timeout == 10

    def test_init_custom_timeout(self):
        el = WebElement(timeout=5, id="test")
        assert el._timeout == 5

    def test_init_wait_after_click_false(self):
        el = WebElement(id="test")
        assert el._wait_after_click is False

    def test_init_wait_after_click_true(self):
        el = WebElement(wait_after_click=True, id="test")
        assert el._wait_after_click is True

    def test_init_locator_from_css_selector(self):
        el = WebElement(css_selector=".my-class")
        assert el._locator == ("css selector", ".my-class")

    def test_init_locator_from_xpath(self):
        el = WebElement(xpath="//div[@id='test']")
        assert el._locator == ("xpath", "//div[@id='test']")

    def test_init_locator_replaces_underscore_with_space(self):
        el = WebElement(data_test_attr="some_value")
        assert el._locator == ("data test attr", "some_value")


class TestWebElementFind:
    def test_find_returns_element(self):
        mock_driver = MagicMock()
        mock_element = MagicMock()
        el = WebElement(id="test")
        el._web_driver = mock_driver

        with patch('Diplom.pages.elements.WebDriverWait') as mock_wait:
            mock_wait.return_value.until.return_value = mock_element
            result = el.find()
            assert result == mock_element

    def test_find_returns_none_on_exception(self):
        mock_driver = MagicMock()
        el = WebElement(id="test")
        el._web_driver = mock_driver

        with patch('Diplom.pages.elements.WebDriverWait') as mock_wait:
            mock_wait.return_value.until.side_effect = Exception("timeout")
            result = el.find()
            assert result is None


class TestWebElementWaitToBeClickable:
    def test_returns_element_when_clickable(self):
        mock_driver = MagicMock()
        mock_element = MagicMock()
        el = WebElement(id="test")
        el._web_driver = mock_driver

        with patch('Diplom.pages.elements.WebDriverWait') as mock_wait:
            mock_wait.return_value.until.return_value = mock_element
            result = el.wait_to_be_clickable(check_visibility=False)
            assert result == mock_element

    def test_returns_none_on_exception(self):
        mock_driver = MagicMock()
        el = WebElement(id="test")
        el._web_driver = mock_driver

        with patch('Diplom.pages.elements.WebDriverWait') as mock_wait:
            mock_wait.return_value.until.side_effect = Exception("not clickable")
            result = el.wait_to_be_clickable(check_visibility=False)
            assert result is None


class TestWebElementIsClickable:
    def test_is_clickable_true(self):
        mock_driver = MagicMock()
        mock_element = MagicMock()
        el = WebElement(id="test")
        el._web_driver = mock_driver

        with patch.object(el, 'wait_to_be_clickable', return_value=mock_element):
            assert el.is_clickable() is True

    def test_is_clickable_false(self):
        mock_driver = MagicMock()
        el = WebElement(id="test")
        el._web_driver = mock_driver

        with patch.object(el, 'wait_to_be_clickable', return_value=None):
            assert el.is_clickable() is False


class TestWebElementIsPresented:
    def test_is_presented_true(self):
        mock_driver = MagicMock()
        mock_element = MagicMock()
        el = WebElement(id="test")
        el._web_driver = mock_driver

        with patch.object(el, 'find', return_value=mock_element):
            assert el.is_presented() is True

    def test_is_presented_false(self):
        mock_driver = MagicMock()
        el = WebElement(id="test")
        el._web_driver = mock_driver

        with patch.object(el, 'find', return_value=None):
            assert el.is_presented() is False


class TestWebElementIsVisible:
    def test_is_visible_true(self):
        mock_driver = MagicMock()
        mock_element = MagicMock()
        mock_element.is_displayed.return_value = True
        el = WebElement(id="test")
        el._web_driver = mock_driver

        with patch.object(el, 'find', return_value=mock_element):
            assert el.is_visible() is True

    def test_is_visible_false_when_element_none(self):
        mock_driver = MagicMock()
        el = WebElement(id="test")
        el._web_driver = mock_driver

        with patch.object(el, 'find', return_value=None):
            assert el.is_visible() is False

    def test_is_visible_false_when_not_displayed(self):
        mock_driver = MagicMock()
        mock_element = MagicMock()
        mock_element.is_displayed.return_value = False
        el = WebElement(id="test")
        el._web_driver = mock_driver

        with patch.object(el, 'find', return_value=mock_element):
            assert el.is_visible() is False


class TestWebElementSendKeys:
    def test_send_keys_success(self):
        mock_driver = MagicMock()
        mock_element = MagicMock()
        el = WebElement(id="test")
        el._web_driver = mock_driver

        with patch.object(el, 'find', return_value=mock_element):
            el.send_keys("hello world", wait=0)
            mock_element.click.assert_called_once()
            mock_element.clear.assert_called_once()
            mock_element.send_keys.assert_called_once_with("hello world")

    def test_send_keys_replaces_newline(self):
        mock_driver = MagicMock()
        mock_element = MagicMock()
        el = WebElement(id="test")
        el._web_driver = mock_driver

        with patch.object(el, 'find', return_value=mock_element):
            el.send_keys("line1\nline2", wait=0)
            mock_element.send_keys.assert_called_once_with("line1\ue007line2")

    def test_send_keys_raises_when_element_not_found(self):
        mock_driver = MagicMock()
        el = WebElement(id="test")
        el._web_driver = mock_driver

        with patch.object(el, 'find', return_value=None):
            with pytest.raises(AttributeError, match="not found"):
                el.send_keys("hello")


class TestWebElementGetText:
    def test_get_text_success(self):
        mock_driver = MagicMock()
        mock_element = MagicMock()
        mock_element.text = "some text"
        el = WebElement(id="test")
        el._web_driver = mock_driver

        with patch.object(el, 'find', return_value=mock_element):
            assert el.get_text() == "some text"

    def test_get_text_empty_on_exception(self):
        mock_driver = MagicMock()
        mock_element = MagicMock()
        type(mock_element).text = property(lambda self: (_ for _ in ()).throw(Exception("error")))
        el = WebElement(id="test")
        el._web_driver = mock_driver

        with patch.object(el, 'find', return_value=mock_element):
            result = el.get_text()
            assert result == ""


class TestWebElementGetAttribute:
    def test_get_attribute_success(self):
        mock_driver = MagicMock()
        mock_element = MagicMock()
        mock_element.get_attribute.return_value = "value123"
        el = WebElement(id="test")
        el._web_driver = mock_driver

        with patch.object(el, 'find', return_value=mock_element):
            assert el.get_attribute("data-id") == "value123"
            mock_element.get_attribute.assert_called_once_with("data-id")

    def test_get_attribute_returns_none_when_element_not_found(self):
        mock_driver = MagicMock()
        el = WebElement(id="test")
        el._web_driver = mock_driver

        with patch.object(el, 'find', return_value=None):
            assert el.get_attribute("data-id") is None


class TestWebElementSetValue:
    def test_set_value_clears_and_sends(self):
        mock_driver = MagicMock()
        mock_element = MagicMock()
        el = WebElement(id="test")
        el._web_driver = mock_driver

        with patch.object(el, 'find', return_value=mock_element):
            el._set_value(mock_driver, "new value")
            mock_element.clear.assert_called_once()
            mock_element.send_keys.assert_called_once_with("new value")

    def test_set_value_without_clear(self):
        mock_driver = MagicMock()
        mock_element = MagicMock()
        el = WebElement(id="test")
        el._web_driver = mock_driver

        with patch.object(el, 'find', return_value=mock_element):
            el._set_value(mock_driver, "new value", clear=False)
            mock_element.clear.assert_not_called()
            mock_element.send_keys.assert_called_once_with("new value")


class TestWebElementClick:
    def test_click_success(self):
        mock_driver = MagicMock()
        mock_element = MagicMock()
        el = WebElement(id="test")
        el._web_driver = mock_driver
        el._page = MagicMock()

        with patch.object(el, 'wait_to_be_clickable', return_value=mock_element):
            with patch('Diplom.pages.elements.ActionChains') as mock_actions:
                el.click()
                mock_actions.assert_called_once_with(mock_driver)

    def test_click_raises_when_element_not_found(self):
        mock_driver = MagicMock()
        el = WebElement(id="test")
        el._web_driver = mock_driver

        with patch.object(el, 'wait_to_be_clickable', return_value=None):
            with pytest.raises(AttributeError, match="not found"):
                el.click()


class TestWebElementRightMouseClick:
    def test_right_click_success(self):
        mock_driver = MagicMock()
        mock_element = MagicMock()
        el = WebElement(id="test")
        el._web_driver = mock_driver

        with patch.object(el, 'wait_to_be_clickable', return_value=mock_element):
            with patch('Diplom.pages.elements.ActionChains') as mock_actions:
                el.right_mouse_click()
                mock_actions.assert_called_once_with(mock_driver)

    def test_right_click_raises_when_element_not_found(self):
        mock_driver = MagicMock()
        el = WebElement(id="test")
        el._web_driver = mock_driver

        with patch.object(el, 'wait_to_be_clickable', return_value=None):
            with pytest.raises(AttributeError, match="not found"):
                el.right_mouse_click()


class TestWebElementScrollToElement:
    def test_scroll_to_element(self):
        mock_driver = MagicMock()
        mock_element = MagicMock()
        el = WebElement(id="test")
        el._web_driver = mock_driver

        with patch.object(el, 'find', return_value=mock_element):
            el.scroll_to_element()
            mock_driver.execute_script.assert_called_once_with(
                "arguments[0].scrollIntoView();", mock_element
            )


class TestWebElementDelete:
    def test_delete_element(self):
        mock_driver = MagicMock()
        mock_element = MagicMock()
        el = WebElement(id="test")
        el._web_driver = mock_driver

        with patch.object(el, 'find', return_value=mock_element):
            el.delete()
            mock_driver.execute_script.assert_called_once_with(
                "arguments[0].remove();", mock_element
            )
