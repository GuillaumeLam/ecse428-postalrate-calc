import unittest
from parcel import Parcel


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

    def test_no_arguments(self):
        Parcel(0,0,0,0,0,0,0)

    def test_no_arguments_01(self):
        #self.assertRaises(Exception, method0())
        print("test 1")

    def test_too_few_arguments_02(self):
        #self.assertRaises(Exception, method1())
        print("test 2")

    def test_valid_from_postalcode_03(self):
        testparcel = Parcel('V9A',0,0,0,0,0,0)
        self.assertTrue(testparcel.from_pc_valid())
        print("test 3")

    def test_valid_to_postalcode_04(self):
         testparcel = Parcel(0,'H1Y',0,0,0,0,0)
         self.assertTrue(testparcel.from_pc_valid())

    def test_valid_shipment_type_05(self):
         testparcel = Parcel(0,0,0,0,0,0,'Regular')
         self.assertTrue(testparcel.is_postal_type_valid())

     def test_length_is_not_too_low_04(self):
         testparcel = Parcel(0,0,10,0,0,0,0)
         self.assertTrue(testparcel.length_is_not_too_low())
         testparcel = Parcel(0, 0, 9, 0, 0, 0, 0)
         self.assertFalse(testparcel.length_is_not_too_low())

    def test_length_is_not_too_high_05(self):
        testparcel = Parcel(0, 0, 210, 0, 0, 0, 0)
        self.assertTrue(testparcel.length_is_not_too_high())
        testparcel = Parcel(0, 0, 211, 0, 0, 0, 0)
        self.assertFalse(testparcel.length_is_not_too_high())

    def test_width_is_not_too_low_06(self):
         testparcel = Parcel(0, 0, 0, 7, 0, 0, 0)
         self.assertTrue(testparcel.width_is_not_too_low())
         testparcel = Parcel(0, 0, 0, 6, 0, 0, 0)
         self.assertFalse(testparcel.width_is_not_too_low())

    def test_width_is_not_too_high_05(self):
        testparcel = Parcel(0, 0, 0, 275, 0, 0, 0)
        self.assertTrue(testparcel.width_is_not_too_high())
        testparcel = Parcel(0, 0, 0, 276, 0, 0, 0)
        self.assertFalse(testparcel.width_is_not_too_high())

    def test_height_is_not_too_low_06(self):
        testparcel = Parcel(0, 0, 0, 0, 1, 0, 0)
        self.assertTrue(testparcel.width_is_not_too_low())
        testparcel = Parcel(0, 0, 0, 0, 0, 0, 0)
        self.assertFalse(testparcel.width_is_not_too_low())

    def test_height_is_not_too_high_05(self):
        testparcel = Parcel(0, 0, 0, 0, 210, 0, 0)
        self.assertTrue(testparcel.width_is_not_too_high())
        testparcel = Parcel(0, 0, 0, 0, 211, 0, 0)
        self.assertFalse(testparcel.width_is_not_too_high())


     def test_weight_is_not_too_low_for_regular_10(self):
        testparcel = Parcel(0, 0, 0, 0, 0, 0 , 0)
        self.assertTrue(testparcel.is_weight_not_too_low_for_regular())
        testparcel = Parcel(0, 0, 0, 0, 0, -1, 0)
        self.assertFalse(testparcel.is_weight_not_too_low_for_regular())

    def test_weight_is_not_too_high_for_regular_10(self):
        testparcel = Parcel(0, 0, 0, 0, 0, 10, 0)
        self.assertTrue(testparcel.is_weight_not_too_high_for_regular())
        testparcel = Parcel(0, 0, 0, 0, 0, 11, 0)
        self.assertFalse(testparcel.is_weight_not_too_high_for_regular())

    def test_weight_is_not_too_low_for_priority_10(self):
        testparcel = Parcel(0, 0, 0, 0, 0, 11, 0)
        self.assertTrue(testparcel.is_weight_not_too_low_for_priority())
        testparcel = Parcel(0, 0, 0, 0, 0, 10, 0)
        self.assertFalse(testparcel.is_weight_not_too_low_for_priority())


    def test_weight_is_not_too_high_for_priority_10(self):
        testparcel = Parcel(0, 0, 0, 0, 0, 20, 0)
        self.assertTrue(testparcel.is_weight_not_too_high_for_priority())
        testparcel = Parcel(0, 0, 0, 0, 0, 21, 0)
        self.assertFalse(testparcel.is_weight_not_too_high_for_priority())

    def test_weight_is_not_too_low_for_xpress_10(self):
        testparcel = Parcel(0, 0, 0, 0, 0, 21, 0)
        self.assertTrue(testparcel.is_weight_not_too_low_for_xpress())
        testparcel = Parcel(0, 0, 0, 0, 0, 20, 0)
        self.assertFalse(testparcel.is_weight_not_too_low_for_xpress())

    def test_weight_is_not_too_high_for_xpress_10(self):
        testparcel = Parcel(0, 0, 0, 0, 0, 30, 0)
        self.assertTrue(testparcel.is_weight_not_too_high_for_xpress())
        testparcel = Parcel(0, 0, 0, 0, 0, 31, 0)
        self.assertFalse(testparcel.is_weight_not_too_high_for_xpress())


    #
    # def test_rate_validity_10(self):


if __name__ == '__main__':
    unittest.main()
