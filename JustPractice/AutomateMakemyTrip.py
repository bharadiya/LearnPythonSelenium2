import time

from selenium import webdriver
from selenium.common import NoSuchElementException
from selenium.webdriver import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
from selenium.webdriver.common.action_chains import ActionChains
from PIL import Image
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions


def closePopUp(driver,action):
    time.sleep(2)
    action.click(driver.find_element(By.XPATH, "//span[@data-cy='closeModal']")).perform()

def enterFromandTo(fromOrTo,cityName,action):
    fromOrTo.send_keys(cityName)
    time.sleep(2)
    action.send_keys(Keys.DOWN).perform()
    action.send_keys(Keys.ENTER).perform()

def clickParticularDate(driver,date):
    allPrices = driver.find_elements(By.XPATH, "//div[@aria-disabled='false']//p[1]")
    for i in range(0, len(allPrices)):
        # print(allPrices[i].text)
        if allPrices[i].text == date:
            allPrices[i].click()
            break

options = webdriver.ChromeOptions()
options.add_experimental_option("detach", True)
driver = webdriver.Chrome(options=options)
driver.maximize_window()
wait = WebDriverWait(driver, timeout=20)

driver.get("https://makemytrip.com")
driver.set_page_load_timeout(20)
action = ActionChains(driver)

closePopUp(driver,action)
closePopUp(driver,action)

From = driver.find_element(By.XPATH, "//input[@id='fromCity']")
To = driver.find_element(By.XPATH, "//input[@id='toCity']")

enterFromandTo(From,"BOM",action)
enterFromandTo(To,"DEL",action)
clickParticularDate(driver,"17")

searchBtn = driver.find_element(By.XPATH,"//a[text()='Search']")
searchBtn.click()



