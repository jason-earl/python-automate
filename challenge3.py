#!/usr/bin/env python3

import time
import unittest
from selenium import webdriver


class TestExotics(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Chrome("venv/chromedriver")

    def tearDown(self):
        self.driver.close()

    def test_popular_models(self):
        self.driver.get("https://www.copart.com/")
        time.sleep(1)
        trending = self.driver.find_element_by_id("tabTrending")
        links = trending.find_elements_by_tag_name("a")
        for link in links:
            href = link.get_attribute("href")
            if "make" in href or "model" in href:
                print("{} - {}".format(link.text, href))

if __name__ == '__main__':
    unittest.main()
