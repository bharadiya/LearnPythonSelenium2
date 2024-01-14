import time

from PIL import Image
from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select

driver = webdriver.Chrome("../drivers/chromedriver.exe")
driver.maximize_window()

driver.get("https://testautomationpractice.blogspot.com")
driver.set_page_load_timeout(25)

driver.find_element(By.ID, "datepicker").click()
time.sleep(2)

def clickCalendarDate(driver,day):
    days = driver.find_elements(By.XPATH, "//td[@data-handler='selectDay']/a")
    for i in range(0, len(days)):
        if days[i].text == day:
            days[i].click()
            break

clickCalendarDate(driver,"25")

dataFourthRow = driver.find_elements(By.XPATH,"//table[@name='BookTable']//tr[4]/td")
for i in range(0, len(dataFourthRow)):
    print(dataFourthRow[i].text)

