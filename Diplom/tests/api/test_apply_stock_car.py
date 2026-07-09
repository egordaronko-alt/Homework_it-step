import requests
import pytest
import allure
import re


BASE_URL = "https://belgee.by"
API_URL = f"{BASE_URL}/api/apply-stock-car"


def get_session_with_csrf(api_session):
    r = api_session.get(BASE_URL, timeout=15)
    csrf_match = re.search('csrf-token.*?content="(.*?)"', r.text)
    csrf = csrf_match.group(1) if csrf_match else ""
    headers = {
        "X-CSRF-TOKEN": csrf,
        "X-Requested-With": "XMLHttpRequest",
        "Referer": BASE_URL + "/",
    }
    return headers


@allure.feature("Тесты API")
@allure.story("Проверка методов API apply-stock-car")
class TestApplyStockCar:

    @allure.title("GET запрос возвращает 405 Method Not Allowed")
    def test_get_method_not_allowed(self, api_session):
        with allure.step("Выполнен GET запрос к API"):
            response = api_session.get(url=API_URL, timeout=15)

        with allure.step("Проверка статус кода 405"):
            assert response.status_code == 405

    @allure.title("POST запрос с пустым телом возвращает 422")
    def test_post_empty_body(self, api_session):
        headers = get_session_with_csrf(api_session)

        with allure.step("Выполнен POST запрос с пустым телом"):
            response = api_session.post(url=API_URL, data={}, headers=headers, timeout=15)

        with allure.step("Проверка статус кода 422"):
            assert response.status_code == 422

        with allure.step("Проверка наличия ошибок валидации"):
            data = response.json()
            assert "errors" in data
            assert "i_agree" in data["errors"]
            assert "name" in data["errors"]
            assert "phone" in data["errors"]

    @allure.title("POST запрос без i_agree возвращает 422")
    def test_post_without_i_agree(self, api_session):
        headers = get_session_with_csrf(api_session)

        with allure.step("Выполн POST запрос без поля i_agree"):
            response = api_session.post(
                url=API_URL,
                data={"name": "Тест", "phone": "+375291234567"},
                headers=headers,
                timeout=15)

        with allure.step("Проверка статус кода 422"):
            assert response.status_code == 422

        with allure.step("Проверка ошибки для i_agree"):
            data = response.json()
            assert "i_agree" in data["errors"]

    @allure.title("POST запрос без name возвращает 422")
    def test_post_without_name(self, api_session):
        headers = get_session_with_csrf(api_session)

        with allure.step("Выполн POST запрос без поля name"):
            response = api_session.post(
                url=API_URL,
                data={"phone": "+375291234567", "i_agree": "1"},
                headers=headers,
                timeout=15)

        with allure.step("Проверка статус кода 422"):
            assert response.status_code == 422

        with allure.step("Проверка ошибки для name"):
            data = response.json()
            assert "name" in data["errors"]

    @allure.title("POST запрос без phone возвращает 422")
    def test_post_without_phone(self, api_session):
        headers = get_session_with_csrf(api_session)

        with allure.step("Выполн POST запрос без поля phone"):
            response = api_session.post(
                url=API_URL,
                data={"name": "Тест", "i_agree": "1"},
                headers=headers,
                timeout=15)

        with allure.step("Проверка статус кода 422"):
            assert response.status_code == 422

        with allure.step("Проверка ошибки для phone"):
            data = response.json()
            assert "phone" in data["errors"]

    @allure.title("POST запрос с некорректным номером телефона")
    def test_post_invalid_phone(self, api_session):
        headers = get_session_with_csrf(api_session)

        with allure.step("Выполн POST запрос с невалидным номером"):
            response = api_session.post(
                url=API_URL,
                data={"name": "Тест", "phone": "123", "i_agree": "1"},
                headers=headers,
                timeout=15)

        with allure.step("Проверка статус кода 422"):
            assert response.status_code == 422

        with allure.step("Проверка ошибки для phone"):
            data = response.json()
            assert "phone" in data["errors"]

    @allure.title("POST запрос с пустым name возвращает 422")
    def test_post_empty_name(self, api_session):
        headers = get_session_with_csrf(api_session)

        with allure.step("Выполнение POST запроса с пустым name"):
            response = api_session.post(
                url=API_URL,
                data={"name": "", "phone": "+375291234567", "i_agree": "1"},
                headers=headers,
                timeout=15)

        with allure.step("Проверка статус кода 422"):
            assert response.status_code == 422

    @allure.title("POST запрос с валидными данными")
    def test_post_valid_data(self, api_session):
        headers = get_session_with_csrf(api_session)

        with allure.step("Выполнение POST запроса с валидными данными"):
            response = api_session.post(
                url=API_URL,
                data={
                    "name": "Тест Тестович",
                    "phone": "+375291234567",
                    "i_agree": "1",
                },
                headers=headers,
                timeout=15)

        with allure.step("Проверка что ответ не 422 (валидация пройдена)"):
            assert response.status_code != 422

    @allure.title("POST запрос с Content-Type application/json")
    def test_post_json_content_type(self, api_session):
        headers = get_session_with_csrf(api_session)
        headers["Content-Type"] = "application/json"

        with allure.step("Выполнение POST запрос с JSON телом"):
            response = api_session.post(
                url=API_URL,
                json={
                    "name": "Тест Тестович",
                    "phone": "+375291234567",
                    "i_agree": True,
                },
                headers=headers,
                timeout=15)

        with allure.step("Проверка что сервер обработал запрос"):
            assert response.status_code in [200, 422, 500]

    @allure.title("POST запрос с X-Requested-With XMLHttpRequest")
    def test_post_xhr_header(self, api_session):
        headers = get_session_with_csrf(api_session)

        with allure.step("Выполн POST запрос с XHR заголовком"):
            response = api_session.post(
                url=API_URL,
                data={"name": "Тест", "phone": "+375291234567", "i_agree": "1"},
                headers=headers,
                timeout=15)

        with allure.step("Проверка что ответ содержит JSON"):
            assert "application/json" in response.headers.get("content-type", "")

    @allure.title("Ответ API содержит message при ошибке валидации")
    def test_response_contains_message(self, api_session):
        headers = get_session_with_csrf(api_session)

        with allure.step("Выполнение POST запрос с пустым телом"):
            response = api_session.post(url=API_URL, data={}, headers=headers, timeout=15)

        with allure.step("Проверка наличия поля message"):
            data = response.json()
            assert "message" in data
            assert isinstance(data["message"], str)

    @allure.title("Ответ API содержит errors при ошибке валидации")
    def test_response_contains_errors(self, api_session):
        headers = get_session_with_csrf(api_session)

        with allure.step("Выполнение POST запрос с пустым телом"):
            response = api_session.post(url=API_URL, data={}, headers=headers, timeout=15)

        with allure.step("Проверка наличия поля errors"):
            data = response.json()
            assert "errors" in data
            assert isinstance(data["errors"], dict)
