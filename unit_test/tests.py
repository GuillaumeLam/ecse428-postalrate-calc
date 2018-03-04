import unittest
from src.parcel import Parcel


class TestPostalRateCalculator(unittest.TestCase):
    # def setUp(self):

    def test_no_arguments(self):
        Parcel(0,0,0,0,0,0,0)
        print("test 1")

    def test_too_few_arguments(self):
        print("test 2")


if __name__ == '__main__':
    unittest.main()
