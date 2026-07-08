import requests
import pytest
import allure
import re


BASE_URL = "https://belgee.by"
API_URL = f"{BASE_URL}/api/apply-stock-car"


def get_session_with_csrf():
    session = requests.Session()
    r = session.get(BASE_URL)
    csrf_match = re.search(r'csrf-token.*?content="(.*?)"', r.text)
    csrf = csrf_match.group(1) if csrf_match else ""
    headers = {
        "X-CSRF-TOKEN": csrf,
        "X-Requested-With": "XMLHttpRequest",
        "Referer": BASE_URL + "/",
    }
    return session, headers


@allure.feature("Тесты API")
@allure.story("Проверка методов API apply-stock-car")
class TestApplyStockCar:

    @allure.title("GET запрос возвращает 405 Method Not Allowed")
    def test_get_method_not_allowed(self):
        with allure.step("Выполн GET запрос к API"):
            response = requests.get(url=API_URL)

        with allure.step("Проверка статус кода 405"):
            assert response.status_code == 405

    @allure.title("POST запрос с пустым телом возвращает 422")
    def test_post_empty_body(self):
        session, headers = get_session_with_csrf()

        with allure.step("Выполн POST запрос с пустым телом"):
            response = session.post(url=API_URL, data={}, headers=headers)

        with allure.step("Проверка статус кода 422"):
            assert response.status_code == 422

        with allure.step("Проверка наличия ошибок валидации"):
            data = response.json()
            assert "errors" in data
            assert "i_agree" in data["errors"]
            assert "name" in data["errors"]
            assert "phone" in data["errors"]

    @allure.title("POST запрос без i_agree возвращает 422")
    def test_post_without_i_agree(self):
        session, headers = get_session_with_csrf()

        with allure.step("Выполн POST запрос без поля i_agree"):
            response = session.post(
                url=API_URL,
                data={"name": "Тест", "phone": "+375291234567"},
                headers=headers,
            )

        with allure.step("Проверка статус кода 422"):
            assert response.status_code == 422

        with allure.step("Проверка ошибки для i_agree"):
            data = response.json()
            assert "i_agree" in data["errors"]

    @allure.title("POST запрос без name возвращает 422")
    def test_post_without_name(self):
        session, headers = get_session_with_csrf()

        with allure.step("Выполн POST запрос без поля name"):
            response = session.post(
                url=API_URL,
                data={"phone": "+375291234567", "i_agree": "1"},
                headers=headers,
            )

        with allure.step("Проверка статус кода 422"):
            assert response.status_code == 422

        with allure.step("Проверка ошибки для name"):
            data = response.json()
            assert "name" in data["errors"]

    @allure.title("POST запрос без phone возвращает 422")
    def test_post_without_phone(self):
        session, headers = get_session_with_csrf()

        with allure.step("Выполн POST запрос без поля phone"):
            response = session.post(
                url=API_URL,
                data={"name": "Тест", "i_agree": "1"},
                headers=headers,
            )

        with allure.step("Проверка статус кода 422"):
            assert response.status_code == 422

        with allure.step("Проверка ошибки для phone"):
            data = response.json()
            assert "phone" in data["errors"]

    @allure.title("POST запрос с некорректным номером телефона")
    def test_post_invalid_phone(self):
        session, headers = get_session_with_csrf()

        with allure.step("Выполн POST запрос с невалидным номером"):
            response = session.post(
                url=API_URL,
                data={"name": "Тест", "phone": "123", "i_agree": "1"},
                headers=headers,
            )

        with allure.step("Проверка статус кода 422"):
            assert response.status_code == 422

        with allure.step("Проверка ошибки для phone"):
            data = response.json()
            assert "phone" in data["errors"]

    @allure.title("POST запрос с пустым name возвращает 422")
    def test_post_empty_name(self):
        session, headers = get_session_with_csrf()

        with allure.step("Выполн POST запрос с пустым name"):
            response = session.post(
                url=API_URL,
                data={"name": "", "phone": "+375291234567", "i_agree": "1"},
                headers=headers,
            )

        with allure.step("Проверка статус кода 422"):
            assert response.status_code == 422

    @allure.title("POST запрос с валидными данными")
    def test_post_valid_data(self):
        session, headers = get_session_with_csrf()

        with allure.step("Выполн POST запрос с валидными данными"):
            response = session.post(
                url=API_URL,
                data={
                    "name": "Тест Тестович",
                    "phone": "+375291234567",
                    "i_agree": "1",
                },
                headers=headers,
            )

        with allure.step("Проверка что ответ не 422 (валидация пройдена)"):
            assert response.status_code != 422

    @allure.title("POST запрос с Content-Type application/json")
    def test_post_json_content_type(self):
        session, headers = get_session_with_csrf()
        headers["Content-Type"] = "application/json"

        with allure.step("Выполн POST запрос с JSON телом"):
            response = session.post(
                url=API_URL,
                json={
                    "name": "Тест Тестович",
                    "phone": "+375291234567",
                    "i_agree": True,
                },
                headers=headers,
            )

        with allure.step("Проверка что сервер обработал запрос"):
            assert response.status_code in [200, 422, 500]

    @allure.title("POST запрос с X-Requested-With XMLHttpRequest")
    def test_post_xhr_header(self):
        session, headers = get_session_with_csrf()

        with allure.step("Выполн POST запрос с XHR заголовком"):
            response = session.post(
                url=API_URL,
                data={"name": "Тест", "phone": "+375291234567", "i_agree": "1"},
                headers=headers,
            )

        with allure.step("Проверка что ответ содержит JSON"):
            assert "application/json" in response.headers.get("content-type", "")

    @allure.title("Ответ API содержит message при ошибке валидации")
    def test_response_contains_message(self):
        session, headers = get_session_with_csrf()

        with allure.step("Выполн POST запрос с пустым телом"):
            response = session.post(url=API_URL, data={}, headers=headers)

        with allure.step("Проверка наличия поля message"):
            data = response.json()
            assert "message" in data
            assert isinstance(data["message"], str)

    @allure.title("Ответ API содержит errors при ошибке валидации")
    def test_response_contains_errors(self):
        session, headers = get_session_with_csrf()

        with allure.step("Выполн POST запрос с пустым телом"):
            response = session.post(url=API_URL, data={}, headers=headers)

        with allure.step("Проверка наличия поля errors"):
            data = response.json()
            assert "errors" in data
            assert isinstance(data["errors"], dict)
