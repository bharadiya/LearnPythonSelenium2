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

# male = driver.find_element(By.XPATH, "//input[@id='male']")
# male.click()
#
# selectCountry= driver.find_element(By.ID,"country")
# selectorForCountry = Select(selectCountry)
#
# selectorForCountry.select_by_index(3)
# selectorForCountry.select_by_value("australia")
#
# def checkWeekDay(driver,dayName):
#     driver.find_element(By.XPATH, "//input[@id='" + dayName + "']").click()
#
# checkWeekDay(driver,"thursday")


action = ActionChains(driver)

dragMeToTarget = driver.find_element(By.XPATH,"//p[text()='Drag me to my target']/parent::div")
dropToTarget = driver.find_element(By.XPATH,"//p[text()='Drop here']/parent::div")

action.drag_and_drop(dragMeToTarget,dropToTarget).perform()
# driver.save_screenshot("C:\\Users\\poona\\PycharmProjects\\LearnSelenium\\Screenshots\\drag.png")

screenshot = Image.open('dragBy.png')
screenshot.show()


