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

    EXTERNAL_PAGES = [
        ("https://geelyautomobile.by/", "geelyautomobile.by"),
        ("https://t.me/belgee_belarus", "Telegram belgee"),
        ("https://www.instagram.com/belgee.official/", "Instagram belgee"),
        ("https://www.tiktok.com/@geely_belarus", "TikTok belgee"),
        ("https://www.youtube.com/@cjscbelgee-1840", "YouTube belgee"),
        ("https://zmitroc.by/", "zmitroc.by"),
    ]

    ALL_PAGES = BELGEE_PAGES + EXTERNAL_PAGES

    @pytest.mark.parametrize("url, name", ALL_PAGES)
    @allure.title("GET запрос возвращает статус 200 - {name}")
    def test_get_page_returns_200(self, url, name):
        with allure.step(f"Выполн GET запрос к {url}"):
            response = requests.get(url=url, timeout=30)

        with allure.step(f"Проверка статус кода 200 для {name}"):
            assert response.status_code == 200, (
                f"Страница {name} вернула {response.status_code}, ожидался 200"
            )

    @pytest.mark.parametrize("url, name", ALL_PAGES)
    @allure.title("GET запрос возвращает Content-Type - {name}")
    def test_get_page_content_type(self, url, name):
        with allure.step(f"Выполн GET запрос к {url}"):
            response = requests.get(url=url, timeout=30)

        with allure.step(f"Проверка Content-Type для {name}"):
            content_type = response.headers.get("content-type", "")
            assert content_type, f"Страница {name} не вернула Content-Type"

    @pytest.mark.parametrize("url, name", BELGEE_PAGES)
    @allure.title("GET запрос возвращает тело страницы - {name}")
    def test_get_page_has_body(self, url, name):
        with allure.step(f"Выполн GET запрос к {url}"):
            response = requests.get(url=url, timeout=30)

        with allure.step(f"Проверка что тело ответа не пустое для {name}"):
            assert len(response.text) > 0, f"Страница {name} вернула пустое тело"

    @pytest.mark.parametrize("url, name", [
        ("https://belgee.by/", "Главная"),
        ("https://belgee.by/about", "О предприятии"),
        ("https://belgee.by/models/S50", "Модель S50"),
        ("https://belgee.by/models/X50", "Модель X50"),
        ("https://belgee.by/models/X50-plus", "Модель X50 Plus"),
        ("https://belgee.by/models/x70-new", "Модель X70 New"),
        ("https://belgee.by/models/x80-phev", "Модель X80 PHEV"),
    ])
    @allure.title("GET запрос страницы модели содержит html - {name}")
    def test_get_model_page_is_html(self, url, name):
        with allure.step(f"Выполн GET запрос к {url}"):
            response = requests.get(url=url, timeout=30)

        with allure.step(f"Проверка что ответ HTML для {name}"):
            assert "text/html" in response.headers.get("content-type", ""), (
                f"Страница {name} не вернула HTML"
            )

    @pytest.mark.parametrize("url, name", [
        ("https://belgee.by/storage/settings/February2025/KX4JJoK19RxyHERQLA27.pdf", "PDF документ"),
    ])
    @allure.title("GET запрос PDF возвращает application/pdf - {name}")
    def test_get_pdf_content_type(self, url, name):
        with allure.step(f"Выполн GET запрос к {url}"):
            response = requests.get(url=url, timeout=30)

        with allure.step(f"Проверка Content-Type PDF для {name}"):
            content_type = response.headers.get("content-type", "")
            assert "pdf" in content_type.lower(), (
                f"Файл {name} вернул {content_type}, ожидался application/pdf"
            )

    @pytest.mark.parametrize("url, name", EXTERNAL_PAGES)
    @allure.title("GET запрос внешних ресурсов возвращает 200 - {name}")
    def test_get_external_resources_returns_200(self, url, name):
        with allure.step(f"Выполн GET запрос к {url}"):
            response = requests.get(url=url, timeout=30)

        with allure.step(f"Проверка статус кода 200 для {name}"):
            assert response.status_code == 200, (
                f"Ресурс {name} вернул {response.status_code}, ожидался 200"
            )
