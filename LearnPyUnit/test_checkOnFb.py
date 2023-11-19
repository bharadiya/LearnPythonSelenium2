import time
import pytest
from selenium import webdriver
from Pages.Loginpage import Loginpage

driver = None
def setup_module(self,module):
    print('------------------set up method --------------------------------')
    options = webdriver.ChromeOptions()
    options.add_experimental_option("detach", True)
    self.driver = webdriver.Chrome(options=options)
    self.driver.maximize_window()
    self.driver.get("https://fb.com")

def teardown_module(self,module):
    print('------------------tear down method------------------------')
    self.driver.close()

def test_checkLoginOnFb(self):
    time.sleep(5)
    l = Loginpage(self.driver)
    l.enterUserName(self.driver,"s.b@gmail.com")
    l.enterPassword(self.driver,"jfkdjfkdjfkdjkfjdjfk")
    l.clickLoginButton(self.driver)
