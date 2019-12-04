#!/usr/bin/env python3

import time
from selenium import webdriver


def main():
    driver = webdriver.Chrome("venv/chromedriver")
    driver.get("https://www.copart.com/")
    time.sleep(1)
    trending = driver.find_element_by_id("tabTrending")
    links = trending.find_elements_by_tag_name("a")
    for link in links:
        href = link.get_attribute("href")
        if "make" in href or "model" in href:
            print("{} - {}".format(link.text, href))
    driver.close()

if __name__ == '__main__':
    main()
