import time
import allure
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.action_chains import ActionChains


@allure.feature("UI Тесты")
@allure.story("Страница модели S50")
class TestS50Page:

    @allure.title("Проверка функциональности страницы S50")
    def test_s50_functionality(self, model_page):
        page = model_page('S50')

        with allure.step("Проверка заголовка страницы"):
            assert "S50" in page.driver.title, "Открыта страница не S50"

        with allure.step("Открытие меню"):
            page.new_s50_button.find().click()
            page.wait_page_loaded()

        with allure.step("Переход к разделу 'Комфорт'"):
            page.comfort_button.scroll_to_element_with_offset(offset=150)
            page.comfort_button.click()
            page.wait_page_loaded()

        with allure.step("Переход к разделу 'Функциональность'"):
            page.functionality_button.scroll_to_element_with_offset(offset=150)
            page.functionality_button.click()
            page.wait_page_loaded()

        with allure.step("Переход к разделу 'Прайс-лист'"):
            page.price_list_button.scroll_to_element_with_offset(offset=150)
            page.price_list_button.click()
            page.wait_page_loaded()

        with allure.step("Переход к разделу 'Заявка'"):
            page.bid_button.scroll_to_element_with_offset(offset=150)
            page.bid_button.click()
            page.wait_page_loaded()

    @allure.title("Проверка переключения экстерьера и интерьера")
    def test_exterier_and_interier(self, model_page):
        page = model_page('S50')
        page.exterier_button.scroll_to_element()
        page.wait_page_loaded()
        exterier_but = page.exterier_button.find()
        interier_but = page.interier_button.find()
        with allure.step("Проверка начального состояния экстерьера"):
            assert "_active" not in exterier_but.get_attribute('class')
        with allure.step("Клик по экстерьеру"):
            exterier_but.click()
            page.wait_page_loaded()
            assert "_active" in exterier_but.get_attribute('class')
            assert "_active" not in interier_but.get_attribute('class')
        with allure.step("Клик по интерьеру"):
            interier_but.click()
            page.wait_page_loaded()
            assert "_active" in interier_but.get_attribute('class')
        with allure.step("Возврат к экстерьеру"):
            exterier_but.click()
            page.wait_page_loaded()

    @allure.title("Проверка выбора цветов S50")
    def test_colors_S50(self, model_page):
        page = model_page('S50')
        time.sleep(2)
        with allure.step("Нахождение всех цветов"):
            all_colors = page.all_colors.find()
            page.driver.execute_script("arguments[0].scrollIntoView({block: 'center'});", all_colors[0])
            page.wait_page_loaded()
            assert len(all_colors) >= 2, f"Найдено {len(all_colors)} цветов, нужно минимум 2"
        with allure.step("Проверка активности первого цвета"):
            assert "_active" in all_colors[0].get_attribute('class'), "Первый цвет не активен"
        with allure.step("Переход по цветам"):
            for i in range(1, len(all_colors)):
                prev_color = all_colors[i - 1]
                curr_color = all_colors[i]
                prev_class = prev_color.get_attribute('class')
                assert "_active" in prev_class, f"Цвет {i - 1} не активен перед кликом"
                curr_color.click()
                time.sleep(0.5)
                curr_class = curr_color.get_attribute('class')
                assert "_active" in curr_class, f"Цвет {i} не стал активным"
                prev_class = prev_color.get_attribute('class')
                assert "_active" not in prev_class, f"Цвет {i - 1} все еще активен"

    @allure.title("Проверка вращения 3D модели S50")
    def test_canvas_s50(self, model_page):
        page = model_page('S50')
        page.canvas_360.scroll_to_element()
        canvas = page.canvas_360.find()
        with allure.step("Получение начального изображения"):
            before = page.driver.execute_script(
                "return arguments[0].toDataURL();",
                canvas
            )
        with allure.step("Перетаскивание canvas для вращения"):
            ActionChains(page.driver) \
                .click_and_hold(canvas) \
                .move_by_offset(-300, 0) \
                .release() \
                .perform()
            page.wait_page_loaded()
        with allure.step("Проверка изменения изображения"):
            after = page.driver.execute_script(
                "return arguments[0].toDataURL();",
                canvas
            )
            assert before != after, "Автомобиль не вращается"

    @allure.title("Проверка выпадающего списка дилеров")
    def test_dealer_dropdown(self, model_page):
        page = model_page('S50')
        page.submit_image.scroll_to_element()
        with allure.step("Открытие списка дилеров"):
            button = page.dealer_dropdown.find()
            button.click()
        with allure.step("Проверка наличия дилеров"):
            dealer = page.dealer_fields.find()
            assert len(dealer) > 0, "Список дилеров пуст"
        with allure.step("Перебор дилеров"):
            for i in range(len(dealer)):
                if "--open" not in button.get_attribute('class'):
                    button.click()
                dealer = page.dealer_fields.find()
                assert i < len(dealer), f"Индекс {i} вне диапазона (всего {len(dealer)})"
                assert dealer[i].text, f"Опция {i} пустая"
                if i < len(dealer):
                    dealer[i].click()

    @allure.title("Проверка выпадающего списка комплектаций")
    def test_equipment_dropdown(self, model_page):
        page = model_page('S50')
        page.submit_image.scroll_to_element()
        time.sleep(1)
        with allure.step("Открытие списка комплектаций"):
            button_equipment = page.equipment_dropdown.find()
            button_equipment.click()
            time.sleep(2)
        with allure.step("Проверка наличия комплектаций"):
            equipment = page.equipment_fields.find()
            assert len(equipment) > 0, "Список дилеров пуст"
        with allure.step("Перебор комплектаций"):
            for i in range(len(equipment)):
                if "--open" not in button_equipment.get_attribute('class'):
                    button_equipment.click()
                equipment = page.equipment_fields.find()
                assert i < len(equipment), f"Индекс {i} вне диапазона (всего {len(equipment)})"
                assert equipment[i].text, f"Опция {i} пустая"
                if i < len(equipment):
                    equipment[i].click()

    @allure.title("Проверка чекбокса согласия")
    def test_agreement_dropdown(self, model_page):
        page = model_page('S50')
        page.submit_image.scroll_to_element()
        time.sleep(1)
        with allure.step("Клик по чекбоксу согласия"):
            checkbox = page.personal_information_field.find()
            page.driver.execute_script("arguments[0].click();", checkbox)
            time.sleep(2)
        with allure.step("Проверка состояния чекбокса"):
            assert checkbox.is_selected(), "Чекбокс не выбран"

    @allure.title("TC-13: Успешная отправка формы с валидными данными")
    def test_positive_submit_form(self, model_page):
        page = model_page('S50')
        page.submit_image.scroll_to_element()
        with allure.step("Заполнение полей формы"):
            page.full_name_field.find().send_keys("Иванов Иван Иванович")
            page.phone_field.find().send_keys("291234567")
            page.email_field.find().send_keys("test@mail.ru")
        with allure.step("Установка согласия"):
            consent = page.personal_information_field.find()
            if not consent.is_selected():
                page.driver.execute_script("arguments[0].click();", consent)
        with allure.step("Отправка формы"):
            page.agree_button.find().click()
        with allure.step("Проверка сообщения об успехе"):
            success = page.success_popup.wait_until_visible(timeout=5)
            assert success is not None, "Сообщение об успехе не появилось"
            assert "отправлен" in success.text.lower() or "свяжутся" in success.text.lower(), \
                f"Неожиданный текст: {success.text}"
        with allure.step("Ожидание исчезновения сообщения"):
            page.success_popup.wait_until_not_visible(timeout=5)

    @allure.title("TC-14: Отправка пустой формы")
    def test_submit_empty_form(self, model_page):
        page = model_page('S50')
        page.submit_image.scroll_to_element()
        time.sleep(1)
        with allure.step("Отправка пустой формы"):
            page.agree_button.find().click()
            time.sleep(1)
        with allure.step("Проверка ошибок на всех полях"):
            name_class = page.full_name_field.get_attribute('class')
            phone_class = page.phone_field.get_attribute('class')
            consent_class = page.personal_information_field.get_attribute('class')
            assert "_error" in name_class, f"Нет ошибки для поля Ф.И.О. Класс: {name_class}"
            assert "_error" in phone_class, f"Нет ошибки для поля Телефон. Класс: {phone_class}"
            assert "_error" in consent_class, f"Нет ошибки для поля Согласие. Класс: {consent_class}"

    @allure.title("TC-15: Отправка формы без заполнения Ф.И.О")
    def test_submit_without_name(self, model_page):
        page = model_page('S50')
        page.submit_image.scroll_to_element()
        time.sleep(1)
        with allure.step("Заполнение только телефона и email"):
            phone = page.phone_field.find()
            phone.clear()
            phone.send_keys("291234567")
            email = page.email_field.find()
            email.clear()
            email.send_keys("test@mail.ru")
        with allure.step("Установка согласия"):
            consent = page.personal_information_field.find()
            if not consent.is_selected():
                page.driver.execute_script("arguments[0].click();", consent)
        with allure.step("Отправка формы"):
            submit = page.agree_button.find()
            submit.click()
            time.sleep(1)
        with allure.step("Проверка ошибки только для Ф.И.О"):
            name_class = page.full_name_field.get_attribute('class')
            assert "_error" in name_class, f"Нет ошибки для поля Ф.И.О. Класс: {name_class}"
            phone_class = page.phone_field.get_attribute('class')
            consent_class = page.personal_information_field.get_attribute('class')
            assert "_error" not in phone_class, "Поле Телефон не должно иметь ошибку"
            assert "_error" not in consent_class, "Поле Согласие не должно иметь ошибку"

    @allure.title("TC-16: Отправка формы без заполнения телефона")
    def test_submit_without_phone(self, model_page):
        page = model_page('S50')
        page.submit_image.scroll_to_element()
        time.sleep(1)
        with allure.step("Заполнение только Ф.И.О и email"):
            name = page.full_name_field.find()
            name.clear()
            name.send_keys("Иванов Иван Иванович")
            email = page.email_field.find()
            email.clear()
            email.send_keys("test@mail.ru")
        with allure.step("Установка согласия"):
            consent = page.personal_information_field.find()
            if not consent.is_selected():
                page.driver.execute_script("arguments[0].click();", consent)
        with allure.step("Отправка формы"):
            submit = page.agree_button.find()
            submit.click()
            time.sleep(1)
        with allure.step("Проверка ошибки только для Телефона"):
            phone_class = page.phone_field.get_attribute('class')
            assert "_error" in phone_class, f"Нет ошибки для поля Телефон. Класс: {phone_class}"
            name_class = page.full_name_field.get_attribute('class')
            consent_class = page.personal_information_field.get_attribute('class')
            assert "_error" not in name_class, "Поле Ф.И.О не должно иметь ошибку"
            assert "_error" not in consent_class, "Поле Согласие не должно иметь ошибку"

    @allure.title("TC-17: Отправка формы с невалидным номером телефона")
    def test_submit_invalid_phone(self, model_page):
        page = model_page('S50')
        page.submit_image.scroll_to_element()
        time.sleep(1)
        with allure.step("Заполнение полей с невалидным телефоном"):
            name = page.full_name_field.find()
            name.clear()
            name.send_keys("Иванов Иван Иванович")
            phone = page.phone_field.find()
            phone.clear()
            phone.send_keys("1")
            email = page.email_field.find()
            email.clear()
            email.send_keys("test@mail.ru")
        with allure.step("Установка согласия"):
            consent = page.personal_information_field.find()
            if not consent.is_selected():
                page.driver.execute_script("arguments[0].click();", consent)
        with allure.step("Отправка формы"):
            submit = page.agree_button.find()
            submit.click()
            time.sleep(1)
        with allure.step("Проверка ошибки только для Телефона"):
            phone_class = page.phone_field.get_attribute('class')
            assert "_error" in phone_class, f"Нет ошибки для поля Телефон. Класс: {phone_class}"
            name_class = page.full_name_field.get_attribute('class')
            consent_class = page.personal_information_field.get_attribute('class')
            assert "_error" not in name_class, "Поле Ф.И.О не должно иметь ошибку"
            assert "_error" not in consent_class, "Поле Согласие не должно иметь ошибку"

    @allure.title("TC-18: Отправка формы с невалидным email")
    def test_submit_invalid_email(self, model_page):
        page = model_page('S50')
        page.submit_image.scroll_to_element()
        time.sleep(1)
        with allure.step("Заполнение полей с невалидным email"):
            name = page.full_name_field.find()
            name.clear()
            name.send_keys("Иванов Иван Иванович")
            phone = page.phone_field.find()
            phone.clear()
            phone.send_keys("291234567")
            email = page.email_field.find()
            email.clear()
            email.send_keys("invalid-email")
        with allure.step("Установка согласия"):
            consent = page.personal_information_field.find()
            if not consent.is_selected():
                page.driver.execute_script("arguments[0].click();", consent)
        with allure.step("Отправка формы"):
            submit = page.agree_button.find()
            submit.click()
            time.sleep(1)
        with allure.step("Проверка ошибки только для Email"):
            email_class = page.email_field.get_attribute('class')
            assert "_error" in email_class, f"Нет ошибки для поля Email. Класс: {email_class}"
            name_class = page.full_name_field.get_attribute('class')
            phone_class = page.phone_field.get_attribute('class')
            consent_class = page.personal_information_field.get_attribute('class')
            assert "_error" not in name_class, "Поле Ф.И.О не должно иметь ошибку"
            assert "_error" not in phone_class, "Поле Телефон не должно иметь ошибку"
            assert "_error" not in consent_class, "Поле Согласие не должно иметь ошибку"

    @allure.title("TC-19: Отправка формы без согласия на обработку данных")
    def test_submit_without_consent(self, model_page):
        page = model_page('S50')
        page.submit_image.scroll_to_element()
        time.sleep(1)
        with allure.step("Заполнение полей без согласия"):
            name = page.full_name_field.find()
            name.clear()
            name.send_keys("Иванов Иван Иванович")
            phone = page.phone_field.find()
            phone.clear()
            phone.send_keys("291234567")
            email = page.email_field.find()
            email.clear()
            email.send_keys("test@mail.ru")
        with allure.step("Отправка формы"):
            submit = page.agree_button.find()
            submit.click()
            time.sleep(1)
        with allure.step("Проверка ошибки только для Согласия"):
            consent_class = page.personal_information_field.get_attribute('class')
            assert "_error" in consent_class, f"Нет ошибки для поля Согласие. Класс: {consent_class}"
            name_class = page.full_name_field.get_attribute('class')
            phone_class = page.phone_field.get_attribute('class')
            assert "_error" not in name_class, "Поле Ф.И.О не должно иметь ошибку"
            assert "_error" not in phone_class, "Поле Телефон не должно иметь ошибку"
