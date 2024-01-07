import unittest
from selenium import webdriver


class verifyGoogleTitle(unittest.TestCase):

    # def test_AssertGoogleTitle(self):
    #     driver = webdriver.Chrome("../drivers/chromedriver.exe")
    #     driver.maximize_window()
    #     driver.get("https://google.com")
    #
    #     currentTitleOfGoogleGotByAutomation = driver.title
    #     print(currentTitleOfGoogleGotByAutomation)
    #
    #     self.assertEqual("Google", currentTitleOfGoogleGotByAutomation)
    #     driver.close()

    def test_AssertAutomationBlogSpot(self):
        driver = webdriver.Chrome("../drivers/chromedriver.exe")
        driver.maximize_window()
        driver.get("https://testautomationpractice.blogspot.com/")

        currentTitleOfGoogleGotByAutomation = driver.title
        print(currentTitleOfGoogleGotByAutomation)

        self.assertEqual("Automation Testing Practice", currentTitleOfGoogleGotByAutomation)
        driver.close()


if __name__ == "__main__":
    unittest.main()
