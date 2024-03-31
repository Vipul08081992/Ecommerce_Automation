import pytest
from utils.Read_File import read_row_from_excel
from resources.pages.Login_page import Login_page
from resources.pages.Product_page import Product_page
from utils.waits import explicit_waits
from resources.constants.urls_of_page import product_page_url
# Test Login i.e open Product page:
@pytest.mark.parametrize("test_cred",read_row_from_excel("C:\\Users\\vipul\\PycharmProjects\\Swag_Labs\\resources\\Data\\Valid Credentials.xlsx",sheet_name="login_cred"))
def test_login_chrome(test_cred,open_login_page):
    username=test_cred["username"]
    password=test_cred["password"]
    driver=open_login_page
    loginpage=Login_page(driver)
    loginpage.login(username=username, password=password)
    productpage = Product_page(driver)
    explicit_waits(driver=driver, t_in_sec=10, element=productpage.heading())
    url=driver.current_url
    assert url == product_page_url()

# Verify Error Texts:
#TE-1: Username and password empty.
def test_TE_1(open_login_page):
    driver = open_login_page
    loginpage = Login_page(driver)
    loginpage.login(username="", password="")
    error_message=loginpage.get_error_text()
    assert error_message == "Epic sadface: Username is required"

#TE-2: Username empty.
def test_TE_2(open_login_page):
    driver = open_login_page
    loginpage = Login_page(driver)
    loginpage.login(username="", password="sauce_secret")
    error_message=loginpage.get_error_text()
    assert error_message == "Epic sadface: Username is required"

#TE-3: Password empty.
def test_TE_3(open_login_page):
    driver = open_login_page
    loginpage = Login_page(driver)
    loginpage.login(username="sauce_secret", password="")
    error_message=loginpage.get_error_text()
    assert error_message == "Epic sadface: Password is required"

#TE-4: Invalid Username and Password.
def test_TE_4(open_login_page):
    driver = open_login_page
    loginpage = Login_page(driver)
    loginpage.login(username="sauce_secret", password="sauce_secret")
    error_message=loginpage.get_error_text()
    assert error_message == "Epic sadface: Username and password do not match any user in this service"

#TE-5: User credentials are suspended:
def test_TE_5(open_login_page):
    driver = open_login_page
    loginpage = Login_page(driver)
    loginpage.login(username="locked_out_user", password="secret_sauce")
    error_message=loginpage.get_error_text()
    assert error_message == "Epic sadface: Sorry, this user has been locked out."

