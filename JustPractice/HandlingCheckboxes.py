import time

from selenium import webdriver
from selenium.common import NoSuchElementException
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
from selenium.webdriver.common.action_chains import ActionChains
from PIL import Image
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions

# options = webdriver.ChromeOptions()
# options.add_experimental_option("detach",True)
driver = webdriver.Chrome()
driver.maximize_window()
driver.get("https://opensource-demo.orangehrmlive.com/web/index.php/auth/login")

username=driver.find_element(By.XPATH,"//input[@name='username']")
wait = WebDriverWait(driver,30)
wait.until(expected_conditions.element_to_be_clickable(username))
username.send_keys("Admin")

password = driver.find_element(By.NAME,"password")
password.send_keys("admin123")
driver.find_element(By.XPATH,"//button[contains(text(),'')]").click()

wait.until(expected_conditions.element_to_be_clickable(driver.find_element(By.XPATH,"//input[@name='username']")))
driver.find_element(By.XPATH,"//span[text()='Admin']").click();

time.sleep(6)
action = ActionChains(driver)
usernameCheckbox = driver.find_element(By.XPATH,"//div[text()='Username']/preceding-sibling::div//input")
action.click(usernameCheckbox).perform();

driver.save_screenshot('ss2.png')
screenshot = Image.open('ss.png')
screenshot.show()
