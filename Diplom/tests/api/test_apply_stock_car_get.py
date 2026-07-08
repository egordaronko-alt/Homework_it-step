import requests
import pytest
import allure


BASE_URL = "https://belgee.by"
API_URL = f"{BASE_URL}/api/apply-stock-car"


@allure.feature("Тесты API")
@allure.story("Проверка GET метода apply-stock-car")
class TestApplyStockCarGet:

    @allure.title("GET запрос возвращает статус код 405")
    def test_get_returns_405(self):
        with allure.step("Выполн GET запрос к API"):
            response = requests.get(url=API_URL)

        with allure.step("Проверка статус кода 405"):
            assert response.status_code == 405

    @allure.title("GET запрос возвращает заголовок Allow: POST")
    def test_get_allow_header_post(self):
        with allure.step("Выполн GET запрос к API"):
            response = requests.get(url=API_URL)

        with allure.step("Проверка заголовка Allow"):
            assert response.headers.get("Allow") == "POST"

    @allure.title("GET запрос возвращает Content-Type text/html")
    def test_get_content_type_html(self):
        with allure.step("Выполн GET запрос к API"):
            response = requests.get(url=API_URL)

        with allure.step("Проверка Content-Type"):
            assert "text/html" in response.headers.get("content-type", "")

    @allure.title("GET запрос не возвращает JSON")
    def test_get_not_json(self):
        with allure.step("Выполн GET запрос к API"):
            response = requests.get(url=API_URL)

        with allure.step("Проверка что ответ не JSON"):
            assert "application/json" not in response.headers.get("content-type", "")

    @allure.title("GET запрос возвращает тело ответа")
    def test_get_has_body(self):
        with allure.step("Выполн GET запрос к API"):
            response = requests.get(url=API_URL)

        with allure.step("Проверка что тело ответа не пустое"):
            assert len(response.text) > 0

    @allure.title("GET запрос с параметрами также возвращает 405")
    def test_get_with_query_params(self):
        with allure.step("Выполн GET запрос с query параметрами"):
            response = requests.get(
                url=API_URL,
                params={"name": "test", "phone": "+375291234567"},
            )

        with allure.step("Проверка статус кода 405"):
            assert response.status_code == 405

    @allure.title("HEAD запрос возвращает 405")
    def test_head_returns_405(self):
        with allure.step("Выполн HEAD запрос к API"):
            response = requests.head(url=API_URL)

        with allure.step("Проверка статус кода 405"):
            assert response.status_code == 405

    @allure.title("PUT запрос возвращает 405")
    def test_put_returns_405(self):
        with allure.step("Выполн PUT запрос к API"):
            response = requests.put(url=API_URL, json={})

        with allure.step("Проверка статус кода 405"):
            assert response.status_code == 405

    @allure.title("DELETE запрос возвращает 405")
    def test_delete_returns_405(self):
        with allure.step("Выполн DELETE запрос к API"):
            response = requests.delete(url=API_URL)

        with allure.step("Проверка статус кода 405"):
            assert response.status_code == 405

    @allure.title("PATCH запрос возвращает 405")
    def test_patch_returns_405(self):
        with allure.step("Выполн PATCH запрос к API"):
            response = requests.patch(url=API_URL, json={})

        with allure.step("Проверка статус кода 405"):
            assert response.status_code == 405
