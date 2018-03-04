import unittest
from src.parcel import Parcel


class TestPostalRateCalculator(unittest.TestCase):
    # def setUp(self):
    def test_no_arguments(self):
        Parcel(0,0,0,0,0,0,0)

    def test_no_arguments_01(self):
        # Parcel(0,0,0,0,0,0,0)
        self.assertRaises(Exception, method0())
        print("test 1")

    def test_too_few_arguments_02(self):
        self.assertRaises(Exception, method1())
        print("test 2")

    def test_valid_from_postalcode_03(self):
        self.assertTrue(method2())
        print("test 3")

    def test_valid_to_postalcode_04(self):
        self.assertEqual(MTL, method3())

    def test_valid_shipment_type_04(self):
        self.assertTrue(method3())

    def test_length_is_not_too_low_04(self):

        self.assertTrue(val <= method4())

    def test_length_is_not_too_high_05(self):
        self.assertTrue(val >= method4())

    def test_width_is_not_too_low_06(self):
        self.assertTrue(val <= method4())

    def test_width_is_not_too_high_07(self):
        self.assertTrue(val >= method5())

    def test_height_is_in_not_too_low_08(self):
        self.assertTrue(val <= method4())

    def test_height_is_in_not_too_high_09(self):
        self.assertTrue(val >= method4())

    def test_weight_is_not_too_low_for_regular_10(self):
        self.assertTrue(val <= method4())

    def test_weight_is_not_too_high_for_regular_11(self):
        self.assertTrue(val >= method4())


    def test_weight_is_not_too_low_for_priority_12(self):
        self.assertTrue(val <= method4())

    def test_weight_is_not_too_high_for_priority_13(self):
        self.assertTrue(val >= method4())

    def test_weight_is_in_range_for_XXXpress_09(self):
        self.assertTrue(val <= method4())
        self.assertTrue(val >= method4())

    def test_rate_validity_10(self):



if __name__ == '__main__':
    unittest.main()
