import requests
import pytest
import allure


@allure.feature("Тесты API")
@allure.story("Проверка GET метода страниц belgee.by")
class TestGetPagesBelgee:

    BELGEE_PAGES = [
        ("https://belgee.by/", "Главная"),
        ("https://belgee.by/about", "О предприятии"),
        ("https://belgee.by/contacts", "Контакты"),
        ("https://belgee.by/cookie", "Cookie"),
        ("https://belgee.by/dealers", "Дилеры"),
        ("https://belgee.by/gostinica", "Гостиница"),
        ("https://belgee.by/infoliniya-belgee", "Инфолиния"),
        ("https://belgee.by/kredit", "Кредит"),
        ("https://belgee.by/lizing", "Лизинг"),
        ("https://belgee.by/magazin", "Магазин"),
        ("https://belgee.by/manual", "Руководство пользователя"),
        ("https://belgee.by/models/S50", "Модель S50"),
        ("https://belgee.by/models/X50", "Модель X50"),
        ("https://belgee.by/models/X50-plus", "Модель X50 Plus"),
        ("https://belgee.by/models/x70-new", "Модель X70 New"),
        ("https://belgee.by/models/x80-phev", "Модель X80 PHEV"),
        ("https://belgee.by/news", "Новости"),
        ("https://belgee.by/news/dilerskij-centra-na-kulmana-1-uzhe-otkryt-v-minske", "Новость: Дилерский центр"),
        ("https://belgee.by/news/iyun-pobil-vse-rekordy-bolee-4-300-novyh-avtomobilej-szao-beldzhi-na-dorogah-strany", "Новость: Июнь рекорды"),
        ("https://belgee.by/news/maksimalnaya-vygoda-na-avtomobili-belgee-tolko-do-konca-iyulya", "Новость: Максимальная выгода"),
        ("https://belgee.by/news/novye-rekordy-szao-beldzhi-podvedeny-itogi-maya-po-prodazham", "Новость: Рекорды мая"),
        ("https://belgee.by/news/novyj-dilerskij-centr-belgee-otkryt-v-minske", "Новость: Новый дилерский центр"),
        ("https://belgee.by/news/pomosh-na-dorogah-kruglosutochnaya-podderzhka-vladelcev-belgee", "Новость: Помощь на дорогах"),
        ("https://belgee.by/news/priglashaem-vas-na-vyezdnoj-test-drajv", "Новость: Тест-драйв"),
        ("https://belgee.by/news/razdelenie-brendov-geely-i-belgee", "Новость: Разделение брендов"),
        ("https://belgee.by/news/szao-beldzhi-podvelo-itogi-srazu-dvuh-konkursov-sredi-dilerskih-predpriyatij-po-prodazham-i-po-marketingu", "Новость: Итоги конкурсов"),
        ("https://belgee.by/pomosh-na-dorogah-kruglosutochnaya-podderzhka-vladelcev-belgee", "Помощь на дорогах"),
        ("https://belgee.by/postavshikam", "Поставщикам"),
        ("https://belgee.by/promo", "Акции"),
        ("https://belgee.by/protivodejstvie-korrupcii", "Противодействие коррупции"),
        ("https://belgee.by/service-values", "Ценности сервиса"),
        ("https://belgee.by/sovety-po-ekspluatacii-avtomobilya-belgee", "Советы по эксплуатации"),
        ("https://belgee.by/stat-dilerom", "Стать дилером"),
        ("https://belgee.by/sto", "СТО"),
        ("https://belgee.by/vakansii", "Вакансии"),
        ("https://belgee.by/storage/settings/February2025/KX4JJoK19RxyHERQLA27.pdf", "PDF документ"),
    ]

    @pytest.mark.parametrize("url, name", BELGEE_PAGES)
    @allure.title("GET запрос возвращает статус 200 - {name}")
    def test_get_page_returns_200(self, api_session, url, name):
        with allure.step(f"Выполнен GET запрос к {url}"):
            response = api_session.get(url=url, timeout=15)

        with allure.step(f"Проверка статус кода 200 для {name}"):
            assert response.status_code == 200, (
                f"Страница {name} вернула {response.status_code}, ожидался 200"
            )

    @pytest.mark.parametrize("url, name", [
        ("https://belgee.by/storage/settings/February2025/KX4JJoK19RxyHERQLA27.pdf", "PDF документ"),
    ])
    @allure.title("GET запрос PDF возвращает application/pdf - {name}")
    def test_get_pdf_content_type(self, api_session, url, name):
        with allure.step(f"Выполнен GET запрос к {url}"):
            response = api_session.get(url=url, timeout=15)

        with allure.step(f"Проверка Content-Type PDF для {name}"):
            content_type = response.headers.get("content-type", "")
            assert "pdf" in content_type.lower(), (
                f"Файл {name} вернул {content_type}, ожидался application/pdf"
            )
