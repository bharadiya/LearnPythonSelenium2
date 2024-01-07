from selenium.webdriver.firefox import webdriver

driver = webdriver.Firefox("C:\\Users\\poona\\PycharmProjects\\LearnSelenium\\drivers\\geckodriver.exe")
driver.maximize_window()

driver.get("https://testautomationpractice.blogspot.com")
