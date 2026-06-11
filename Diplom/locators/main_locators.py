import os
from Diplom.pages.elements import WebElement, ManyWebElements
from Diplom.pages.base_page import WebPage


class MainPage(WebPage):
    def __init__(self, web_driver, url=''):
        if not url:
            url = os.getenv("MAIN_PAGE") or 'https://belgee.by/'

        super().__init__(web_driver, url)

    accept_cookie = WebElement(xpath='//a[@class="button big _js-b-cookie-alert _js-cookie-save-all"]')
    btn_catalog = WebElement(xpath='//h1')
    text_of_footer = WebElement(xpath='//span[text()="Специальные предложения"]')
    models = WebElement(xpath='//span[@class="dashed"]')
    model_S50 = WebElement(xpath='/html/body/div[1]/header/div[2]/div/div/div/div/div[2]/div[2]/div//span[text()="S50"]')
    model_X50 = WebElement(xpath='/html/body/div[1]/header/div[2]/div/div/div/div/div[2]/div[2]/div/div/div/div/div/div/div[2]/div/a/div[2]/span')
    model_x50plus = WebElement(xpath='//span[contains(text(), "X50+")]')
    model_x70 = WebElement(xpath='//span[contains(text(), "X70")]')
    model_x80PHEV = WebElement(xpath='//span[contains(text(), "X80")]')