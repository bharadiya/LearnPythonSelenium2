import time

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions

driver = webdriver.Chrome("/drivers/chromedriver.exe")
driver.maximize_window()

driver.get("https://fb.com")

driver.save_screenshot("abc.png")

webelementEmail = driver.find_element(By.XPATH,"//input[@placeholder='Email address or phone number']")
webElementPassword = driver.find_element(By.NAME,"pass")
webElementForgottenPassword =driver.find_element(By.PARTIAL_LINK_TEXT,"Forgotten pass")



webelementEmail.send_keys("Hi@gmail.com")
webElementPassword.send_keys("123456")

titleOfPage=driver.title
print("Title of the page is " + titleOfPage)


webElementForgottenPassword.click()

time.sleep(5)
currentURL=driver.current_url
print(currentURL)
driver.back()

time.sleep(5)
driver.forward()

