import time

from selenium import webdriver
from selenium.webdriver.common.alert import Alert
from selenium.webdriver.common.by import By

driver = webdriver.Chrome("../drivers/chromedriver.exe")
driver.maximize_window()

driver.get("https://testautomationpractice.blogspot.com")
time.sleep(5)

al = Alert(driver)

# alertBtn = driver.find_element(By.XPATH,"//button[text()='Alert']")
# alertBtn.click()
# time.sleep(3)
# al.accept()
#
#
# alertBtnConfirmBox = driver.find_element(By.XPATH,"//button[text()='Confirm Box']")
# alertBtnConfirmBox.click()
# time.sleep(3)
# al.dismiss()

alertBtnSendKeys = driver.find_element(By.XPATH,"//button[text()='Prompt']")
alertBtnSendKeys.click()
time.sleep(3)
al.send_keys("Shweta")
al.accept()
