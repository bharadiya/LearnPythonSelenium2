import time

from PIL import Image
from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.select import Select
from selenium.webdriver.support.wait import WebDriverWait

driver = webdriver.Firefox("../drivers/chromedriver.exe")
driver.maximize_window()

driver.get("https://testautomationpractice.blogspot.com")
male = driver.find_element(By.XPATH, "//input[@id='male']")
wait = WebDriverWait(driver, 20)
wait.until(expected_conditions.visibility_of(male))
male.click()

# In industry , its not a good practice to use time.sleep() , its recommended to use either implicit or explicit waits
# Polling time is by default set to 0.5s
# But selenium recommends you don't user explicit and implicit wait together
