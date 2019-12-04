#!/usr/bin/env python3

import unittest
from Fib import fib

class FibTests(unittest.TestCase):

    def test_0(self):
        self.assertEqual(fib(0), 0)

    def test_1(self):
        self.assertEqual(fib(1), 1)

    def test_2(self):
        self.assertEqual(fib(2), 1)

    def test_3(self):
        self.assertEqual(fib(3), 2)

    def test_4(self):
        self.assertEqual(fib(4), 3)

    def test_5(self):
        self.assertEqual(fib(5), 5)

    def test_6(self):
        self.assertEqual(fib(6), 8)

    def test_7(self):
        self.assertEqual(fib(7), 13)

    def test_8(self):
        self.assertEqual(fib(8), 21)

    def test_9(self):
        self.assertEqual(fib(9), 34)

    def test_10(self):
        self.assertEqual(fib(10), 55)

    def test_11(self):
        self.assertEqual(fib(11), 89)

    def test_12(self):
        self.assertEqual(fib(12), 144)

    def test_13(self):
        self.assertEqual(fib(13), 233)

    def test_14(self):
        self.assertEqual(fib(14), 377)

    def test_15(self):
        self.assertEqual(fib(15), 610)

    def test_16(self):
        self.assertEqual(fib(16), 987)

    def test_17(self):
        self.assertEqual(fib(17), 1597)

    def test_18(self):
        self.assertEqual(fib(18), 2584)

    def test_19(self):
        self.assertEqual(fib(19), 4181)

    def test_20(self):
        self.assertEqual(fib(20), 6765)

if __name__ == '__main__':
    unittest.main()
