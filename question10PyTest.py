import time

import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By

driver = None
def setup_module(module):
    global driver
    driver = webdriver.Chrome()
    driver.get("https://www.makemytrip.com/")
    driver.implicitly_wait(20)
    driver.maximize_window()


def teardown_module(module):
    driver.close()

def test_first():
    # Close the initial popup
    driver.find_element(By.CSS_SELECTOR, "span[data-cy='closeModal']").click()

    # Selecting From City
    driver.find_element(By.ID, "fromCity").click()
    driver.find_element(By.CSS_SELECTOR, "input[placeholder='From']").send_keys("HYD")
    driver.find_element(By.CSS_SELECTOR, "p[class*='searchedResult']").click()

    # Selecting To city
    driver.find_element(By.ID, "toCity").click()
    driver.find_element(By.CSS_SELECTOR, "input[placeholder='To']").send_keys("MAA")
    time.sleep(5)
    driver.find_element(By.XPATH, "//div[text()='MAA']").click()

    # Select from date
    driver.find_element(By.CSS_SELECTOR, "div[class*='DayPicker-Day'][aria-disabled='false']").click()

    # Select return date
    driver.find_element(By.CSS_SELECTOR, "p[data-cy='returnDefaultText']").click()
    driver.find_element(By.CSS_SELECTOR,
                        "div[class*='DayPicker-Day'][aria-disabled='false'][aria-selected='false']").click()

    # Click on search
    driver.find_element(By.LINK_TEXT, "SEARCH").click()

    # Wait for search results and dismiss popup
    time.sleep(5)
    driver.find_element(By.XPATH, "//button[text()='OKAY, GOT IT!']").click()

    # Get and assert the search result text
    search_result_text = driver.find_element(By.CSS_SELECTOR, "div[class='listingRhs']>p>span").text
    expected_text = "Flights from Hyderabad to Chennai, and back"

    assert search_result_text == expected_text, f"Expected '{expected_text}', but got '{search_result_text}'"
