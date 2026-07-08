import time
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.action_chains import ActionChains



class TestS50Page:

    def test_s50_functionality(self, model_page):
        page = model_page('S50')

        assert "S50" in page.driver.title, "Открыта страница не S50"
        print("Открыта страница S50")

        # 1. Открываем меню
        page.new_s50_button.find().click()
        page.wait_page_loaded()  # ← вместо time.sleep(1.5)
        print("Меню открыто")

        # 2. Переход к разделу "Комфорт"
        page.comfort_button.scroll_to_element_with_offset(offset=150)
        page.comfort_button.click()
        page.wait_page_loaded()
        print("Раздел 'Комфорт' загружен")

        # 3. Переход к разделу "Функциональность"
        page.functionality_button.scroll_to_element_with_offset(offset=150)
        page.functionality_button.click()
        page.wait_page_loaded()
        print("Раздел 'Функциональность' загружен")

        # 4. Переход к разделу "Прайс-лист"
        page.price_list_button.scroll_to_element_with_offset(offset=150)
        page.price_list_button.click()
        page.wait_page_loaded()
        print("Раздел 'Прайс-лист' загружен")

        # 5. Переход к разделу "Заявка"
        page.bid_button.scroll_to_element_with_offset(offset=150)
        page.bid_button.click()
        page.wait_page_loaded()
        print("Раздел 'Заявка' загружен")


    def test_exterier_and_interier(self, model_page):
        page = model_page('S50')
        page.exterier_button.scroll_to_element()
        page.wait_page_loaded()
        exterier_but = page.exterier_button.find()
        interier_but = page.interier_button.find()
        assert "_active" not in exterier_but.get_attribute('class')
        exterier_but.click()
        page.wait_page_loaded()
        assert "_active" in exterier_but.get_attribute('class')
        assert "_active" not in interier_but.get_attribute('class')
        interier_but.click()
        page.wait_page_loaded()
        assert "_active" in interier_but.get_attribute('class')
        exterier_but.click()
        page.wait_page_loaded()


    def test_colors_S50(self, model_page):
        page = model_page('S50')
        time.sleep(2)
        # Находим все цвета
        all_colors = page.all_colors.find()
        page.driver.execute_script("arguments[0].scrollIntoView({block: 'center'});", all_colors[0])
        page.wait_page_loaded()
        assert len(all_colors) >= 2, f"Найдено {len(all_colors)} цветов, нужно минимум 2"
        # Проверяем, что первый цвет активен
        assert "_active" in all_colors[0].get_attribute('class'), "Первый цвет не активен"
        # Переходим по цветам
        for i in range(1, len(all_colors)):
            prev_color = all_colors[i - 1]
            curr_color = all_colors[i]
            # Проверяем, что предыдущий активен (перед кликом)
            prev_class = prev_color.get_attribute('class')
            assert "_active" in prev_class, f"Цвет {i - 1} не активен перед кликом"
            # Кликаем на текущий цвет
            curr_color.click()
            time.sleep(0.5)
            # Проверяем, что текущий стал активным
            curr_class = curr_color.get_attribute('class')
            assert "_active" in curr_class, f"Цвет {i} не стал активным"
            # Проверяем, что предыдущий стал неактивным
            prev_class = prev_color.get_attribute('class')
            assert "_active" not in prev_class, f"Цвет {i - 1} все еще активен"


    def test_canvas_s50(self, model_page):
        page = model_page('S50')
        page.canvas_360.scroll_to_element()
        canvas = page.canvas_360.find()
        before = page.driver.execute_script(
            "return arguments[0].toDataURL();",
            canvas
        )
        ActionChains(page.driver) \
            .click_and_hold(canvas) \
            .move_by_offset(-300, 0) \
            .release() \
            .perform()

        page.wait_page_loaded()
        after = page.driver.execute_script(
            "return arguments[0].toDataURL();",
            canvas
        )

        assert before != after, "Автомобиль не вращается"

    def test_dealer_dropdown(self, model_page):
        page = model_page('S50')
        page.submit_image.scroll_to_element()

        button = page.dealer_dropdown.find()
        button.click()

        # Получаем свежий список
        dealer = page.dealer_fields.find()
        assert len(dealer) > 0, "Список дилеров пуст"

        for i in range(len(dealer)):
            if "--open" not in button.get_attribute('class'):
                button.click()

            dealer = page.dealer_fields.find()
            assert i < len(dealer), f"Индекс {i} вне диапазона (всего {len(dealer)})"
            assert dealer[i].text, f"Опция {i} пустая"

            if i < len(dealer):
                dealer[i].click()

    def test_equipment_dropdown(self, model_page):
        page = model_page('S50')
        page.submit_image.scroll_to_element()
        time.sleep(1)
        button_equipment = page.equipment_dropdown.find()
        button_equipment.click()
        time.sleep(2)
        equipment = page.equipment_fields.find()
        assert len(equipment) > 0, "Список дилеров пуст"

        for i in range(len(equipment)):
            if "--open" not in button_equipment.get_attribute('class'):
                button_equipment.click()

            equipment = page.equipment_fields.find()
            assert i < len(equipment), f"Индекс {i} вне диапазона (всего {len(equipment)})"
            assert equipment[i].text, f"Опция {i} пустая"

            if i < len(equipment):
                equipment[i].click()


    def test_agreement_dropdown(self, model_page):
        page = model_page('S50')
        page.submit_image.scroll_to_element()
        time.sleep(1)

        # Находим скрытый чекбокс
        checkbox = page.personal_information_field.find()

        # Кликаем через JavaScript (гарантированно работает)
        page.driver.execute_script("arguments[0].click();", checkbox)
        time.sleep(2)

        # Проверяем, что выбран
        assert checkbox.is_selected(), "Чекбокс не выбран"
        print("Чекбокс согласия выбран")

##Тестирования формы заявки на странице S50##

    def test_positive_submit_form(self, model_page):
        """
        TC-13: Успешная отправка формы с валидными данными
        """
        page = model_page('S50')
        page.submit_image.scroll_to_element()

        # Заполняем поля
        page.full_name_field.find().send_keys("Иванов Иван Иванович")
        page.phone_field.find().send_keys("291234567")
        page.email_field.find().send_keys("test@mail.ru")

        # Согласие
        consent = page.personal_information_field.find()
        if not consent.is_selected():
            page.driver.execute_script("arguments[0].click();", consent)

        # Отправка
        page.agree_button.find().click()

        # Ждём появления сообщения
        success = page.success_popup.wait_until_visible(timeout=5)

        assert success is not None, "Сообщение об успехе не появилось"
        assert "отправлен" in success.text.lower() or "свяжутся" in success.text.lower(), \
            f"Неожиданный текст: {success.text}"

        # Ждём исчезновения сообщения
        page.success_popup.wait_until_not_visible(timeout=5)

    def test_submit_empty_form(self, model_page):
        """
        TC-14: Отправка пустой формы
        """
        page = model_page('S50')
        page.submit_image.scroll_to_element()
        time.sleep(1)

        # Отправляем пустую форму
        page.agree_button.find().click()
        time.sleep(1)

        # Проверяем, что у каждого обязательного поля появился класс _error
        name_class = page.full_name_field.get_attribute('class')
        phone_class = page.phone_field.get_attribute('class')
        consent_class = page.personal_information_field.get_attribute('class')

        # Проверяем наличие ошибок
        assert "_error" in name_class, f"Нет ошибки для поля Ф.И.О. Класс: {name_class}"
        assert "_error" in phone_class, f"Нет ошибки для поля Телефон. Класс: {phone_class}"
        assert "_error" in consent_class, f"Нет ошибки для поля Согласие. Класс: {consent_class}"

        print("Все поля подсвечены ошибкой (класс _error присутствует)")

    def test_submit_without_name(self, model_page):
        """
        TC-15: Отправка формы без заполнения Ф.И.О
        """
        page = model_page('S50')
        page.submit_image.scroll_to_element()
        time.sleep(1)

        # Заполняем только телефон и email
        phone = page.phone_field.find()
        phone.clear()
        phone.send_keys("291234567")

        email = page.email_field.find()
        email.clear()
        email.send_keys("test@mail.ru")

        # Согласие
        consent = page.personal_information_field.find()
        if not consent.is_selected():
            page.driver.execute_script("arguments[0].click();", consent)

        # Отправляем
        submit = page.agree_button.find()
        submit.click()
        time.sleep(1)

        # Проверяем, что у поля Ф.И.О появился класс _error
        name_class = page.full_name_field.get_attribute('class')
        assert "_error" in name_class, f"Нет ошибки для поля Ф.И.О. Класс: {name_class}"

        # Проверяем, что у других полей нет ошибки
        phone_class = page.phone_field.get_attribute('class')
        consent_class = page.personal_information_field.get_attribute('class')

        assert "_error" not in phone_class, "Поле Телефон не должно иметь ошибку"
        assert "_error" not in consent_class, "Поле Согласие не должно иметь ошибку"

        print("Только поле Ф.И.О подсвечено ошибкой")

    def test_submit_without_phone(self, model_page):
        """
        TC-16: Отправка формы без заполнения телефона
        """
        page = model_page('S50')
        page.submit_image.scroll_to_element()
        time.sleep(1)

        # Заполняем только Ф.И.О и email
        name = page.full_name_field.find()
        name.clear()
        name.send_keys("Иванов Иван Иванович")

        email = page.email_field.find()
        email.clear()
        email.send_keys("test@mail.ru")

        # Согласие
        consent = page.personal_information_field.find()
        if not consent.is_selected():
            page.driver.execute_script("arguments[0].click();", consent)

        # Отправляем
        submit = page.agree_button.find()
        submit.click()
        time.sleep(1)

        # Проверяем, что у поля Телефон появился класс _error
        phone_class = page.phone_field.get_attribute('class')
        assert "_error" in phone_class, f"Нет ошибки для поля Телефон. Класс: {phone_class}"

        # Проверяем, что у других обязательных полей нет ошибки
        name_class = page.full_name_field.get_attribute('class')
        consent_class = page.personal_information_field.get_attribute('class')

        assert "_error" not in name_class, "Поле Ф.И.О не должно иметь ошибку"
        assert "_error" not in consent_class, "Поле Согласие не должно иметь ошибку"

        print("Только поле Телефон подсвечено ошибкой")

    def test_submit_invalid_phone(self, model_page):
        """
        TC-17: Отправка формы с невалидным номером телефона
        """
        page = model_page('S50')
        page.submit_image.scroll_to_element()
        time.sleep(1)

        # Заполняем все поля, но телефон – слишком короткий
        name = page.full_name_field.find()
        name.clear()
        name.send_keys("Иванов Иван Иванович")

        phone = page.phone_field.find()
        phone.clear()
        phone.send_keys("1")  # невалидный

        email = page.email_field.find()
        email.clear()
        email.send_keys("test@mail.ru")

        # Согласие
        consent = page.personal_information_field.find()
        if not consent.is_selected():
            page.driver.execute_script("arguments[0].click();", consent)

        # Отправляем
        submit = page.agree_button.find()
        submit.click()
        time.sleep(1)

        # Проверяем, что у поля Телефон появился класс _error
        phone_class = page.phone_field.get_attribute('class')
        assert "_error" in phone_class, f"Нет ошибки для поля Телефон. Класс: {phone_class}"

        # Проверяем, что у других обязательных полей нет ошибки
        name_class = page.full_name_field.get_attribute('class')
        consent_class = page.personal_information_field.get_attribute('class')

        assert "_error" not in name_class, "Поле Ф.И.О не должно иметь ошибку"
        assert "_error" not in consent_class, "Поле Согласие не должно иметь ошибку"

        print("Только поле Телефон подсвечено ошибкой")

    def test_submit_invalid_email(self, model_page):
        """
        TC-18: Отправка формы с невалидным email
        """
        page = model_page('S50')
        page.submit_image.scroll_to_element()
        time.sleep(1)

        # Заполняем все поля, но email – невалидный
        name = page.full_name_field.find()
        name.clear()
        name.send_keys("Иванов Иван Иванович")

        phone = page.phone_field.find()
        phone.clear()
        phone.send_keys("291234567")

        email = page.email_field.find()
        email.clear()
        email.send_keys("invalid-email")  # невалидный

        # Согласие
        consent = page.personal_information_field.find()
        if not consent.is_selected():
            page.driver.execute_script("arguments[0].click();", consent)

        # Отправляем
        submit = page.agree_button.find()
        submit.click()
        time.sleep(1)

        # Проверяем, что у поля Email появился класс _error (если поле обязательное)
        email_class = page.email_field.get_attribute('class')
        assert "_error" in email_class, f"Нет ошибки для поля Email. Класс: {email_class}"

        # Проверяем, что у других обязательных полей нет ошибки
        name_class = page.full_name_field.get_attribute('class')
        phone_class = page.phone_field.get_attribute('class')
        consent_class = page.personal_information_field.get_attribute('class')

        assert "_error" not in name_class, "Поле Ф.И.О не должно иметь ошибку"
        assert "_error" not in phone_class, "Поле Телефон не должно иметь ошибку"
        assert "_error" not in consent_class, "Поле Согласие не должно иметь ошибку"

        print("Только поле Email подсвечено ошибкой")

    def test_submit_without_consent(self, model_page):
        """
        TC-19: Отправка формы без согласия на обработку данных
        """
        page = model_page('S50')
        page.submit_image.scroll_to_element()
        time.sleep(1)

        # Заполняем все поля, но НЕ ставим галочку согласия
        name = page.full_name_field.find()
        name.clear()
        name.send_keys("Иванов Иван Иванович")

        phone = page.phone_field.find()
        phone.clear()
        phone.send_keys("291234567")

        email = page.email_field.find()
        email.clear()
        email.send_keys("test@mail.ru")

        # Пропускаем согласие

        # Отправляем
        submit = page.agree_button.find()
        submit.click()
        time.sleep(1)

        # Проверяем, что у поля Согласие появился класс _error
        consent_class = page.personal_information_field.get_attribute('class')
        assert "_error" in consent_class, f"Нет ошибки для поля Согласие. Класс: {consent_class}"

        # Проверяем, что у других обязательных полей нет ошибки
        name_class = page.full_name_field.get_attribute('class')
        phone_class = page.phone_field.get_attribute('class')

        assert "_error" not in name_class, "Поле Ф.И.О не должно иметь ошибку"
        assert "_error" not in phone_class, "Поле Телефон не должно иметь ошибку"

        print("Только поле Согласие подсвечено ошибкой")
