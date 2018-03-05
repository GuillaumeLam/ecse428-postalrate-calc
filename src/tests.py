import unittest
from parcel import Parcel
from errors import Errors



class TestPostalRateCalculator(unittest.TestCase):

    def setUp(self):
        self.testparcel = Parcel(0,0,0,0,0,0,0)
        self.testparcel.sameto = []

    # test whether an Exception has been raised when no arguments are inputted
    def test_01_no_arguments(self):
        with self.assertRaises(Exception):
            Errors.no_args(1)

    # test whether an Exception has been raised when too few arguments are inputted
    def test_02_too_few_arguments(self):
        with self.assertRaises(Exception):
            Errors.missing_args(4)

    # test whether an Exception has been raised when too many arguments are inputted
    def test_03_too_many_arguments(self):
        with self.assertRaises(Exception):
            Errors.too_many_args(9)

    # test whether the inputted postal code is an acceptable string
    def test_04_valid_form_of_from_postalcode(self):
        testparcel = Parcel('A0Z', 0, 0, 0, 0, 0, 0)
        self.assertTrue(testparcel.pc_valid_form())
        testparcel = Parcel('Home', 0, 0, 0, 0, 0, 0)
        self.assertFalse(testparcel.pc_valid_form())
        testparcel = Parcel( 0, 'Z1A', 0, 0, 0, 0, 0)
        self.assertTrue(testparcel.pc_valid_form())
        testparcel = Parcel(0, 'School', 0, 0, 0, 0, 0)
        self.assertFalse(testparcel.pc_valid_form())

    # test whether the From postal code is a valid one from the CSV list
    def test_05_valid_from_postalcode(self):
        testparcel = Parcel('V9A',0,0,0,0,0,0)
        self.assertTrue(testparcel.from_pc_valid())
        testparcel = Parcel('Z8H',0,0,0,0,0,0)
        self.assertFalse(testparcel.from_pc_valid())

    # test whether the To postal code is a valid one from the CSV list, if the To postal code is valid
    def test_06_valid_to_postalcode(self):
        testparcel = Parcel('V9A','H1Y',0,0,0,0,0)
        testparcel.from_pc_valid()
        self.assertTrue(testparcel.to_pc_valid())
        testparcel.to_pc = 'A2Z'
        self.assertFalse(testparcel.to_pc_valid())

    # test whether the shipment type is one of the three options: Regular, Xpress, Priority
    def test_07_valid_shipment_type(self):
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
