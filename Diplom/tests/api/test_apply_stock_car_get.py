import requests
import pytest
import allure


BASE_URL = "https://belgee.by"
API_URL = f"{BASE_URL}/api/apply-stock-car"


@allure.feature("Тесты API")
@allure.story("Проверка GET метода apply-stock-car")
class TestApplyStockCarGet:

    @allure.title("GET запрос возвращает статус код 405")
    def test_get_returns_405(self, api_session):
        with allure.step("Выполнение GET запроса к API"):
            response = api_session.get(url=API_URL, timeout=15)

        with allure.step("Проверка статус кода 405"):
            assert response.status_code == 405

    @allure.title("GET запрос с параметрами также возвращает 405")
    def test_get_with_query_params(self, api_session):
        with allure.step("Выполнение GET запрос с query параметрами"):
            response = api_session.get(
                url=API_URL,
                params={"name": "test", "phone": "+375291234567"},
                timeout=15,
            )

        with allure.step("Проверка статус кода 405"):
            assert response.status_code == 405

    @allure.title("HEAD запрос возвращает 405")
    def test_head_returns_405(self, api_session):
        with allure.step("Выполнение HEAD запроса к API"):
            response = api_session.head(url=API_URL, timeout=15)

        with allure.step("Проверка статус кода 405"):
            assert response.status_code == 405

    @allure.title("PUT запрос возвращает 405")
    def test_put_returns_405(self, api_session):
        with allure.step("Выполнение PUT запроса к API"):
            response = api_session.put(url=API_URL, json={}, timeout=15)

        with allure.step("Проверка статус кода 405"):
            assert response.status_code == 405

    @allure.title("DELETE запрос возвращает 405")
    def test_delete_returns_405(self, api_session):
        with allure.step("Выполнение DELETE запроса к API"):
            response = api_session.delete(url=API_URL, timeout=15)

        with allure.step("Проверка статус кода 405"):
            assert response.status_code == 405

    @allure.title("PATCH запрос возвращает 405")
    def test_patch_returns_405(self, api_session):
        with allure.step("Выполнение PATCH запроса к API"):
            response = api_session.patch(url=API_URL, json={}, timeout=15)

        with allure.step("Проверка статус кода 405"):
            assert response.status_code == 405
