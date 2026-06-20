import time
import pytest
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.action_chains import ActionChains

from Diplom.locators.main_locators import MainPage

def test_belgee(driver):
    page = MainPage(driver)
    page.accept_cookie.wait_to_be_clickable()
    page.accept_cookie.click()
    page.pop_window.wait_to_be_clickable()
    page.pop_window.click()
    # #Test models in models
    # page.header_models.click()
    # all_models = page.many_models.get_text()
    # list_of_models = ['S50', 'X50', 'X50+', 'X70', 'X80']
    # print(all_models)
    # for i in range(len(list_of_models)):
    #     assert list_of_models[i] in all_models[i], f'модель {list_of_models[i]} отсутствует в dropdown menu'
    # #Работоспособность ссылок перехода на модель автомобиля
    # #S50 the first
    # model_links = [page.model_S50_link,
    #                page.model_X50_link,
    #                page.model_X50plus_link,
    #                page.model_X70_link,
    #                page.model_X80_link]
    #
    # for i in range(len(model_links)):
    #     switcher = page.models_switcher.get_attribute('class')
    #     if "_toggled" not in switcher:
    #         page.models_switcher.click()
    #     model_links[i].wait_to_be_clickable()
    #     model_links[i].click()
    #     page.go_back()
    print(page.special_deal_akcii.find())
    # menu = page.special_deals_menu.find()
    # akcii = page.special_deal_akcii.find()
    #
    # actions = ActionChains(driver)
    # actions.move_to_element(menu) \
    #     .pause(1) \
    #     .move_to_element(akcii) \
    #     .pause(1) \
    #     .click() \
    #     .perform()
