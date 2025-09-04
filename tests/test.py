from selenium import webdriver

def test_google_homepage():
    driver = webdriver.Chrome()
    driver.get("https://www.google.com")
    assert "Google" in driver.title
    driver.quit()