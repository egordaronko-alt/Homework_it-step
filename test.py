# import time
# from selenium import webdriver
# from selenium.webdriver.common.by import By
# from selenium.webdriver.common.keys import Keys
#
# driver = webdriver.Chrome()
# driver.get('https://demoqa.com/text-box')
# time.sleep(2)
#
# full_name = driver.find_element(By.XPATH, '//input[@id="userName"]')
# if full_name.get_attribute('value') == "":
#     full_name.send_keys('Full_Name')
# assert full_name.get_attribute('value') == 'Full_Name', "поле Full_name некорректное"
# time.sleep(2)
#
# name_example = driver.find_element(By.XPATH, '//input[@id="userEmail"]')
#
# if name_example.get_attribute('value') == "":
#     name_example.send_keys('name_example@mail.com')
# assert name_example.get_attribute('value') == 'name_example@mail.com', "nameexample error"
# time.sleep(2)
#
# curr_adress = driver.find_element(By.XPATH, '//textarea[@id="currentAddress"]')
#
# if curr_adress.get_attribute('value') == "":
#     curr_adress.send_keys('current_address')
# assert curr_adress.get_attribute('value') == 'current_address', "curr_adress error"
# time.sleep(2)
#
#
# permanentAddress = driver.find_element(By.XPATH, '//textarea[@id="permanentAddress"]')
#
# if permanentAddress.get_attribute('value') == "":
#     permanentAddress.send_keys('permanentAddress')
# assert permanentAddress.get_attribute('value') == 'permanentAddress', "permanentAddress error"
# time.sleep(2)
#
# driver.find_element(By.XPATH, '//button[@id="submit"]').click()
# time.sleep(2)
# driver.quit()
from Diplom.locators.main_locators import MainPage

# import time
# from selenium import webdriver
# from selenium.webdriver.common.by import By
# from selenium.webdriver.common.keys import Keys
#
# driver = webdriver.Chrome()
# driver.get('https://the-internet.herokuapp.com/status_codes')
# time.sleep(2)
#
# elements = driver.find_elements(By.XPATH, "//ul//li//a")
# for i in range(len(elements)):
#     elements[i].click()
#     time.sleep(4)
#     driver.back()
#     time.sleep(4)
#
# driver.quit()

# import os
# import time
# from selenium import webdriver
# from webdriver_manager.chrome import ChromeDriverManager
# from selenium.webdriver.chrome.service import Service
# from selenium.webdriver.common.by import By
# from selenium.webdriver.common.keys import Keys
# import os
#
# options = webdriver.ChromeOptions()
# download_dir = r'C:\Users\user\PycharmProjects\qa2025\egor_daronko\downloadsss'
# preferences = {
#     "download.default_directory": download_dir,
#     "safebrowsing.enabled": False
# }
# options.add_experimental_option("prefs", preferences)
#
# service = Service(ChromeDriverManager().install())
# driver = webdriver.Chrome(service=service, options=options)
#
# driver.get("https://demoqa.com/upload-download")
# time.sleep(3)
# upload_file = driver.find_element(By.XPATH, "//input[@id='uploadFile']")
# upload_file.send_keys(f"{os.getcwd()}/downloadsss/happy-catto-cats.gif")
# time.sleep(7)
# driver.get("http://the-internet.herokuapp.com/download")
#
# upload_files = driver.find_elements(By.XPATH, "//div[@class='example']/a")
# for file in upload_files:
#     file.click()
#     time.sleep(0.1)
# time.sleep(3)


# import os
# import time
# from selenium import webdriver
# from webdriver_manager.chrome import ChromeDriverManager
# from selenium.webdriver.chrome.service import Service
# from selenium.webdriver.common.by import By
# from selenium.webdriver.common.keys import Keys
# from selenium.webdriver.support.ui import WebDriverWait
# from selenium.webdriver.support import expected_conditions as EC
#
# service = Service(ChromeDriverManager().install())
# driver = webdriver.Chrome(service=service)
# wait = WebDriverWait(driver, 30, poll_frequency=1)
#
# driver.get("https://omayo.blogspot.com/")
#
# sec_25_button = ("xpath", "//div[@id='deletesuccess']")
# sec_10_button = ("xpath", "//div[@id='delayedText']")
# enable_button = ("xpath", "//input[@id='timerButton']")
# my_button = ("xpath", "//button[@id='myBtn']")
# try_it = ("xpath", "//button[@onclick='setTimeout(myFunctionABC,3000)']")
#
# wait.until(EC.invisibility_of_element(sec_25_button))
# wait.until(EC.visibility_of_element_located(sec_10_button))
# wait.until(EC.element_to_be_clickable(enable_button))
# driver.find_element(*try_it).click()
# wait.until_not(EC.element_attribute_to_include(my_button, 'disabled'))
# wait.until_not(EC.element_to_be_clickable(my_button))
# time.sleep(5)

# import os
# import time
# from selenium import webdriver
# from webdriver_manager.chrome import ChromeDriverManager
# from selenium.webdriver.chrome.service import Service
# from selenium.webdriver.chrome.options import Options
# from selenium.webdriver.common.by import By
# from selenium.webdriver.common.keys import Keys
# from selenium.webdriver.support.ui import WebDriverWait
# from selenium.webdriver.support import expected_conditions as EC
#
# options = Options()
# options.add_argument('--disable-blink-features=AutomationControlled')
# options.add_argument('--window-size=1920,1080')
# options.add_argument('--user-agent=Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/148.0.0.0 Safari/537.36 Edg/148.0.0.0')
#
# service = Service(ChromeDriverManager().install())
# driver = webdriver.Chrome(service=service, options=options)
# wait = WebDriverWait(driver, 10, poll_frequency=1)
#
# driver.get("https://www.tiktok.com/")
# time.sleep(20)
# # driver.save_screenshot('screen.png')

# import os
# import time
# from selenium import webdriver
# from webdriver_manager.chrome import ChromeDriverManager
# from selenium.webdriver.chrome.service import Service
# from selenium.webdriver.chrome.options import Options
# from selenium.webdriver.common.by import By
# from selenium.webdriver.common.keys import Keys
# from selenium.webdriver.support.ui import WebDriverWait
# from selenium.webdriver.support import expected_conditions as EC
#
# service = Service(ChromeDriverManager().install())
# driver = webdriver.Chrome(service=service)
# wait = WebDriverWait(driver, 10, poll_frequency=1)
#
# driver.get("https://demoqa.com/alerts")
# button_1 = ("xpath", "//button[@id='promtButton']")
# wait.until(EC.element_to_be_clickable(button_1)).click()
# alert = wait.until(EC.alert_is_present())
# driver.switch_to.alert
# time.sleep(3)
# alert.send_keys('Keys')
# alert.accept()
# time.sleep(3)


# import os
# import time
# from selenium import webdriver
# from webdriver_manager.chrome import ChromeDriverManager
# from selenium.webdriver.chrome.service import Service
# from selenium.webdriver.chrome.options import Options
# from selenium.webdriver.common.by import By
# import pickle
# from selenium.webdriver.common.keys import Keys
# from selenium.webdriver.support.ui import WebDriverWait
# from selenium.webdriver.support import expected_conditions as EC

# service = Service(ChromeDriverManager().install())
# driver = webdriver.Chrome(service=service)
# wait = WebDriverWait(driver, 10, poll_frequency=1)

# driver.get("https://www.freeconferencecall.com/en/us/login")

# driver.add_cookie({
#     'name': 'test',
#     'value': 'testirov',
# })
#
# driver.refresh()
#
# find_cookie = driver.get_cookie('test')
# print(find_cookie)

# before = driver.get_cookie('country_code')
# print(before)
# driver.delete_cookie('country_code')
# assert driver.get_cookie('country_code') is None, 'кука не удалена'

# driver.get("https://www.wildberries.by/")


# element = ("xpath", "//input[@data-testid='searchInput']")
# input_field = wait.until(EC.element_to_be_clickable(element))
# input_field.send_keys("297269658")
# time.sleep(2)
# input_field.send_keys(Keys.ENTER)
# wait.until(EC.element_to_be_clickable(("xpath", "//button[@aria-label='Добавить в корзину']"))).click()
# time.sleep(5)

# pickle.dump(driver.get_cookies(), open(os.getcwd() + "/cookies/cookies.pkl", "wb"))


# driver.delete_all_cookies()
# cookies = pickle.load(open(os.getcwd()+"/cookies/cookies.pkl", "rb"))
# for cookie in cookies:
#     driver.add_cookie(cookie)
# time.sleep(5)
# driver.refresh()
# time.sleep(5)

# import os
# import time
# from selenium import webdriver
# from webdriver_manager.chrome import ChromeDriverManager
# from selenium.webdriver.chrome.service import Service
# from selenium.webdriver.chrome.options import Options
# from selenium.webdriver.common.by import By
# import pickle
# from selenium.webdriver.common.keys import Keys
# from selenium.webdriver.support.ui import WebDriverWait
# from selenium.webdriver.support import expected_conditions as EC
#
# service = Service(ChromeDriverManager().install())
# driver = webdriver.Chrome(service=service)
# wait = WebDriverWait(driver, 10, poll_frequency=0.1)
#
# driver.get("https://demoqa.com/selectable")
#
#
# Cras_justo_odio = ("xpath", "//li[contains(@class, 'mt-2') and text()='Cras justo odio']")
# Morbi_leo_risus = ("xpath", "//li[contains(@class, 'mt-2') and text()='Morbi leo risus']")
# LIST = ("xpath", "//button[@data-rr-ui-event-key='list']")
# GRID = ("xpath", "//button[@data-rr-ui-event-key='grid']")
# ONE = ("xpath", "//li[contains(@class, 'list-group') and text()='One']")
# SIX = ("xpath", "//li[contains(@class, 'list-group') and text()='Six']")
#
# time.sleep(3)
# before = driver.find_element(*Cras_justo_odio).get_attribute("class")
# print("active" in before)
# driver.find_element(*Cras_justo_odio).click()
# after = driver.find_element(*Cras_justo_odio).get_attribute("class")
# print("active" in after)
# driver.find_element(*Morbi_leo_risus).click()
# print("active" in driver.find_element(*Morbi_leo_risus).get_attribute("class"))
# time.sleep(3)
# driver.find_element(*GRID).click()
# driver.find_element(*ONE).click()
# driver.find_element(*SIX).click()
# print("active" in driver.find_element(*ONE).get_attribute("class"))
# assert "active" in driver.find_element(*SIX).get_attribute("class")
# print("active" in driver.find_element(*SIX).get_attribute("class"))
# time.sleep(3)

# import time
# from selenium import webdriver
# from webdriver_manager.chrome import ChromeDriverManager
# from selenium.webdriver.chrome.service import Service
# from selenium.webdriver.support.ui import WebDriverWait
# from selenium.webdriver.support import expected_conditions as EC
#
# options = webdriver.ChromeOptions()
# options.add_argument("--disable-blink-features=AutomationControlled")
# service = Service(ChromeDriverManager().install())
# driver = webdriver.Chrome(service=service, options=options)
# wait = WebDriverWait(driver, 5, poll_frequency=1)
#
# links = ['https://hyperskill.org/login', 'https://stepik.org/', 'https://www.ozon.ru/']
# LOCATOR = ("xpath", "//header//a[@href]")
#
# for _ in range(len(links)-1):
#     driver.switch_to.new_window("tab")
#     time.sleep(3)
#
# wait.until(EC.number_of_windows_to_be(len(links)))
# windows = driver.window_handles
#
# for i in range(len(windows)):
#      driver.switch_to.window(windows[i])
#      time.sleep(2)
#      driver.get(links[i])
#      time.sleep(2)
#
# for i in range(len(windows)):
#      driver.switch_to.window(windows[i])
#      print(driver.title)
#
# for i in range(len(windows)):
#      driver.switch_to.window(windows[i])
#      wait.until(EC.presence_of_all_elements_located(LOCATOR))
#      page_links = driver.find_elements(*LOCATOR)
#      print(page_links[0].get_attribute("href"))
#      page_links[0].click()

# nums = {4, 5, 6, 7, 8, 9}
# diff = 2
# counter = 0

# for i in range(len(nums) - 2):
#      for j in range(i+1, len(nums) - 1):
#           if nums[j] - nums[i] == diff:
#                for k in range(j+1, len(nums)):
#                     if nums[k] - nums[j] == diff:
#                          counter += 1
#                     elif nums[k] - nums[j] > diff:
#                          break
#           elif nums[j] - nums[i] > diff:
#                break
# print(counter)

# for i in nums:
#      if i + diff in nums and i + (2 * diff) in nums:
#         counter += 1
# print(counter)
