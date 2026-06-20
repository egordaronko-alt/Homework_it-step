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
    #test header
    #models switcher
    models_switcher = WebElement(css_selector='div.w-header-inset-dropper._js-header-inset-dropper')
    header_models = WebElement(css_selector='span.dashed')
    many_models = ManyWebElements(css_selector='.col-md-3.col-sm-3.col-4.pb-10')
    #models links
    model_S50_link = WebElement(css_selector='img[src*="w300_h200_dzylmn18v0ls4xg1bgep.png"]')
    model_X50_link = WebElement(css_selector='img[src*="w300_h200_uogzrfwzjdl9svcpzj57.png"]')
    model_X50plus_link = WebElement(css_selector='img[src*="w300_h200_44a9oqstp6l9jkoe7kui.png"]')
    model_X70_link = WebElement(css_selector='img[src*="w300_h200_m9xovvg3ffjp3bh9xmjl.png"]')
    model_X80_link = WebElement(css_selector="img[src*='w300_h200_f5y8il8onsgrnqplsmeg.png']")

    special_deal_akcii = WebElement(css_selektor='a[href="https://belgee.by/promo"].__link')
    special_deals_menu = WebElement(xpath='//span[text()="Специальные предложения"]')

