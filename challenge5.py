#!/usr/bin/env python3

import os
from collections import defaultdict
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support import expected_conditions as ec
from selenium.webdriver.support.ui import WebDriverWait

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
    input_search = driver.find_element_by_id("input-search")
    input_search.click()
    input_search.send_keys("porsche")
    input_search.send_keys(Keys.ENTER)
    # Gecko likes a click as well
    search_form = driver.find_element_by_id("search-form")
    buttons = search_form.find_elements_by_tag_name("button")
    for button in buttons:
        if "Search" in button.text:
            button.click()
    print("Waitng for search results")
    wait = WebDriverWait(driver, 20)
    wait.until(ec.visibility_of_element_located((By.XPATH, "//*[@id=\"serverSideDataTable\"]//td")))
    print("done waiting for search results")
    dropdown = driver.find_element_by_name("serverSideDataTable_length")
    dropdown.find_element_by_xpath("//option[. = '100']").click()
    print("Switching to 100 entries.")
    wait = WebDriverWait(driver, 20)
    wait.until(ec.visibility_of_element_located(
        (By.XPATH, "//*[@id=\"serverSideDataTable\"]//tr[100]/td[1]")))
    print("Done switching to 100 entries.")
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
