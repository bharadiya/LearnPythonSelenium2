import time

from PIL import Image
from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select

driver = webdriver.Chrome("../drivers/chromedriver.exe")
driver.maximize_window()

driver.get("https://testautomationpractice.blogspot.com")
driver.implicitly_wait(20)
male = driver.find_element(By.XPATH, "//input[@id='males']")
male.click()

# In industry , its not a good practice to use time.sleep() , its recommended to use either implicit or explicit waits

