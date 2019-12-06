#!/usr/bin/env python3

import os
import unittest
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait


class TestExotics(unittest.TestCase):
    def setUp(self):
        os.environ['MOZ_HEADLESS'] = '1'
        self.driver = webdriver.Firefox()

    def tearDown(self):
        self.driver.close()
        self.driver.quit()

    def test_exotics(self):
        self.driver.get("https://www.copart.com/")
        input_search = self.driver.find_element_by_id("input-search")
        input_search.click()
        input_search.send_keys("exotics")
        input_search.send_keys(Keys.ENTER)
        WebDriverWait(self.driver, 20).until(
            lambda x: x.find_element_by_xpath("//*[@id=\"serverSideDataTable\"]//td").is_displayed())
        table = self.driver.find_element_by_id("serverSideDataTable")
        self.assertIn("PORSCHE", table.text)

if __name__ == '__main__':
    unittest.main()
