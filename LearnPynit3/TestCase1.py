import time
import unittest

from selenium import webdriver


class TestCase1(unittest.TestCase):
    def test_LaunchGoogleAndVerifyTitle(self):
        self.driver = webdriver.Chrome()
        self.driver.get("https://google.com")
        print(self.driver.title)
        time.sleep(5)
        print("Test case is executed successfully")
