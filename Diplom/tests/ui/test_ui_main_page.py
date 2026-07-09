import time
import allure
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.action_chains import ActionChains


@allure.feature("UI Тесты")
@allure.story("Главная страница belgee.by")
class TestBasePage:

    @allure.title("Проверка моделей в выпадающем меню")
    def test_models(self, page):
        with allure.step("Открыть меню моделей"):
            page.header_models.click()
        with allure.step("Получить список моделей"):
            all_models = page.many_models.get_text()
        list_of_models = ['S50', 'X50', 'X50+', 'X70', 'X80']
        for i in range(len(list_of_models)):
            with allure.step(f"Проверка наличия модели {list_of_models[i]}"):
                assert list_of_models[i] in all_models[i], f'модель {list_of_models[i]} отсутствует в dropdown menu'

    @allure.title("Проверка ссылок перехода на модель автомобиля")
    def test_links(self, page):
        with allure.step("Открыть меню моделей"):
            page.header_models.click()
        model_links = [page.model_S50_link,
                       page.model_X50_link,
                       page.model_X50plus_link,
                       page.model_X70_link,
                       page.model_X80_link]
        switcher = page.models_switcher.get_attribute('class')
        for i in range(len(model_links)):
            time.sleep(3)
            with allure.step(f"Переход по ссылке модели {i + 1}"):
                if "_toggled" not in switcher:
                    page.models_switcher.click()
                model_links[i].wait_to_be_clickable()
                model_links[i].click()
                page.go_back()
                page.wait_page_loaded()
        if "_toggled" in switcher:
            page.models_switcher.click()

    @allure.title("Тест меню 'Специальные предложения'")
    def test_special(self, page):
        menu = page.special_deal_menu.find()
        special_deal_list = [page.special_deal_promo,
                             page.special_deal_leasing,
                             page.special_deal_kredit]
        actions = ActionChains(page.driver)
        for item in special_deal_list:
            with allure.step("Переход в раздел специальных предложений"):
                page.wait_page_loaded(sleep_time=1)
                actions.move_to_element(menu) \
                  .move_to_element(item.find()) \
                  .click() \
                  .perform()
                page.wait_page_loaded(sleep_time=0.5)
                page.go_back()

    @allure.title("Тест меню 'Владельцу'")
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
            with allure.step("Переход в раздел 'Владельцу'"):
                page.wait_page_loaded(sleep_time=0.5)
                owner_menu = page.owner_main_link.find()
                ActionChains(page.driver) \
                    .move_to_element(owner_menu) \
                    .move_to_element(element.find()) \
                    .click() \
                    .perform()
                page.go_back()

    @allure.title("Тест меню 'СЗАО БЕЛДЖИ'")
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
            with allure.step("Переход в раздел 'СЗАО БЕЛДЖИ'"):
                page.wait_page_loaded(sleep_time=1.5)
                czao_main = page.czao_main_link.find()
                actions.move_to_element(czao_main) \
                .move_to_element(item.find()) \
                .click() \
                .perform()
                page.wait_page_loaded(sleep_time=1)
                page.go_back()
        with allure.step("Проверка ссылки 'Свяжитесь с нами'"):
            page.connect_with_us.click()
            page.wait_page_loaded()
            page.go_back()
        with allure.step("Проверка ссылки BELGEE"):
            page.belgee_link.click()
            page.wait_page_loaded()
            page.go_back()

    @allure.title("Функциональный тест 9 изображений")
    def test_of_images(self, page):
        with allure.step("Переход к первому изображению"):
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
            with allure.step(f"Проверка изображения {i + 1}"):
                assert list_of_images[i].is_presented(), f'Изображение {i + 1} не отображено'
                if i < len(list_of_images) - 1:
                    page.main_arrow_right.click()

    @allure.title("Функциональный тест нижних изображений")
    def test_next_images(self, page):
        list_of_pictures = [page.picture1,
                            page.picture2,
                            page.picture3,
                            page.picture4,
                            page.picture5,
                            page.picture6]
        page.arrow.scroll_to_element()
        for i in range(len(list_of_pictures) - 3):
            with allure.step(f"Проверка видимости изображений {i + 1}-{i + 3}"):
                for j in range(i, i + 3):
                    assert list_of_pictures[j].is_visible(), f'{j} не отображается'
                page.arrow.click()
                page.arrow.wait_to_be_clickable()

    @allure.title("Перемещение изображений на главной странице")
    def test_move_images(self, page):
        source = page.move_picture1.find()
        actions = ActionChains(page.driver)
        page.move_picture1.scroll_to_element()
        page.move_picture1.wait_to_be_clickable()
        with allure.step("Перетаскивание изображения влево"):
            actions.click_and_hold(source)
            for _ in range(10):
                actions.move_by_offset(-120, 0).pause(0.02)
            actions.release()
            actions.pause(2)
        with allure.step("Перетаскивание изображения вправо"):
            actions.click_and_hold(source)
            for _ in range(12):
                actions.move_by_offset(100, 0).pause(0.02)
            actions.release()
            actions.perform()
        with allure.step("Проверка dots навигации"):
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

    @allure.title("Проверка CSS анимации элемента разработчика")
    def test_creater_of_web_site(self, page):
        icon_element = page.site_developer.find()
        page.driver.execute_script("arguments[0].scrollIntoView({block: 'center'});", icon_element)
        time.sleep(2)
        with allure.step("Получение начальных CSS значений"):
            initial_transform = icon_element.value_of_css_property('transform')
            initial_bg = icon_element.value_of_css_property('background-color')
        with allure.step("Наведение на ссылку разработчика"):
            developers_link = page.developer.find()
            actions = ActionChains(page.driver)
            actions.move_to_element(developers_link).perform()
        with allure.step("Проверка анимации"):
            changed = False
            for i in range(3):
                time.sleep(0.1)
                current_transform = icon_element.value_of_css_property('transform')
                current_bg = icon_element.value_of_css_property('background-color')
                if current_transform != initial_transform or current_bg != initial_bg:
                    changed = True
                    break
            assert changed, "Анимация не была обнаружена в течение 0.6 секунд"

    @allure.title("Проверка смены фона социальных иконок")
    def test_changing_of_backgrounds(self, page):
        social_icons = [
            ('Telegram', page.icon_of_telegram),
            ('Instagram', page.icon_of_instagram),
            ('Facebook', page.icon_of_youtube)]
        page.driver.execute_script("arguments[0].scrollIntoView({block: 'center'});", page.icon_of_telegram.find())
        time.sleep(1)
        for icon_name, social_icon in social_icons:
            with allure.step(f"Проверка иконки {icon_name}"):
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
