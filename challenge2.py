#!/usr/bin/env python3

import time
import unittest
from selenium import webdriver
from selenium.webdriver.common.keys import Keys


class TestExotics(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Chrome("venv/chromedriver")

    def tearDown(self):
        self.driver.close()

    def test_exotics(self):
        self.driver.get("https://www.copart.com/")
        self.driver.find_element_by_id("input-search").click()
        self.driver.find_element_by_id("input-search").send_keys("exotics")
        self.driver.find_element_by_id("input-search").send_keys(Keys.ENTER)
        time.sleep(5)
        table = self.driver.find_element_by_id("serverSideDataTable")
        self.assertIn("PORSCHE", table.text)

if __name__ == '__main__':
    unittest.main()
