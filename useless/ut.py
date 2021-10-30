import zz
import unittest

class Test1(unittest.TestCase):
    @classmethod
    def setUpClass(self):
        print("start ut")

    @classmethod
    def tearDownClass(self):
        print("\nend of ut")

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def test_one(self):
        this_zz = zz.zz(1000)
        this_zz.equip_main_entrys(1, True, False)
        a = True
        a = a and this_zz.equip_1_sub_entry(1, 1, 1, 6)
        a = a and this_zz.equip_2_sub_entry(0, 1, 1, 6)
        a = a and this_zz.equip_3_sub_entry(1, 0, 1, 6)
        a = a and this_zz.equip_4_sub_entry(1, 1, 1, 6)
        a = a and this_zz.equip_5_sub_entry(1, 1, 0, 6)
        self.assertTrue(a)
        self.assertAlmostEqual(2.48, this_zz.get_crit_damage())

        this_zz = zz.zz(1000)
        this_zz.equip_main_entrys(1, False, True)
        a = True
        a = a and this_zz.equip_1_sub_entry(1, 1, 6, 1)
        a = a and this_zz.equip_2_sub_entry(0, 1, 6, 1)
        a = a and this_zz.equip_3_sub_entry(1, 0, 6, 1)
        a = a and this_zz.equip_4_sub_entry(1, 1, 6, 1)
        a = a and this_zz.equip_5_sub_entry(1, 3, 4, 0)
        self.assertTrue(a)
        self.assertAlmostEqual(0.974, this_zz.get_crit_rate())

    def test_two(self):
        this_zz = zz.zz(1000)
        this_zz.equip_main_entrys(1, True, False)
        a = True
        a = a and this_zz.equip_1_sub_entry(1, 1, 1, 7)
        a = a and this_zz.equip_2_sub_entry(0, 1, 1, 6)
        a = a and this_zz.equip_3_sub_entry(1, 0, 1, 6)
        a = a and this_zz.equip_4_sub_entry(1, 1, 1, 6)
        a = a and this_zz.equip_5_sub_entry(1, 1, 0, 6)
        self.assertFalse(a)

        this_zz = zz.zz(1000)
        this_zz.equip_main_entrys(1, True, False)
        a = this_zz.equip_1_sub_entry(1, 3, 3, 3)
        self.assertFalse(a)
        a = this_zz.equip_2_sub_entry(2, 2, 3, 3)
        self.assertFalse(a)
        a = this_zz.equip_3_sub_entry(4, 3, 1, 1)
        self.assertFalse(a)
        a = this_zz.equip_4_sub_entry(1, 3, 3, 3)
        self.assertFalse(a)
        a = this_zz.equip_5_sub_entry(1, 3, 3, 3)
        self.assertFalse(a)




# if __name__ == '__main__':
#     suite = unittest.TestSuite()
#     unittest.main()