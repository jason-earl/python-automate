#!/usr/bin/env python3

import os
import time
from collections import defaultdict
from selenium import webdriver
from selenium.webdriver.common.keys import Keys

DAMAGE_TYPES = {'REAR END': 0,
                'FRONT END': 1,
                'MINOR DENT/SCRATCHES': 2,
                'UNDERCARRIAGE': 3,
                'MISC': 4}

def main():
    models = defaultdict(int)
    os.environ['MOZ_HEADLESS'] = '1'
    driver = webdriver.Firefox()
    driver.get("https://www.copart.com/")
    driver.find_element_by_id("input-search").click()
    driver.find_element_by_id("input-search").send_keys("porsche")
    driver.find_element_by_id("input-search").send_keys(Keys.ENTER)
    # Gecko likes a click as well
    search_form = driver.find_element_by_id("search-form")
    buttons = search_form.find_elements_by_tag_name("button")
    for button in buttons:
        if "Search" in button.text:
            button.click()
    time.sleep(10)
    dropdown = driver.find_element_by_name("serverSideDataTable_length")
    dropdown.find_element_by_xpath("//option[. = '100']").click()
    time.sleep(5)
    table = driver.find_element_by_id("serverSideDataTable")
    spans = table.find_elements_by_tag_name("span")
    for span in spans:
        if span.get_attribute('data-uname') =='lotsearchLotmodel':
            models[span.text] += 1
    print("********************MODELS********************")
    # print Models (sorted)
    for key, val in sorted(models.items()):
        print("{}: {}".format(key, val))
    damage_totals = defaultdict(int)
    for span in spans:
        if span.get_attribute('data-uname') == 'lotsearchLotdamagedescription':
            damage_type = DAMAGE_TYPES.get(span.text, 4)
            damage_totals[damage_type] += 1
    print("********************DAMAGE********************")
    for damage_type in DAMAGE_TYPES:
        print("{}: {}".format(damage_type, damage_totals[DAMAGE_TYPES[damage_type]]))
    driver.close()
    driver.quit()

if __name__ == '__main__':
    main()
