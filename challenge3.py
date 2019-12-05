#!/usr/bin/env python3

import os
import time
from selenium import webdriver

def main():
    os.environ['MOZ_HEADLESS'] = '1'
    driver = webdriver.Firefox()
    driver.get("https://www.copart.com/")
    time.sleep(1)
    trending = driver.find_element_by_id("tabTrending")
    links = trending.find_elements_by_tag_name("a")
    for link in links:
        href = link.get_attribute("href")
        if "make" in href or "model" in href:
            print("{} - {}".format(link.text, href))
    driver.close()
    driver.quit()

if __name__ == '__main__':
    main()
