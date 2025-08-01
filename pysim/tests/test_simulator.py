import unittest

class TestSimulator(unittest.TestCase):
    def setUp(self):
        print("Test setUp!!")

    def tearDown(self):
        print("test tearDown!!!")

    def test_pass(self):
        self.assertTrue(True)

    def test_fail(self):
        self.assertFalse(False)
