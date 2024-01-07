import unittest

from selenium import webdriver


# def setUpModule():
#     print("set up module before class level at suite level")
#
# def tearDownModule():
#     print("tear down module after class level at suite level")

class AppTesting(unittest.TestCase):
    @classmethod
    def setUp(self):
        print("Before Every Test - Login")

    @classmethod
    def setUpClass(cls):
        print("Before Class only 1 time - Open Browser and hit URL")

    def test_search(self):
        print("This is search test - Functionality no . 1")

    def test_AdvancedSearch(self):
        print("This is advanced search test - Functionality no . 2")

    def test_prepaidRecharge(self):
        print("This is prepaid recharge test - Functionality no . 3")

    def test_postpaidRecharge(self):
        print("This is post paid test - Functionality no . 4")

    @classmethod
    def tearDown(self):
        print("After every test - Logout")

    #
    @classmethod
    def tearDownClass(cls):
        print("After Class only 1 time - Close browser")


if __name__ == "__main__":
    unittest.main()

# set up method will run before every test case (self)
# teardown method will run after every test case (self)
# setUpClass method will run one time before class (cls)
# tearDownClass method will run one time after class  (cls)
#
#
# all this methods name should be exactly same except for your test case and you need to add @classMethod annotation on the top of method
