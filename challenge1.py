#!/usr/bin/env python3

import os
import unittest
from selenium import webdriver

class Challenge1(unittest.TestCase):

    def setUp(self):
        os.environ['MOZ_HEADLESS'] = '1'
        self.driver = webdriver.Firefox()

    def tearDown(self):
        self.driver.close()
        self.driver.quit()

    def test_challenge1(self):
        self.driver.get("https://www.google.com")
        self.assertIn("Google", self.driver.title)


if __name__ == '__main__':
    unittest.main()
