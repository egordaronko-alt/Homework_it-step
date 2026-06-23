from Diplom.pages.elements import WebElement, ManyWebElements
from Diplom.pages.base_page import WebPage
import os


class MainPage(WebPage):

    def __init__(self, web_driver, url=''):
        if not url:
            url = os.getenv("MAIN_PAGE") or 'https://belgee.by/'
        super().__init__(web_driver, url)
    #accept cookies
    accept_cookie = WebElement(css_selector='.button.big._js-b-cookie-alert._js-cookie-save-all')
    #close pop window
    pop_window = WebElement(css_selector='.close._js-pop-close')

                                            #Тестирование хедера Belgee.by
    #Локаторы моделей
    models_switcher = WebElement(css_selector='div.w-header-inset-dropper._js-header-inset-dropper')
    header_models = WebElement(css_selector='span.dashed')
    many_models = ManyWebElements(css_selector='.col-md-3.col-sm-3.col-4.pb-10')
    #Локаторы ссылок на модели
    model_S50_link = WebElement(css_selector='img[src*="w300_h200_dzylmn18v0ls4xg1bgep.png"]')
    model_X50_link = WebElement(css_selector='img[src*="w300_h200_uogzrfwzjdl9svcpzj57.png"]')
    model_X50plus_link = WebElement(css_selector='img[src*="w300_h200_44a9oqstp6l9jkoe7kui.png"]')
    model_X70_link = WebElement(css_selector='img[src*="w300_h200_m9xovvg3ffjp3bh9xmjl.png"]')
    model_X80_link = WebElement(css_selector="img[src*='w300_h200_f5y8il8onsgrnqplsmeg.png']")

    #Тестирование футера "Специальные предложения"
    special_deal_menu = WebElement(xpath='//span[text()="Специальные предложения"]')
    special_deal_promo = WebElement(xpath='//a[@href="https://belgee.by/promo" and text()="Акции"]')
    special_deal_leasing = WebElement(xpath='//a[@href="https://belgee.by/lizing" and text()="Лизинг"]')
    special_deal_kredit = WebElement(xpath='//a[@href="https://belgee.by/kredit" and text()="Кредит"]')

    #Тестирование "Владельцу"
    owner_main_link = WebElement(xpath='//li/a/span[text()="Владельцу"]')
    owner_user_manual = WebElement(css_selector='a[href="https://belgee.by/manual"][class="__link"]')
    owner_hundred_belgee = WebElement(css_selector='a[href="https://belgee.by/sto"][class="__link"]')
    owner_core_values = WebElement(css_selector='a[href="https://belgee.by/service-values"][class="__link"]')
    owner_expluatation_advice = WebElement(css_selector='a[href="https://belgee.by/sovety-po-ekspluatacii-avtomobilya-belgee"][class ="__link"]')
    owner_info_line = WebElement(css_selector='a[href="https://belgee.by/infoliniya-belgee"][class="__link"]')
    owner_road_help = WebElement(css_selector='a[href="https://belgee.by/pomosh-na-dorogah-kruglosutochnaya-podderzhka-vladelcev-belgee"][class="__link"]')
    #Тестирование "СЗАО БЕЛДЖИ"
    czao_main_link = WebElement(xpath='//li/a/span[text()="СЗАО БЕЛДЖИ"]')
    czao_news = WebElement(css_selector='li div ul li a[target="_self"][href="https://belgee.by/news"]')
    czao_about = WebElement(css_selector='li div ul li a[target="_self"][href="https://belgee.by/about"]')
    czao_suppliers = WebElement(css_selector='li div ul li a[target="_self"][href="https://belgee.by/postavshikam"]')
    czao_diller = WebElement(css_selector='li div ul li a[target="_self"][href="https://belgee.by/stat-dilerom"]')
    czao_hotel = WebElement(css_selector='li div ul li a[target="_self"][href="https://belgee.by/gostinica"]')
    czao_shop = WebElement(css_selector='li div ul li a[target="_self"][href="https://belgee.by/magazin"]')
    czao_corruption = WebElement(css_selector='li div ul li a[href="https://belgee.by/protivodejstvie-korrupcii"]')
    czao_vacancy = WebElement(css_selector='li div ul li a[href="https://belgee.by/vakansii"]')