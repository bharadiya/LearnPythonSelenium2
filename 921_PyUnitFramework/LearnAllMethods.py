import unittest

from selenium import webdriver


# def setUpModule():
#     print("set up module before class level at suite level")
#
# def tearDownModule():
#     print("tear down module after class level at suite level")

class AppTesting(unittest.TestCase):
    def test_search(self):
        print("This is search test - Functionality no . 1")

    @unittest.SkipTest
    def test_AdvancedSearch(self):
        print("This is advanced search test - Functionality no . 2")
    @unittest.skip("As client told")
    def test_prepaidRecharge(self):
        print("This is prepaid recharge test - Functionality no . 3")
    @unittest.skipIf(1==2,"as condition is passed")
    def test_postpaidRecharge(self):
        print("This is post paid test - Functionality no . 4")

if __name__ == "__main__":
    unittest.main()
