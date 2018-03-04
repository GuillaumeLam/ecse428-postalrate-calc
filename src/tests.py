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
        self.testparcel.sameto = []

    def test_01_no_arguments(self):
        with self.assertRaises(Exception):
            Errors.no_args(1)

    def test_02_too_few_arguments(self):
        with self.assertRaises(Exception):
            Errors.missing_args(4)

    def test_03_valid_from_postalcode(self):
        testparcel = Parcel('V9A',0,0,0,0,0,0)
        self.assertTrue(testparcel.from_pc_valid())

    def test_04_valid_to_postalcode(self):
        testparcel = Parcel('V9A','H1Y',0,0,0,0,0)
        testparcel.from_pc_valid()
        self.assertTrue(testparcel.to_pc_valid())

    def test_05_valid_shipment_type(self):
        testparcel = Parcel(0,0,0,0,0,0,'Regular')
        self.assertTrue(testparcel.is_postal_type_valid())
        testparcel.weight = 'Xpress'
        self.assertTrue(testparcel.is_postal_type_valid())
        testparcel.weight = 'Priority'
        self.assertTrue(testparcel.is_postal_type_valid())


    def test_06_length_is_not_too_low(self):
        testparcel = Parcel(0,0,10,0,0,0,0)
        self.assertTrue(testparcel.length_is_not_too_low())
        testparcel = Parcel(0, 0, 9, 0, 0, 0, 0)
        self.assertFalse(testparcel.length_is_not_too_low())

    def test_07_length_is_not_too_high(self):
        testparcel = Parcel(0, 0, 210, 0, 0, 0, 0)
        self.assertTrue(testparcel.length_is_not_too_high())
        testparcel = Parcel(0, 0, 211, 0, 0, 0, 0)
        self.assertFalse(testparcel.length_is_not_too_high())

    def test_08_width_is_not_too_low(self):
        testparcel = Parcel(0, 0, 0, 7, 0, 0, 0)
        self.assertTrue(testparcel.width_is_not_too_low())
        testparcel = Parcel(0, 0, 0, 6, 0, 0, 0)
        self.assertFalse(testparcel.width_is_not_too_low())

    def test_09_width_is_not_too_high(self):
        testparcel = Parcel(0, 0, 0, 275, 0, 0, 0)
        self.assertTrue(testparcel.width_is_not_too_high())
        testparcel = Parcel(0, 0, 0, 276, 0, 0, 0)
        self.assertFalse(testparcel.width_is_not_too_high())

    def test_10_height_is_not_too_low(self):
        testparcel = Parcel(0, 0, 0, 0, 1, 0, 0)
        self.assertTrue(testparcel.width_is_not_too_low())
        testparcel = Parcel(0, 0, 0, 0, 0, 0, 0)
        self.assertFalse(testparcel.width_is_not_too_low())

    def test_11_height_is_not_too_high(self):
        testparcel = Parcel(0, 0, 0, 0, 210, 0, 0)
        self.assertTrue(testparcel.width_is_not_too_high())
        testparcel = Parcel(0, 0, 0, 0, 211, 0, 0)
        self.assertFalse(testparcel.width_is_not_too_high())

    def test_12_weight_is_not_too_low_for_regular(self):
        testparcel = Parcel(0, 0, 0, 0, 0, 0 , 0)
        self.assertTrue(testparcel.is_weight_not_too_low_for_regular())
        testparcel = Parcel(0, 0, 0, 0, 0, -1, 0)
        self.assertFalse(testparcel.is_weight_not_too_low_for_regular())

    def test_13_weight_is_not_too_high_for_regular(self):
        testparcel = Parcel(0, 0, 0, 0, 0, 10, 0)
        self.assertTrue(testparcel.is_weight_not_too_high_for_regular())
        testparcel = Parcel(0, 0, 0, 0, 0, 11, 0)
        self.assertFalse(testparcel.is_weight_not_too_high_for_regular())

    def test_14_weight_is_not_too_low_for_xpress(self):
        testparcel = Parcel(0, 0, 0, 0, 0, 21, 0)
        self.assertTrue(testparcel.is_weight_not_too_low_for_xpress())
        testparcel = Parcel(0, 0, 0, 0, 0, 20, 0)
        self.assertFalse(testparcel.is_weight_not_too_low_for_xpress())

    def test_15_weight_is_not_too_high_for_xpress(self):
        testparcel = Parcel(0, 0, 0, 0, 0, 30, 0)
        self.assertTrue(testparcel.is_weight_not_too_high_for_xpress())
        testparcel = Parcel(0, 0, 0, 0, 0, 31, 0)
        self.assertFalse(testparcel.is_weight_not_too_high_for_xpress())

    def test_16_weight_is_not_too_low_for_priority(self):
        testparcel = Parcel(0, 0, 0, 0, 0, 11, 0)
        self.assertTrue(testparcel.is_weight_not_too_low_for_priority())
        testparcel = Parcel(0, 0, 0, 0, 0, 10, 0)
        self.assertFalse(testparcel.is_weight_not_too_low_for_priority())

    def test_17_weight_is_not_too_high_for_priority(self):
        testparcel = Parcel(0, 0, 0, 0, 0, 20, 0)
        self.assertTrue(testparcel.is_weight_not_too_high_for_priority())
        testparcel = Parcel(0, 0, 0, 0, 0, 21, 0)
        self.assertFalse(testparcel.is_weight_not_too_high_for_priority())





if __name__ == '__main__':
    unittest.main()
