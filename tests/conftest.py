import pytest
from selenium import webdriver
from resources.constants.urls_of_page import login_page_url
from resources.pages.Login_page import Login_page
from resources.pages.Product_page import Product_page
from utils.waits import explicit_waits

@pytest.fixture()
def open_login_page():
    driver=webdriver.Chrome()
    driver.get(login_page_url())
    driver.maximize_window()
    yield driver
    driver.quit()

@pytest.fixture()
def open_product_page(open_login_page):
    driver=open_login_page
    loginpage=Login_page(driver)
    loginpage.login(username='standard_user',password='secret_sauce')
    productpage=Product_page(driver)
    explicit_waits(driver=driver,t_in_sec=10,element=productpage.heading())
    return driver

