import pytest
from unittest.mock import MagicMock, patch
from Diplom.pages.elements import ManyWebElements, WebElement


class TestManyWebElementsInit:
    def test_inherits_from_web_element(self):
        el = ManyWebElements(id="test")
        assert isinstance(el, WebElement)

    def test_init_locator_from_css_selector(self):
        el = ManyWebElements(css_selector=".my-class")
        assert el._locator == ("css selector", ".my-class")


class TestManyWebElementsFind:
    def test_find_returns_list(self):
        mock_driver = MagicMock()
        mock_elements = [MagicMock(), MagicMock(), MagicMock()]
        el = ManyWebElements(id="test")
        el._web_driver = mock_driver

        with patch('Diplom.pages.elements.WebDriverWait') as mock_wait:
            mock_wait.return_value.until.return_value = mock_elements
            result = el.find()
            assert result == mock_elements
            assert len(result) == 3

    def test_find_returns_empty_list_on_exception(self):
        mock_driver = MagicMock()
        el = ManyWebElements(id="test")
        el._web_driver = mock_driver

        with patch('Diplom.pages.elements.WebDriverWait') as mock_wait:
            mock_wait.return_value.until.side_effect = Exception("timeout")
            result = el.find()
            assert result == []


class TestManyWebElementsGetItem:
    def test_getitem_returns_correct_element(self):
        mock_driver = MagicMock()
        mock_elements = [MagicMock(name="elem0"), MagicMock(name="elem1")]
        el = ManyWebElements(id="test")
        el._web_driver = mock_driver

        with patch.object(el, 'find', return_value=mock_elements):
            assert el[0] == mock_elements[0]
            assert el[1] == mock_elements[1]

    def test_getitem_out_of_range(self):
        mock_driver = MagicMock()
        mock_elements = [MagicMock()]
        el = ManyWebElements(id="test")
        el._web_driver = mock_driver

        with patch.object(el, 'find', return_value=mock_elements):
            with pytest.raises(IndexError):
                el[5]


class TestManyWebElementsCount:
    def test_count_returns_length(self):
        mock_driver = MagicMock()
        mock_elements = [MagicMock(), MagicMock(), MagicMock(), MagicMock()]
        el = ManyWebElements(id="test")
        el._web_driver = mock_driver

        with patch.object(el, 'find', return_value=mock_elements):
            assert el.count() == 4

    def test_count_returns_zero_for_empty(self):
        mock_driver = MagicMock()
        el = ManyWebElements(id="test")
        el._web_driver = mock_driver

        with patch.object(el, 'find', return_value=[]):
            assert el.count() == 0


class TestManyWebElementsGetText:
    def test_get_text_returns_list(self):
        mock_driver = MagicMock()
        elem1 = MagicMock()
        elem1.text = "hello"
        elem2 = MagicMock()
        elem2.text = "world"
        el = ManyWebElements(id="test")
        el._web_driver = mock_driver

        with patch.object(el, 'find', return_value=[elem1, elem2]):
            result = el.get_text()
            assert result == ["hello", "world"]

    def test_get_text_handles_exception(self):
        mock_driver = MagicMock()
        elem_ok = MagicMock()
        elem_ok.text = "ok"
        elem_err = MagicMock()
        type(elem_err).text = property(lambda self: (_ for _ in ()).throw(Exception("error")))
        el = ManyWebElements(id="test")
        el._web_driver = mock_driver

        with patch.object(el, 'find', return_value=[elem_ok, elem_err]):
            result = el.get_text()
            assert result[0] == "ok"
            assert result[1] == ""


class TestManyWebElementsGetAttribute:
    def test_get_attribute_returns_list(self):
        mock_driver = MagicMock()
        elem1 = MagicMock()
        elem1.get_attribute.return_value = "val1"
        elem2 = MagicMock()
        elem2.get_attribute.return_value = "val2"
        el = ManyWebElements(id="test")
        el._web_driver = mock_driver

        with patch.object(el, 'find', return_value=[elem1, elem2]):
            result = el.get_attribute("data-id")
            assert result == ["val1", "val2"]
            elem1.get_attribute.assert_called_with("data-id")
            elem2.get_attribute.assert_called_with("data-id")


class TestManyWebElementsSetValue:
    def test_set_value_raises_error(self):
        el = ManyWebElements(id="test")
        el._web_driver = MagicMock()

        with pytest.raises(TypeError):
            el._set_value(MagicMock(), "value")


class TestManyWebElementsClick:
    def test_click_raises_error(self):
        el = ManyWebElements(id="test")
        el._web_driver = MagicMock()

        with pytest.raises(TypeError):
            el.click()
