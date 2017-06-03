# -*- coding: utf-8 -*-
from selenium import webdriver
from selenium.common.exceptions import *
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

driver = webdriver.Firefox()
#driver.set_window_size(1400,1000)
driver.get("https://www.facebook.com")
email=driver.find_element_by_name('email')
email.clear()
email.send_keys("") # email here
passw=driver.find_element_by_name("pass")
passw.clear()
passw.send_keys("") # password here
try :
    driver.find_element_by_name("login").click()
except  Exception:
    driver.find_element_by_xpath("//input[@type='submit']").click()
time.sleep(2)
driver.get("https://www.facebook.com/groups/")
time.sleep(1)
count=0
driver.find_element_by_partial_link_text("Группы").click()
time.sleep(1)

linklist=[]
for group in driver.find_elements_by_partial_link_text("действия ожидающие подтверждения"):
    linklist.append(group.get_attribute("href"))
for url in linklist:
    driver.get(url)
    for item in driver.find_elements_by_xpath("//a[@data-tooltip-content=\"Удалить\"]"):
        item.click()
        time.sleep(2)
        try:
            driver.find_element_by_css_selector('.layerConfirm').click()
        except:
            pass
        time.sleep(4)
        try:
            driver.find_element_by_css_selector(".confirm_dialog")
            driver.find_element_by_css_selector('.layerConfirm').click()
        except Exception:
            pass
