import unittest
import time

from selenium import webdriver

class AppTesting(unittest.TestCase):

    def test_AssertGoogleTitle(self):
        driver = webdriver.Chrome()
        driver.maximize_window()
        driver.get("https://google.com")
        getTitle = driver.title
        print(getTitle)
        self.assertNotEqual("Googl",getTitle)

    # def test_AssertGoogleTitle(self):
    #     driver = webdriver.Chrome()
    #     driver.maximize_window()
    #     driver.get("https://google.com")
    #     getTitle = driver.title
    #     print(getTitle)
    #     print("Googl" == getTitle)
    #     self.assertFalse("Googl" == getTitle)

    # def test_AssertNoneParams(self):
    #     d = None
    #     self.assertIsNotNone(d)

if __name__ == "__main__":
    unittest.main()


