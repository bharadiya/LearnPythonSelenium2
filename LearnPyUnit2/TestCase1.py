import unittest
from selenium import webdriver

class SearchEngineTest(unittest.TestCase):
    def test_Google(self):
        self.driver = webdriver.Chrome()
        self.driver.get("https://redbus.in")
        print("Tiltle of the page "+ self.driver.title)

if __name__ == "__main__":
    unittest.main()
