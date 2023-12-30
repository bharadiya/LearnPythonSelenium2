import unittest


# def setUpModule():
#     print("set up module")
#
# def tearDownModule():
#     print("tear down module")

class AppTesting(unittest.TestCase):
    # @classmethod
    # def setUp(self):
    #     print("Login")
    #
    # @classmethod
    # def setUpClass(cls):
    #     print("open application")
    #
    # @classmethod
    # def tearDownClass(cls):
    #     print("close application")

    def test_search(self):
        print("This is search test")

    @unittest.skip("Skipping as this is blocking other test case")
    def test_AdvancedSearch(self):
        print("This is advanced search test")

    @unittest.SkipTest
    def test_prepaidRecharge(self):
        print("This is prepaid recharge test")

    @unittest.skipIf(1==1,"skipping this one as condition is satisfied")
    def test_postpaidRecharge(self):
        print("This is post paid test")  #  # @classmethod  # def tearDown(self):  #     print("Logout")


if __name__ == "__main__":
    unittest.main()
