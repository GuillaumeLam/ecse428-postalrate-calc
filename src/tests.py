import unittest
from parcel import Parcel
from errors import Errors


# min_length = 10
# max_length = 210
# min_height = 1
# max_height = 210
# min_width = 7
# max_width = 275
#
# min_weight_regular = 0
# max_weight_regular = 10
#
# min_weight_priority = 11
# max_weight_priority = 20
#
# min_weight_xpress = 21
# max_weight_xpress = 30
#
# rs_rate = 1.619
# xs_rate = 1.149
# ps_rate = 0.964


class TestPostalRateCalculator(unittest.TestCase):
    def setUp(self):
        self.testparcel = Parcel(0,0,0,0,0,0,0)

    def test_no_arguments_01(self):
        with self.assertRaises(Exception):
            Errors.no_args(1)

    def test_too_few_arguments_02(self):
        with self.assertRaises(Exception):
            Errors.missing_args(4)

    def test_valid_from_postalcode_03(self):
        testparcel = Parcel('V9A',0,0,0,0,0,0)
        self.assertTrue(testparcel.from_pc_valid())

    # def test_valid_to_postalcode_04(self):
    #     Parcel.to = "H1Y"
    #     self.assertTrue(Parcel.from_pc_valid())
    #
    # def test_valid_shipment_type_04(self):
    #
    #     self.assertTrue(method3())
    #
    # def test_length_is_not_too_low_04(self):
    #
    #     self.assertTrue(min_length <= method4())
    #
    # def test_length_is_not_too_high_05(self):
    #     self.assertTrue(max_length >= method4())
    #
    # def test_width_is_not_too_low_06(self):
    #     self.assertTrue(min_width <= method4())
    #
    # def test_width_is_not_too_high_07(self):
    #     self.assertTrue(max_width >= method5())
    #
    # def test_height_is_in_not_too_low_08(self):
    #     self.assertTrue(min_height <= method4())
    #
    # def test_height_is_in_not_too_high_09(self):
    #     self.assertTrue(max_height >= method4())
    #
    # def test_weight_is_not_too_low_for_regular_10(self):
    #     self.assertTrue(min_weight_regular <= method4())
    #
    # def test_weight_is_not_too_high_for_regular_11(self):
    #     self.assertTrue(max_weight_regular >= method4())
    #
    # def test_weight_is_not_too_low_for_priority_12(self):
    #     self.assertTrue(min_weight_priority <= method4())
    #
    # def test_weight_is_not_too_high_for_priority_13(self):
    #     self.assertTrue(max_weight_priority >= method4())
    #
    # def test_weight_is_in_range_for_xpress_14(self):
    #     self.assertTrue(min_weight_xpress <= method4())
    #
    # def test_weigth_is_in_range_for_xpress_15(self):
    #     self.assertTrue(max_weight_xpress >= method4())
    #
    # def test_rate_validity_10(self):


if __name__ == '__main__':
    unittest.main()
