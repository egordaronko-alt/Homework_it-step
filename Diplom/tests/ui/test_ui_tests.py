import time
import pytest
import requests
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.action_chains import ActionChains
from Diplom.locators.main_locators import MainPage
from selenium.webdriver.common.keys import Keys

def test_belgee(driver):
    page = MainPage(driver)
    page.accept_cookie.click()
    page.pop_window.wait_to_be_clickable()
    page.pop_window.click()
    page.wait_page_loaded(check_images=True, scroll_page=False)
    time.sleep(3)

# #Test models in models
#     page.header_models.click()
#     all_models = page.many_models.get_text()
#     list_of_models = ['S50', 'X50', 'X50+', 'X70', 'X80']
#     print(all_models)
#     for i in range(len(list_of_models)):
#         assert list_of_models[i] in all_models[i], f'модель {list_of_models[i]} отсутствует в dropdown menu'
#
# #Работоспособность ссылок перехода на модель автомобиля
#     model_links = [page.model_S50_link,
#                    page.model_X50_link,
#                    page.model_X50plus_link,
#                    page.model_X70_link,
#                    page.model_X80_link]
#     switcher = page.models_switcher.get_attribute('class')
#     for i in range(len(model_links)):
#         time.sleep(2)
#         if "_toggled" not in switcher:
#             page.models_switcher.click()
#         model_links[i].wait_to_be_clickable()
#         model_links[i].click()
#         page.go_back()
#     if "_toggled" in switcher:
#         page.models_switcher.click()
#
#
# # Тест меню "Специальные предложения"
#     menu = page.special_deal_menu.find()
#
#     special_deal_list = [page.special_deal_promo,
#                          page.special_deal_leasing,
#                          page.special_deal_kredit]
#
#     actions = ActionChains(driver)
#     for item in special_deal_list:
#         page.wait_page_loaded(sleep_time=1.5)
#         actions.move_to_element(menu) \
#           .move_to_element(item.find()) \
#           .click() \
#           .perform()
#         page.wait_page_loaded(sleep_time=0.5)
#         page.go_back()
#
# #Тест меню "Владельцу"
#     owner = page.owner_main_link.find()
#
#     owner_list = [page.owner_user_manual,
#                   page.owner_hundred_belgee,
#                   page.owner_core_values,
#                   page.owner_expluatation_advice,
#                   page.owner_info_line,
#                   page.owner_road_help]
#     actions = ActionChains(driver)
#     for element in owner_list:
#         page.wait_page_loaded(sleep_time=1.5)
#         actions.move_to_element(owner) \
#           .move_to_element(element.find()) \
#           .click() \
#           .perform()
#         page.wait_page_loaded(sleep_time=0.5)
#         page.go_back()
# #Тест меню "СЗАО БЕЛДЖИ"
#     czao_main = page.czao_main_link.find()
#
#     czao_elements = [page.czao_news,
#                      page.czao_about,
#                      page.czao_suppliers,
#                      page.czao_diller,
#                      page.czao_hotel,
#                      page.czao_shop,
#                      page.czao_corruption,
#                      page.czao_vacancy]
#
#     actions = ActionChains(driver)
#     for item in czao_elements:
#         page.wait_page_loaded(sleep_time=1.5)
#         actions.move_to_element(czao_main) \
#         .move_to_element(item.find()) \
#         .click() \
#         .perform()
#         page.wait_page_loaded(sleep_time=0.5)
#         page.go_back()
#     page.connect_with_us.click()
#     page.wait_page_loaded()
#     page.go_back()
#     page.belgee_link.click()
#     page.wait_page_loaded()
#     page.go_back()

#Функциональный тест 9 изображений

    while True:
        start_of_pictures = page.number_of_picture.get_text()
        if "1 / 9" in start_of_pictures:
            break
        else:
            page.main_arrow_left.click(wait_page=False)

    list_of_images = [page.image_1,
                      page.image_2,
                      page.image_3,
                      page.image_4,
                      page.image_5,
                      page.image_6,
                      page.image_7,
                      page.image_8,
                      page.image_9]

    for i in range(len(list_of_images)):
        print(list_of_images[i].get_attribute("src"))
        assert list_of_images[i].is_presented(), f'Изображение {i + 1} не отображено'

        # Кликаем на стрелку, только если это НЕ последняя картинка
        if i < len(list_of_images) - 1:
            page.main_arrow_right.click()







# #Функциональный тест нижних изображений
#     list_of_pictures = [page.picture1,
#                         page.picture2,
#                         page.picture3,
#                         page.picture4,
#                         page.picture5,
#                         page.picture6]
#
#     page.strelka.scroll_to_element()
#     for i in range(len(list_of_pictures) - 3):
#         for j in range(i, i + 3):
#             assert list_of_pictures[j].is_visible(), f'{j} не отображается'
#         page.strelka.click()
#         page.strelka.wait_to_be_clickable()



