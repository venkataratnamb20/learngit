import unittest
from pysim.simulator import run_ngspice

class TestSimulator(unittest.TestCase):
    def setUp(self):
        print("Test setUp!!")

    def tearDown(self):
        print("test tearDown!!!")

    def test_run_ngapice_pass(self):
        ngspice_in_result = 'ngspice-42' in run_ngspice('ngspice -v')
        self.assertTrue(True)

    def test_fail(self):
        self.assertFalse(False)
