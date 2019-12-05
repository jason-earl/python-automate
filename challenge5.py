#!/usr/bin/env python3

import os
import time
from collections import defaultdict
from selenium import webdriver
from selenium.webdriver.common.keys import Keys

def main():
    models = defaultdict(int)
    #os.environ['MOZ_HEADLESS'] = '1'
    driver = webdriver.Firefox()
    driver.get("https://www.copart.com/")
    driver.find_element_by_id("input-search").click()
    driver.find_element_by_id("input-search").send_keys("porsche")
    driver.find_element_by_id("input-search").send_keys(Keys.ENTER)
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
    rear_end = 0
    front_end = 0
    minor_dent = 0
    under_carriage = 0
    misc = 0
    for span in spans:
        if span.get_attribute('data-uname') == 'lotsearchLotdamagedescription':
            # These if statements are a waste of time.  I should do
            # this like I did models.
            if span.text == 'REAR END':
                rear_end += 1
            elif span.text == 'FRONT END':
                front_end += 1
            elif span.text == 'MINOR DENT/SCRATCHES':
                minor_dent += 1
            elif span.text == 'UNDERCARRIAGE':
                under_carriage += 1
            else:
                misc += 1
    print("********************DAMAGE********************")
    print("REAR END: ", rear_end)
    print("FRONT END: ", front_end)
    print("MINOR DENT/SCRATCHES: ", minor_dent)
    print("UNDERCARRIAGE: ", under_carriage)
    print("MISC: ", misc)
    driver.close()
    driver.quit()

if __name__ == '__main__':
    main()
