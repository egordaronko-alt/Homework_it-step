import os
from Diplom.pages.elements import WebElement, ManyWebElements
from Diplom.pages.base_page import WebPage


class MainPage(WebPage):
    def __init__(self, web_driver, url=''):
        if not url:
            url = os.getenv("MAIN_PAGE") or 'https://belgee.by/'

        super().__init__(web_driver, url)

    btn_catalog = WebElement(xpath='//h1')