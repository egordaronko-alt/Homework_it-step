import os
import pytest
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from Diplom.locators.main_locators import MainPage
from selenium.common.exceptions import TimeoutException


@pytest.fixture
def driver():
    chrome_options = Options()
    chrome_options.add_argument('--start-maximized')
    if os.getenv('SELENIUM_HEADLESS'):
        chrome_options.add_argument('--headless')
        chrome_options.add_argument('--no-sandbox')
        chrome_options.add_argument('--disable-dev-shm-usage')

    # ← ИЗМЕНЕНО: используем WebDriver Manager
    service = Service(ChromeDriverManager().install())
    driver = webdriver.Chrome(service=service, options=chrome_options)

    yield driver
    driver.quit()

@pytest.fixture
def page(driver):
    page = MainPage(driver)

    page.accept_cookie.click()

    try:
        page.pop_window.wait_to_be_clickable().click()
    except TimeoutException:
        page.execute_script("""
            var el = document.querySelector('.close._js-pop-close');
            if (el) el.click();
        """)

    return page


@pytest.fixture
def model_page(driver):
    def _create_model_page(model_name):
        url = f"https://belgee.by/models/{model_name}"
        page = MainPage(driver, url)

        page.accept_cookie.click()

        try:
            page.pop_window.wait_to_be_clickable().click()
        except TimeoutException:
            page.execute_script("""
                var el = document.querySelector('.close._js-pop-close');
                if (el) el.click();
            """)

        return page

    return _create_model_page