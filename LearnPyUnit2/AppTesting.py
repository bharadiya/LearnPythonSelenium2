import unittest


# def setUpModule():
#     print("set up module")
#
# def tearDownModule():
#     print("tear down module")

class AppTesting(unittest.TestCase):
    @classmethod
    def setUp(self):
        print("runs before every test")

    @classmethod
    def setUpClass(cls):
        print("runs only once and that too before setup only once")

    @classmethod
    def tearDownClass(cls):
        print("runs only once and that too after teardown only once")

    @classmethod
    def tearDown(self):
        print("Runs after every test")

    def test_search(self):
        print("This is search test")

    def test_AdvancedSearch(self):
        print("This is advanced search test")


    def test_prepaidRecharge(self):
        print("This is prepaid recharge test")


    def test_postpaidRecharge(self):
        print("This is post paid test")  #  # @classmethod  # def tearDown(self):  #     print("Logout")


if __name__ == "__main__":
    unittest.main()
