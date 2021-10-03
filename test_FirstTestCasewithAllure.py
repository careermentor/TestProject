from selenium.webdriver import Chrome
import pytest
import allure

def test_login():
    path = "D:\\Selenium_Python\\chromedriver_win32\\chromedriver.exe"
    driver = Chrome(executable_path=path)
    driver.get("https://www.facebook.com/")
    driver.maximize_window()