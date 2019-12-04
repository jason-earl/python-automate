#!/usr/bin/env python3

import unittest
from EnglishNumber import int_to_english

class EnglishNumberTests(unittest.TestCase):

    def test_zero(self):
        self.assertEqual(int_to_english(0), 'zero')

    def test_one(self):
        self.assertEqual(int_to_english(1), 'one')

    def test_two(self):
        self.assertEqual(int_to_english(2), 'two')

    def test_three(self):
        self.assertEqual(int_to_english(3), 'three')

    def test_four(self):
        self.assertEqual(int_to_english(4), 'four')

    def test_five(self):
        self.assertEqual(int_to_english(5), 'five')

    def test_six(self):
        self.assertEqual(int_to_english(6), 'six')

    def test_seven(self):
        self.assertEqual(int_to_english(7), 'seven')

    def test_eight(self):
        self.assertEqual(int_to_english(8), 'eight')

    def test_nine(self):
        self.assertEqual(int_to_english(9), 'nine')

    def test_ten(self):
        self.assertEqual(int_to_english(10), 'ten')

    def test_eleven(self):
        self.assertEqual(int_to_english(11), 'eleven')

    def test_twelve(self):
        self.assertEqual(int_to_english(12), 'twelve')

    def test_thirteen(self):
        self.assertEqual(int_to_english(13), 'thirteen')

    def test_fourteen(self):
        self.assertEqual(int_to_english(14), 'fourteen')

    def test_fifteen(self):
        self.assertEqual(int_to_english(15), 'fifteen')

    def test_sixteen(self):
        self.assertEqual(int_to_english(16), 'sixteen')

    def test_seventeen(self):
        self.assertEqual(int_to_english(17), 'seventeen')

    def test_eighteen(self):
        self.assertEqual(int_to_english(18), 'eighteen')

    def test_nineteen(self):
        self.assertEqual(int_to_english(19), 'nineteen')

    def test_twenty(self):
        self.assertEqual(int_to_english(20), 'twenty')

    def test_twenty_one(self):
        self.assertEqual(int_to_english(21), 'twenty one')

    def test_thirty(self):
        self.assertEqual(int_to_english(30), 'thirty')

    def test_thirty_one(self):
        self.assertEqual(int_to_english(31), 'thirty one')

    def test_forty(self):
        self.assertEqual(int_to_english(40), 'forty')

    def test_forty_one(self):
        self.assertEqual(int_to_english(41), 'forty one')

    def test_fifty(self):
        self.assertEqual(int_to_english(50), 'fifty')

    def test_fity_one(self):
        self.assertEqual(int_to_english(51), 'fifty one')

    def test_sixty(self):
        self.assertEqual(int_to_english(60), 'sixty')

    def test_sixty_one(self):
        self.assertEqual(int_to_english(61), 'sixty one')

    def test_seventy(self):
        self.assertEqual(int_to_english(70), 'seventy')

    def test_seventy_one(self):
        self.assertEqual(int_to_english(71), 'seventy one')

    def test_eighty(self):
        self.assertEqual(int_to_english(80), 'eighty')

    def test_eighty_one(self):
        self.assertEqual(int_to_english(81), 'eighty one')

    def test_ninety(self):
        self.assertEqual(int_to_english(90), 'ninety')

    def test_ninety_one(self):
        self.assertEqual(int_to_english(91), 'ninety one')

    def test_one_hundred(self):
        self.assertEqual(int_to_english(100), 'one hundred')

    def test_one_hundred_one(self):
        self.assertEqual(int_to_english(101), 'one hundred one')

    def test_one_hundred_ten(self):
        self.assertEqual(int_to_english(110), 'one hundred ten')

    def test_one_hundred_eleven(self):
        self.assertEqual(int_to_english(111), 'one hundred eleven')

    def test_one_hundred_forty_four(self):
        self.assertEqual(int_to_english(144), 'one hundred forty four')

    def test_one_thousand(self):
        self.assertEqual(int_to_english(1000), 'one thousand')

    def test_seven_thousand_four_hundred_eight(self):
        self.assertEqual(int_to_english(7408), 'seven thousand four hundred eight')

    def test_nine_thousand_nine_hundred_ninety_nine(self):
        self.assertEqual(int_to_english(9999), 'nine thousand nine hundred ninety nine')

    def test_really_big_number(self):
        self.assertEqual(int_to_english(12111111111),
                         'twelve billion one hundred eleven million one hundred eleven thousand one hundred eleven')

if __name__ == '__main__':
    unittest.main()
