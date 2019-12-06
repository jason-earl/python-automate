#!/usr/bin/env python3

import os
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait

def main():
    os.environ['MOZ_HEADLESS'] = '1'
    driver = webdriver.Firefox()
    driver.get("https://www.copart.com/")
    print("Waiting for page.")
    WebDriverWait(driver, 20).until(
        lambda x: x.find_element_by_xpath("//*[@id=\"tabTrending\"]//a"))
    print("done waiting.")
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
