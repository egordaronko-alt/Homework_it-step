import requests
import pytest
import allure


@allure.feature("Тесты API")
@allure.story("Проверка статус кода")
class TestApiActivities():
    @pytest.mark.parametrize('status_code, url, name_of_site', [
        (200, "https://belgee.by/lizing", "Лизинг"),
        (200, "https://belgee.by/kredit", "Кредит"),
        (200, "https://belgee.by/manual", "Руководство пользователя"),
        (200, "https://belgee.by/sto", "СТО BELGEE"),
        (200, "https://belgee.by/stat-dilerom", "Стать дилером"),
        (200, "https://belgee.by/service-values", "Ценности официального"),
        (200, "https://belgee.by/magazin", "Магазин"),
        (200, "https://belgee.by/gostinica", "Гостиница"),
        (200, "https://belgee.by/promo", "Акции"),
        (200, "https://belgee.by/sovety-po-ekspluatacii-avtomobilya-belgee", "Советы по эксплуатац"),
        (200, "https://belgee.by/infoliniya-belgee", "Инфолиния"),
        (200, "https://belgee.by/pomosh-na-dorogah-kruglosutochnaya-podderzhka-vladelcev-belgee", "Помощь на дорогах"),
        (200, "https://belgee.by/news", "Новости"),
        (200, "https://belgee.by/postavshikam", "Поставщикам"),
        (200, "https://belgee.by/about", "О предприятии")
    ])
    @allure.title("Провeрка статус кода страниц на экране main")
    def test_api_belgee_get(self, status_code, name_of_site, url):
        with allure.step("Вызов ручки ..."):
            response = requests.get(url=url)

        with allure.step(f"Проверка статус кода страницы {name_of_site}"):
            assert response.status_code == status_code



        # assert data["id"] == data_id
        # assert data["title"] == data_title
        # assert data["description"] == data_description
        # assert data["pageCount"] == data_page_count
        # assert data["excerpt"] == data_excerpt
        # assert data["publishDate"] == data_publish_date
        #
        # assert isinstance(data["id"], int)
        # assert isinstance(data["title"], str)
        # assert isinstance(data["description"], str)
        # assert isinstance(data["pageCount"], int)
        # assert isinstance(data["excerpt"], str)
        # assert isinstance(data["publishDate"], str)

# @pytest.mark.parametrize('data_id, status_code',
#     [
#         (1, 200),
#         (-100, 404),
#     ]
#     )
# def test_api_v1_books_get(data_id, status_code):
#
#     url = f'https://fakerestapi.azurewebsites.net/api/v1/Books/{data_id}'
#
#     response = requests.get(url=url)
#
#     assert response.status_code == status_code
#
#     if status_code == 200:
#
#         data = response.json()
#
#         assert isinstance(data["id"], int)
#         assert isinstance(data["title"], str)
#         assert isinstance(data["description"], str)
#         assert isinstance(data["pageCount"], int)
#         assert isinstance(data["excerpt"], str)
#         assert isinstance(data["publishDate"], str)
#
#
# @pytest.mark.parametrize('data_id, data_title, data_description, data_page_count, data_excerpt, data_publish_date, status_code',
#     [
#         (1, "new title", "new description", 500, "new excerpt", "2026-05-18T18:06:56.633Z", 200),
#         (None, None, None, None, None, None, 400),
#     ]
# )
#
# def test_api_v1_books_put(data_id, data_title, data_description, data_page_count, data_excerpt, data_publish_date, status_code):
#
#     url = f'https://fakerestapi.azurewebsites.net/api/v1/Books/{data_id}'
#
#     payload = {
#         "id": data_id,
#         "title": data_title,
#         "description": data_description,
#         "pageCount": data_page_count,
#         "excerpt": data_excerpt,
#         "publishDate": data_publish_date
#     }
#
#     response = requests.put(url=url, json=payload)
#
#     assert response.status_code == status_code
#
#     if status_code == 200:
#
#         data = response.json()
#
#         assert data["id"] == data_id
#         assert data["title"] == data_title
#         assert data["description"] == data_description
#         assert data["pageCount"] == data_page_count
#
# @pytest.mark.parametrize( 'data_id, status_code',
#     [
#         (1, 200),
#         (-1, 404),
#     ]
#     )
#
# def test_api_v1_books_delete(data_id, status_code):
#
#     url = f'https://fakerestapi.azurewebsites.net/api/v1/Books/{data_id}'
#
#     response = requests.delete(url=url)
#
#     assert response.status_code == status_code
#
#     response_get = requests.get(url=url)
#     assert response_get.status_code == 404