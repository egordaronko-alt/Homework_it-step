import os
import pytest
import time
import threading
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
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

    driver = webdriver.Chrome(options=chrome_options)
    driver.implicitly_wait(10)

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