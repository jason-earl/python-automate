#!/usr/bin/env python3

import os
import unittest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as ec
from selenium.webdriver.support.ui import WebDriverWait

class TestCategories(unittest.TestCase):

    def setUp(self):
        os.environ['MOZ_HEADLESS'] = '1'
        self.driver = webdriver.Firefox()
        self.driver.get("https://www.copart.com/")
        print("Waiting for page.")
        wait = WebDriverWait(self.driver, 20)
        wait.until(ec.visibility_of_element_located((By.XPATH, "//*[@id=\"tabTrending\"]//a")))
        print("done waiting.")
        trending = self.driver.find_element_by_id("tabTrending")
        self.links = trending.find_elements_by_tag_name("a")

    def tearDown(self):
        self.driver.close()
        self.driver.quit()

    def test_challenge3forloop(self):
        for link in self.links:
            href = link.get_attribute("href")
            if "make" in href:
                print("{} - {}".format(link.text, href))

    def test_challenge3while(self):
        num_links = len(self.links)
        i = 0
        while i < num_links:
            link = self.links[i]
            href = link.get_attribute("href")
            if "model" in href:
                print("{} - {}".format(link.text, href))
            i += 1

if __name__ == '__main__':
    unittest.main()
