import time

from selenium import webdriver

driver = webdriver.Edge("../drivers/msedgedriver.exe")
driver.maximize_window()
driver.get("https://testautomationpractice.blogspot.com")

