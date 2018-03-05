import unittest
from parcel import Parcel
from errors import Errors


class TestPostalRateCalculator(unittest.TestCase):

    # test whether an Exception has been raised when no arguments are inputted
    def test_01_no_arguments(self):
        with self.assertRaises(Exception):
            Errors.no_args(1)

    # test whether an Exception has been raised when too few arguments are inputted
    def test_02_too_few_arguments(self):
        with self.assertRaises(Exception):
            Errors.missing_args(7)

    # test whether an Exception has been raised when too many arguments are inputted
    def test_03_too_many_arguments(self):
        with self.assertRaises(Exception):
            Errors.too_many_args(20)

    # test whether the From postal code is a valid one from the CSV list
    def test_04_existing_from_postalcode(self):
        testparcel = Parcel('V9A',0,0,0,0,0,0)
        self.assertTrue(testparcel.from_pc_valid())
        testparcel = Parcel('Z8H',0,0,0,0,0,0)
        self.assertFalse(testparcel.from_pc_valid())

    # test whether the To postal code is a valid one from the CSV list, if the To postal code is valid
    def test_05_existing_to_postalcode(self):
        testparcel = Parcel('V9A','H1Y',0,0,0,0,0)
        testparcel.from_pc_valid()
        self.assertTrue(testparcel.to_pc_valid())
        testparcel.to_pc = 'A2Z'
        testparcel.from_pc_valid()
        self.assertFalse(testparcel.to_pc_valid())

    # test whether the shipment type is one of the three options: Regular, Xpress, Priority
    def test_06_valid_shipment_type(self):
        testparcel = Parcel(0,0,0,0,0,0,'Regular')
        self.assertTrue(testparcel.is_postal_type_valid())
        testparcel.p_type = 'Xpress'
        self.assertTrue(testparcel.is_postal_type_valid())
        testparcel.p_type = 'Priority'
        self.assertTrue(testparcel.is_postal_type_valid())
        testparcel.p_type = 'Fast'
        self.assertFalse(testparcel.is_postal_type_valid())

    # test whether the length is not below the minimum length (10 cm)
    def test_07_length_is_not_too_low(self):
        testparcel = Parcel(0,0,0,0,0,0,0)
        testparcel.sameto = [['V9A', 'H1Y', 'Regular', 10, 210, 7, 275, 1, 210, 0, 10, 1.619]]
        testparcel.length = 10
        self.assertTrue(testparcel.length_is_not_too_low())
        testparcel.length = 9
        self.assertFalse(testparcel.length_is_not_too_low())

    # test whether the length is not above the maximum length (10 cm)
    def test_08_length_is_not_too_high(self):
        testparcel = Parcel(0, 0, 0, 0, 0, 0, 0)
        testparcel.sameto = [['V9A', 'H1Y', 'Regular', 10, 210, 7, 275, 1, 210, 0, 10, 1.619]]
        testparcel.length = 210
        self.assertTrue(testparcel.length_is_not_too_high())
        testparcel.length = 211
        self.assertFalse(testparcel.length_is_not_too_high())

    # test whether the width is not below the minimum width (1 cm)
    def test_09_width_is_not_too_low(self):
        testparcel = Parcel(0, 0, 0, 0, 0, 0, 0)
        testparcel.sameto = [['V9A', 'H1Y', 'Regular', 10, 210, 7, 275, 1, 210, 0, 10, 1.619]]
        testparcel.width = 1
        self.assertTrue(testparcel.width_is_not_too_low())
        testparcel.width = 0
        self.assertFalse(testparcel.width_is_not_too_low())

    # test whether the width is not above the maximum width (210 cm)
    def test_10_width_is_not_too_high(self):
        testparcel = Parcel(0, 0, 0, 0, 0, 0, 0)
        testparcel.sameto = [['V9A', 'H1Y', 'Regular', 10, 210, 7, 275, 1, 210, 0, 10, 1.619]]
        testparcel.width = 210
        self.assertTrue(testparcel.width_is_not_too_high())
        testparcel.width = 211
        self.assertFalse(testparcel.width_is_not_too_high())

    # test whether the height is not below the minimum height (7 cm)
    def test_11_height_is_not_too_low(self):
        testparcel = Parcel(0, 0, 0, 0, 0, 0, 0)
        testparcel.sameto = [['V9A', 'H1Y', 'Regular', 10, 210, 7, 275, 1, 210, 0, 10, 1.619]]
        testparcel.height = 7
        self.assertTrue(testparcel.height_is_not_too_low())
        testparcel.height = 6
        self.assertFalse(testparcel.height_is_not_too_low())

    # test whether the height is not above the maximum height (275 cm)
    def test_12_height_is_not_too_high(self):
        testparcel = Parcel(0, 0, 0, 0, 0, 0, 0)
        testparcel.sameto = [['V9A', 'H1Y', 'Regular', 10, 210, 7, 275, 1, 210, 0, 10, 1.619]]
        testparcel.height = 275
        self.assertTrue(testparcel.height_is_not_too_high())
        testparcel.height = 276
        self.assertFalse(testparcel.height_is_not_too_high())

    # test whether the weight is not below the minimum for a small package(1 cm)
    def test_13_weight_is_not_too_low_for_small(self):
        testparcel = Parcel(0, 0, 0, 0, 0, 0, 0)
        testparcel.weight = 1
        self.assertTrue(testparcel.is_weight_not_too_low_for_small())
        testparcel.weight = 0.234
        self.assertTrue(testparcel.is_weight_not_too_low_for_small())
        testparcel.weight = 0
        self.assertFalse(testparcel.is_weight_not_too_low_for_small())

    # test whether the weight is not above the maximum for a small package(10 cm)
    def test_14_weight_is_not_too_high_for_small(self):
        testparcel = Parcel(0, 0, 0, 0, 0, 0, 0)
        testparcel.weight = 10
        self.assertTrue(testparcel.is_weight_not_too_high_for_small())
        testparcel.weight = 11
        self.assertFalse(testparcel.is_weight_not_too_high_for_small())

    # test whether the weight is not below the minimum for a medium package(11 cm)
    def test_15_weight_is_not_too_low_for_medium(self):
        testparcel = Parcel(0, 0, 0, 0, 0, 0, 0)
        testparcel.weight = 11
        self.assertTrue(testparcel.is_weight_not_too_low_for_medium())
        testparcel.weight = 10
        self.assertFalse(testparcel.is_weight_not_too_low_for_medium())

    # test whether the weight is not above the maximum for a medium package(20 cm)
    def test_16_weight_is_not_too_high_for_medium(self):
        testparcel = Parcel(0, 0, 0, 0, 0, 0, 0)
        testparcel.weight = 20
        self.assertTrue(testparcel.is_weight_not_too_high_for_medium())
        testparcel.weight = 21
        self.assertFalse(testparcel.is_weight_not_too_high_for_medium())

    # test whether the weight is not below the minimum for a large package(21 cm)
    def test_17_weight_is_not_too_low_for_large(self):
        testparcel = Parcel(0, 0, 0, 0, 0, 0, 0)
        testparcel.weight = 21
        self.assertTrue(testparcel.is_weight_not_too_low_for_large())
        testparcel.weight = 20
        self.assertFalse(testparcel.is_weight_not_too_low_for_large())

    # test whether the weight is not above the maximum for a large package(30 cm)
    def test_18_weight_is_not_too_high_for_large(self):
        testparcel = Parcel(0, 0, 0, 0, 0, 0, 0)
        testparcel.weight = 30
        self.assertTrue(testparcel.is_weight_not_too_high_for_large())
        testparcel.weight = 31
        self.assertFalse(testparcel.is_weight_not_too_high_for_large())

    # test asserts price matches the expected value
    def test_19_right_price(self):
        testparcel = Parcel('V9A', 'H1Y', 50, 50, 50, 10, 'Regular')
        self.assertEqual(testparcel.verify(), 16.19)
        testparcel = Parcel('V9A', 'H1Y', 50, 50, 50, 15, 'Regular')
        self.assertEqual(testparcel.verify(), 17.23)
        testparcel = Parcel('V9A', 'H1Y', 50, 50, 50, 30, 'Regular')
        self.assertEqual(testparcel.verify(), 28.92)

        testparcel = Parcel('V9A', 'H1Y', 50, 50, 50, 10, 'Xpress')
        self.assertEqual(testparcel.verify(), 20.19)
        testparcel = Parcel('V9A', 'H1Y', 50, 50, 50, 15, 'Xpress')
        self.assertEqual(testparcel.verify(), 21.23)
        testparcel = Parcel('V9A', 'H1Y', 50, 50, 50, 30, 'Xpress')
        self.assertEqual(testparcel.verify(), 32.92)

        testparcel = Parcel('V9A', 'H1Y', 50, 50, 50, 10, 'Priority')
        self.assertEqual(testparcel.verify(), 36.19)
        testparcel = Parcel('V9A', 'H1Y', 50, 50, 50, 15, 'Priority')
        self.assertEqual(testparcel.verify(), 37.23)
        testparcel = Parcel('V9A', 'H1Y', 50, 50, 50, 30, 'Priority')
        self.assertEqual(testparcel.verify(), 48.92)

        testparcel = Parcel('V9A', 'H1Y', 2, 50, 50, 10, 'Regular')
        self.assertEqual(testparcel.verify(), -1)
        testparcel = Parcel('V9A', 'H1Y', 50, 300, 50, 15, 'Xpress')
        self.assertEqual(testparcel.verify(), -1)
        testparcel = Parcel('V9A', 'H1Y', 50, 50, 4684, 30, 'Priority')
        self.assertEqual(testparcel.verify(), -1)
        testparcel = Parcel('V9A', 'H1Y', 50, 50, 50, 0, 'Regular')
        self.assertEqual(testparcel.verify(), -1)
        testparcel = Parcel('V9A', 'H1Y', 50, 50, 50, 45, 'Regular')
        self.assertEqual(testparcel.verify(), -1)
        testparcel = Parcel('V9A', 'H1Y', 50, 50, 50, 30, 'dsf')
        self.assertEqual(testparcel.verify(), -1)

    # test asserts that rate mathes expected value
    def test_20_validate_rate(self):
        testparcel = Parcel('V9A','H1Y','Regular', 11, 8,100, 2)
        testparcel.from_pc_valid()
        self.assertEqual(1.619, float(testparcel.samefrom[0][11]))
        testparcel_2 = Parcel('V9A','H1Y','Regular',11, 8, 100, 13)
        testparcel_2.from_pc_valid()
        self.assertEqual(1.149, float(testparcel.samefrom[1][11]))
        testparcel_3 = Parcel('V9A', 'H1Y', 'Regular', 11, 8, 100, 22)
        testparcel_3.from_pc_valid()
        self.assertEqual(0.964, float(testparcel.samefrom[2][11]))

    # test whether the inputted from postal code has a postal code format
    def test_21_valid_form_of_from_postalcode(self):
        testparcel = Parcel('A0Z', 0, 0, 0, 0, 0, 0)
        self.assertTrue(testparcel.pc_valid_form(testparcel.from_pc))
        testparcel = Parcel('Home', 0, 0, 0, 0, 0, 0)
        self.assertFalse(testparcel.pc_valid_form(testparcel.from_pc))

    # test whether the inputted from postal code has a postal code format
    def test_22_valid_form_of_to_postalcode(self):
        testparcel = Parcel(0, 'Z1A', 0, 0, 0, 0, 0)
        self.assertTrue(testparcel.pc_valid_form(testparcel.to_pc))
        testparcel = Parcel(0, 'School', 0, 0, 0, 0, 0)
        self.assertFalse(testparcel.pc_valid_form(testparcel.to_pc))

    # test whether required values are numeric
    def test_23_valid_numeric_values(self):
        testparcel = Parcel('V0A', 'H1Y', 'not', 'a', 'number', 'yea', 'Regular')
        self.assertFalse(testparcel.numeric_entries_valid_form(testparcel.length))
        self.assertFalse(testparcel.numeric_entries_valid_form(testparcel.height))
        self.assertFalse(testparcel.numeric_entries_valid_form(testparcel.width))
        self.assertFalse(testparcel.numeric_entries_valid_form(testparcel.weight))


if __name__ == '__main__':
    unittest.main()
