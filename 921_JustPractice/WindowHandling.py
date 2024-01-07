import time

from PIL import Image
from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select

driver = webdriver.Chrome("../drivers/chromedriver.exe")
driver.maximize_window()

driver.get("https://testautomationpractice.blogspot.com")
time.sleep(5)

newBrowserWindow = driver.find_element(By.XPATH,"//button[text()='New Browser Window']")
newBrowserWindow.click()

windowHandles = driver.window_handles
time.sleep(3)
print(windowHandles)

driver.switch_to.window(windowHandles[1])
time.sleep(6)

action = ActionChains(driver)
search = driver.find_element(By.XPATH,"//input[@name='search']")

action.move_to_element(search).perform()
search.send_keys("HI")
time.sleep(1)

driver.switch_to.window(windowHandles[0])
time.sleep(3)

male = driver.find_element(By.XPATH, "//input[@id='male']")
male.click()




# for i in range(0,5):
#     for j in range(0,len(windowHandles)):
#         driver.switch_to.window(windowHandles[j])
#         time.sleep(3)

