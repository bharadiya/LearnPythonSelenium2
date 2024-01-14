import unittest

from selenium import webdriver

class TestOnFb(unittest.TestCase):

    def setUpClass(cls):
        print("Runs only once at class level , never runs before every test")
        cls.driver= webdriver.Chrome("../drivers/chromedriver.exe")
        cls.driver.maximize_window()
        cls.driver.get("https://fb.com")

    def tearDownClass(cls):
        print("Runs only once at class level , never runs after every test")
        cls.driver.close()

    def testCaseTryLoggingIntoFB(self):
        lp = LoginPage(self.driver)
