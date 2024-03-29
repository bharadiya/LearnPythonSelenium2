import time

from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait

options = webdriver.ChromeOptions()
options.add_experimental_option("detach",True)
driver = webdriver.Chrome(options=options)
driver.maximize_window()
driver.get("https://www.makemytrip.com/")

wait = WebDriverWait(driver,20)
time.sleep(10)

closeBtn=driver.find_element(By.XPATH,"//body")
wait.until(expected_conditions.element_to_be_clickable(closeBtn))
action = ActionChains(driver)
action.double_click(closeBtn).perform()


