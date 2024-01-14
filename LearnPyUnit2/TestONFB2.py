import unittest
import time

from selenium import webdriver

from Pages.LoginPage2 import Loginpage2
from Pages.Loginpage import Loginpage

class AppTesting(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        lp = Loginpage2()
        lp.hitURL()

    def test_AssertGoogleTitle(self):
        lp = Loginpage2()
        lp.enterUserName("hi")

    @classmethod
    def tearDownClass(cls):
        lp = Loginpage2()
        lp.quitDriver()


if __name__ == "__main__":
    unittest.main()


