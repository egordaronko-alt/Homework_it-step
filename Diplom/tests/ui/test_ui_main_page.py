import time
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.action_chains import ActionChains

class TestBasePage:

    #Test models in models
    def test_models(self, page):
        page.header_models.click()
        all_models = page.many_models.get_text()
        list_of_models = ['S50', 'X50', 'X50+', 'X70', 'X80']
        for i in range(len(list_of_models)):
            assert list_of_models[i] in all_models[i], f'модель {list_of_models[i]} отсутствует в dropdown menu'

    #Работоспособность ссылок перехода на модель автомобиля
    def test_links(self, page):
        page.header_models.click()
        model_links = [page.model_S50_link,
                       page.model_X50_link,
                       page.model_X50plus_link,
                       page.model_X70_link,
                       page.model_X80_link]
        switcher = page.models_switcher.get_attribute('class')
        for i in range(len(model_links)):
            time.sleep(3)
            if "_toggled" not in switcher:
                page.models_switcher.click()
            model_links[i].wait_to_be_clickable()
            model_links[i].click()
            page.go_back()
            page.wait_page_loaded()
        if "_toggled" in switcher:
            page.models_switcher.click()

    # Тест меню "Специальные предложения"
    def test_special(self, page):
        menu = page.special_deal_menu.find()

        special_deal_list = [page.special_deal_promo,
                             page.special_deal_leasing,
                             page.special_deal_kredit]

        actions = ActionChains(page.driver)
        for item in special_deal_list:
            page.wait_page_loaded(sleep_time=1)
            actions.move_to_element(menu) \
              .move_to_element(item.find()) \
              .click() \
              .perform()
            page.wait_page_loaded(sleep_time=0.5)
            page.go_back()

    #Тест меню "Владельцу"
    def test_owner(self, page):

        owner_list = [
            page.owner_user_manual,
            page.owner_hundred_belgee,
            page.owner_core_values,
            page.owner_expluatation_advice,
            page.owner_info_line,
            page.owner_road_help
        ]

        for element in owner_list:
            page.wait_page_loaded(sleep_time=0.5)

            # ВАЖНО: всегда заново берём элементы после возврата
            owner_menu = page.owner_main_link.find()

            ActionChains(page.driver) \
                .move_to_element(owner_menu) \
                .move_to_element(element.find()) \
                .click() \
                .perform()

            page.go_back()

    # Тест меню "СЗАО БЕЛДЖИ"
    def test_czao(self, page):

        czao_elements = [page.czao_news,
                         page.czao_about,
                         page.czao_suppliers,
                         page.czao_diller,
                         page.czao_hotel,
                         page.czao_shop,
                         page.czao_corruption,
                         page.czao_vacancy]

        actions = ActionChains(page.driver)
        for item in czao_elements:
            page.wait_page_loaded(sleep_time=1.5)
            czao_main = page.czao_main_link.find()
            actions.move_to_element(czao_main) \
            .move_to_element(item.find()) \
            .click() \
            .perform()
            page.wait_page_loaded(sleep_time=1)
            page.go_back()
        page.connect_with_us.click()
        page.wait_page_loaded()
        page.go_back()
        page.belgee_link.click()
        page.wait_page_loaded()
        page.go_back()

    # Функциональный тест 9 изображений
    def test_of_images(self, page):
        while True:
            start_of_pictures = page.number_of_picture.get_text()
            if "1 / 8" in start_of_pictures:
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
                          page.image_8]

        for i in range(len(list_of_images)):
            assert list_of_images[i].is_presented(), f'Изображение {i + 1} не отображено'

            # Кликаем на стрелку, только если это НЕ последняя картинка
            if i < len(list_of_images) - 1:
                page.main_arrow_right.click()

    # Функциональный тест нижних изображений
    def test_next_images(self, page):
        list_of_pictures = [page.picture1,
                            page.picture2,
                            page.picture3,
                            page.picture4,
                            page.picture5,
                            page.picture6]

        page.arrow.scroll_to_element()
        for i in range(len(list_of_pictures) - 3):
            for j in range(i, i + 3):
                assert list_of_pictures[j].is_visible(), f'{j} не отображается'
            page.arrow.click()
            page.arrow.wait_to_be_clickable()

    # Перемещение изображений на главной странице сайта
    def test_move_images(self, page):
        source = page.move_picture1.find()
        actions = ActionChains(page.driver)
        page.move_picture1.scroll_to_element()
        page.move_picture1.wait_to_be_clickable()
        actions.click_and_hold(source)
        for _ in range(10):
            actions.move_by_offset(-120, 0).pause(0.02)
        actions.release()
        actions.pause(2)
        actions.click_and_hold(source)
        for _ in range(12):
            actions.move_by_offset(100, 0).pause(0.02)
        actions.release()
        actions.perform()
        page.driver.set_window_size(1200, 1200)
        dots = page.owl_dots.find()
        for _ in range(3):
            for dot in dots:
                if "curent" not in dot.get_attribute("class"):
                    dot.click()

                    WebDriverWait(page.driver, 5).until(
                        lambda d: "curent" in dot.get_attribute("class")
                    )
                    break
            dots = page.owl_dots.find()

    # Проверка CSS элементов футера
    def test_creater_of_web_site(self, page):
        icon_element = page.site_developer.find()
        page.driver.execute_script("arguments[0].scrollIntoView({block: 'center'});", icon_element)
        time.sleep(2)

        initial_transform = icon_element.value_of_css_property('transform')
        initial_bg = icon_element.value_of_css_property('background-color')

        print(f"Начало: transform={initial_transform}, bg={initial_bg}")

        developers_link = page.developer.find()
        actions = ActionChains(page.driver)
        actions.move_to_element(developers_link).perform()

        changed = False
        for i in range(3):
            time.sleep(0.1)
            current_transform = icon_element.value_of_css_property('transform')
            current_bg = icon_element.value_of_css_property('background-color')

            print(f"  {i * 0.1:.1f}s: transform={current_transform}, bg={current_bg}")

            if current_transform != initial_transform or current_bg != initial_bg:
                changed = True
                print(f"Анимация обнаружена на {i * 0.1:.1f} секунде!")
                break

        assert changed, "Анимация не была обнаружена в течение 0.6 секунд"

        print("Анимация работает корректно и плавно!")


    def test_changing_of_backgrounds(self, page):
        social_icons = [
            ('Telegram', page.icon_of_telegram),
            ('Instagram', page.icon_of_instagram),
            ('Facebook', page.icon_of_youtube)]

        page.driver.execute_script("arguments[0].scrollIntoView({block: 'center'});", page.icon_of_telegram.find())
        time.sleep(1)
        for icon_name, social_icon in social_icons:
            icon = social_icon.find()
            icon_before = icon.value_of_css_property('background-color')

            actions = ActionChains(page.driver)
            actions.move_to_element(icon).perform()
            time.sleep(0.5)

            WebDriverWait(page.driver, 2).until(
                lambda driver: icon.value_of_css_property('background-color') != icon_before
            )
            icon_after = icon.value_of_css_property('background-color')
            assert icon_before != icon_after, f"background-color of {icon_name} didn't change"
            time.sleep(0.5)

#---------------------------------------------------------------------------------------------------------
