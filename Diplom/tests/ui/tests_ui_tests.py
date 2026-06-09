# import time
#
# from selenium.common.exceptions import TimeoutException
# from selenium import webdriver
# from webdriver_manager.chrome import ChromeDriverManager
# from selenium.webdriver.chrome.service import Service
# from selenium.webdriver.chrome.options import Options
# from selenium.webdriver.common.by import By
# import pickle
# from selenium.webdriver.common.keys import Keys
# from selenium.webdriver.support.ui import WebDriverWait
# from selenium.webdriver.support import expected_conditions as EC
# from selenium.webdriver.common.action_chains import ActionChains
#
# options = Options()
# options.add_argument('--disable-blink-features=AutomationControlled')
# options.add_argument('--window-size=1920,1080')
# options.add_argument("--incognito")
#
#
# service = Service(ChromeDriverManager().install())
# driver = webdriver.Chrome(service=service, options=options)
# wait = WebDriverWait(driver, 10, poll_frequency=1)
# action = ActionChains
#
# driver.get("https://belgee.by/")
# driver.execute_script("""document.querySelector("[class='s-popup']").style.display = "none";""")
#
# COOKIES = ("xpath", "/html/body/section[4]/div[7]/div/div/div[2]/div/a")
# MODELS = ("xpath", "//span[text()='Модели']")
# FIRST_MODEL = ("xpath", "//img[@title='S50']")
# from selenium.webdriver.common.by import By
#
# all_models = [
#     ("xpath", "//img[contains(@src,'w300_h200_dzylmn18v0ls4xg1bgep.png')]"),
#     ("xpath", "//img[contains(@src,'w300_h200_uogzrfwzjdl9svcpzj57.png')]"),
#     ("xpath", "//img[contains(@src,'w300_h200_44a9oqstp6l9jkoe7kui.png')]"),
#     ("xpath", "//img[contains(@src,'w300_h200_m9xovvg3ffjp3bh9xmjl.png')]"),
#     ("xpath", "//img[contains(@src,'w300_h200_f5y8il8onsgrnqplsmeg.png')]")
#     ]
#
# try:
#     cookies = wait.until(EC.element_to_be_clickable(COOKIES))
#     cookies.click()
# except TimeoutException:
#     pass
#
# for model in all_models:
#     wait.until(EC.element_to_be_clickable(MODELS)).click()
#     wait.until(EC.element_to_be_clickable(driver.find_element(*model))).click()
#     time.sleep(3)
#     driver.back()


##############################
import time

from Diplom.locators.main_locators import MainPage


def test_belgee(driver):
    page = MainPage(driver)
    print(page.btn_catalog.get_text())
