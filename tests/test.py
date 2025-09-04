import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By

def test_open_google():
    # Start Chrome (make sure chromedriver.exe is in PATH)
    driver = webdriver.Chrome()
    driver.get("https://www.google.com")

    # Verify page title contains 'Google'
    assert "Google" in driver.title

    driver.quit()
