import unittest

# def setUpModule():
#     print("set up module before class level")
#
# def tearDownModule():
#     print("tear down module after class level")

class AppTesting(unittest.TestCase):
    # @classmethod
    # def setUp(self):
    #     print("Before Every Test")
    #
    # @classmethod
    # def setUpClass(cls):
    #     print("Before Class only 1 time")

    def test_search(self):
        print("This is search test")

    def test_AdvancedSearch(self):
        print("This is advanced search test")

    def test_prepaidRecharge(self):
        print("This is prepaid recharge test")

    def test_postpaidRecharge(self):
        print("This is post paid test")

    # @classmethod
    # def tearDown(self):
    #     print("After every test")
    #
    # @classmethod
    # def tearDownClass(cls):
    #     print("After Class only 1 time")

if __name__ == "__main__":
    unittest.main()
