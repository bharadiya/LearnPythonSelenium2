import time

from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select

driver = webdriver.Chrome("C:\\Users\\poona\\PycharmProjects\\LearnSelenium\\drivers\\chromedriver.exe")
driver.maximize_window()

driver.get("https://testautomationpractice.blogspot.com")

male = driver.find_element(By.XPATH, "//input[@id='male']")
male.click()

selectCountry= driver.find_element(By.ID,"country")
selectorForCountry = Select(selectCountry)

selectorForCountry.select_by_index(3)
selectorForCountry.select_by_value("australia")

def checkWeekDay(driver,dayName):
    driver.find_element(By.XPATH, "//input[@id='" + dayName + "']").click()

checkWeekDay(driver,"thursday")


action = ActionChains(driver)

