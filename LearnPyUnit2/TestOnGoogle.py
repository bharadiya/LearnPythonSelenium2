import unittest
import time

from selenium import webdriver
from Pages.Loginpage import Loginpage
class AppTesting(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.driver = webdriver.Chrome("../drivers/chromedriver.exe")
        cls.driver.maximize_window()
        cls.driver.get("https://fb.com")

    def test_AssertGoogleTitle(self):
        lp = Loginpage(self.driver)
        lp.enterUserName(self.driver,"ABC")
        lp.enterPassword(self.driver,"DEF")
        lp.clickLoginButton(self.driver)

    @classmethod
    def tearDownClass(cls):
        cls.driver.quit()


if __name__ == "__main__":
    unittest.main()


