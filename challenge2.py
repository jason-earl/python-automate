#!/usr/bin/env python3

import os
import unittest
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as ec
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
        wait = WebDriverWait(self.driver, 20)
        wait.until(ec.visibility_of_element_located((By.XPATH, "//*[@id=\"serverSideDataTable\"]//td")))
        table = self.driver.find_element_by_id("serverSideDataTable")
        self.assertIn("PORSCHE", table.text)

if __name__ == '__main__':
    unittest.main()
