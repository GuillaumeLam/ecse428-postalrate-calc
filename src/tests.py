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

    def test_03_too_many_arguments(self):
        with self.assertRaises(Exception):
            Errors.too_many_args(9)

    def test_03_valid_from_postalcode(self):
        testparcel = Parcel('V9A',0,0,0,0,0,0)
        self.assertTrue(testparcel.from_pc_valid())

    def test_04_valid_to_postalcode(self):
        testparcel = Parcel('V9A','H1Y',0,0,0,0,0)
        testparcel.from_pc_valid()
        self.assertTrue(testparcel.to_pc_valid())

        #testparcel.from_pc = 'H1Y'
        #self.assertTrue(testparcel.from_pc_valid())

    def test_05_valid_shipment_type(self):
        testparcel = Parcel(0,0,0,0,0,0,'Regular')
        self.assertTrue(testparcel.is_postal_type_valid())
        testparcel.type = 'Xpress'
        self.assertTrue(testparcel.is_postal_type_valid())
        testparcel.weight = 'Priority'
        self.assertTrue(testparcel.is_postal_type_valid())

    def test_06_length_is_not_too_low(self):
        testparcel = Parcel(0,0,0,0,0,0,0)
        testparcel.sameto = [['V9A', 'H1Y', 'Regular', 10, 210, 7, 275, 1, 210, 0, 10, 1.619]]
        testparcel.length = 10
        self.assertTrue(testparcel.length_is_not_too_low())
        testparcel.length = 9
        self.assertFalse(testparcel.length_is_not_too_low())

    def test_07_length_is_not_too_high(self):
        testparcel = Parcel(0, 0, 0, 0, 0, 0, 0)
        testparcel.sameto = [['V9A', 'H1Y', 'Regular', 10, 210, 7, 275, 1, 210, 0, 10, 1.619]]
        testparcel.length = 210
        self.assertTrue(testparcel.length_is_not_too_high())
        testparcel.length = 211
        self.assertFalse(testparcel.length_is_not_too_high())

    def test_08_width_is_not_too_low(self):
        testparcel = Parcel(0, 0, 0, 0, 0, 0, 0)
        testparcel.sameto = [['V9A', 'H1Y', 'Regular', 10, 210, 7, 275, 1, 210, 0, 10, 1.619]]
        testparcel.width = 1
        self.assertTrue(testparcel.width_is_not_too_low())
        testparcel.width = 0
        self.assertFalse(testparcel.width_is_not_too_low())

    def test_09_width_is_not_too_high(self):
        testparcel = Parcel(0, 0, 0, 0, 0, 0, 0)
        testparcel.sameto = [['V9A', 'H1Y', 'Regular', 10, 210, 7, 275, 1, 210, 0, 10, 1.619]]
        testparcel.width = 210
        self.assertTrue(testparcel.width_is_not_too_high())
        testparcel.width = 211
        self.assertFalse(testparcel.width_is_not_too_high())

    def test_10_height_is_not_too_low(self):
        testparcel = Parcel(0, 0, 0, 0, 0, 0, 0)
        testparcel.sameto = [['V9A', 'H1Y', 'Regular', 10, 210, 7, 275, 1, 210, 0, 10, 1.619]]
        testparcel.height = 7
        self.assertTrue(testparcel.height_is_not_too_low())
        testparcel.height = 6
        self.assertFalse(testparcel.height_is_not_too_low())

    def test_11_height_is_not_too_high(self):
        testparcel = Parcel(0, 0, 0, 0, 0, 0, 0)
        testparcel.sameto = [['V9A', 'H1Y', 'Regular', 10, 210, 7, 275, 1, 210, 0, 10, 1.619]]
        testparcel.height = 275
        self.assertTrue(testparcel.height_is_not_too_high())
        testparcel.height = 276
        self.assertFalse(testparcel.height_is_not_too_high())

    def test_12_weight_is_not_too_low_for_small(self):
        testparcel = Parcel(0, 0, 0, 0, 0, 0, 0)
        testparcel.weight = 1
        self.assertTrue(testparcel.is_weight_not_too_low_for_small())
        testparcel.weight = 0
        self.assertFalse(testparcel.is_weight_not_too_low_for_small())

    def test_13_weight_is_not_too_high_for_small(self):
        testparcel = Parcel(0, 0, 0, 0, 0, 0, 0)
        testparcel.weight = 10
        self.assertTrue(testparcel.is_weight_not_too_high_for_small())
        testparcel.weight = 11
        self.assertFalse(testparcel.is_weight_not_too_high_for_small())

    def test_14_weight_is_not_too_low_for_medium(self):
        testparcel = Parcel(0, 0, 0, 0, 0, 0, 0)
        testparcel.weight = 11
        self.assertTrue(testparcel.is_weight_not_too_low_for_medium())
        testparcel.weight = 10
        self.assertFalse(testparcel.is_weight_not_too_low_for_medium())

    def test_15_weight_is_not_too_high_for_medium(self):
        testparcel = Parcel(0, 0, 0, 0, 0, 0, 0)
        testparcel.weight = 20
        self.assertTrue(testparcel.is_weight_not_too_high_for_medium())
        testparcel.weight = 21
        self.assertFalse(testparcel.is_weight_not_too_high_for_medium())

    def test_16_weight_is_not_too_low_for_large(self):
        testparcel = Parcel(0, 0, 0, 0, 0, 0, 0)
        testparcel.weight = 21
        self.assertTrue(testparcel.is_weight_not_too_low_for_large())
        testparcel.weight = 20
        self.assertFalse(testparcel.is_weight_not_too_low_for_large())

    def test_17_weight_is_not_too_high_for_large(self):
        testparcel = Parcel(0, 0, 0, 0, 0, 0, 0)
        testparcel.weight = 30
        self.assertTrue(testparcel.is_weight_not_too_high_for_large())
        testparcel.weight = 31
        self.assertFalse(testparcel.is_weight_not_too_high_for_large())


if __name__ == '__main__':
    unittest.main()
