from selenium import webdriver

driver = webdriver.Firefox(executable_path="../drivers/geckodriver.exe")
driver.get('https://testautomationpractice.blogspot.com')
