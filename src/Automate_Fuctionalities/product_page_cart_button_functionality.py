import time

from selenium.webdriver.common.by import By
from src.resources.Element_Location.Product_List_page import Product_Page
from src.Automate_Fuctionalities.Login import login_account_chrome
from src.resources.Element_Location.URLs_of_Website import cart_page_url
from src.utils.Read_Data import read_data_of_cell

#When no Product Added
def cart_button_no_product_add():
    username = read_data_of_cell(
        'C:\\Users\\vipul\\PycharmProjects\\Swag_Labs\\src\\resources\\Data\\Valid Credentials.xlsx', 2, 2)
    password = read_data_of_cell(
        'C:\\Users\\vipul\\PycharmProjects\\Swag_Labs\\src\\resources\\Data\\Valid Credentials.xlsx', 2, 3)
    pro_page=login_account_chrome(username=username, password=password)
    try:
        pro_page.find_element(By.CLASS_NAME,Product_Page.cart_symbol_class()).click()
        time.sleep(5)
        if pro_page.current_url == cart_page_url():
            print(cart_page_url())
            return True
        else:
            return False

    except ValueError:
        print("Element Not Found")

# Product are added
def cart_button_product_add():
    username = read_data_of_cell(
        'C:\\Users\\vipul\\PycharmProjects\\Swag_Labs\\src\\resources\\Data\\Valid Credentials.xlsx', 2, 2)
    password = read_data_of_cell(
        'C:\\Users\\vipul\\PycharmProjects\\Swag_Labs\\src\\resources\\Data\\Valid Credentials.xlsx', 2, 3)
    pro_page = login_account_chrome(username=username, password=password)
    try:
        for i in (1,4):
            pro_page.find_element(By.XPATH,Product_Page.add_to_cart_button_xpath(i)).click()

        pro_page.find_element(By.CLASS_NAME, Product_Page.cart_symbol_class()).click()
        if pro_page.current_url == cart_page_url():
            return True
        else:
            return False

    except ValueError:
        print("Element Not Found")

#Add all the products availlable
def cart_button_product_all_add():
    username = read_data_of_cell(
        'C:\\Users\\vipul\\PycharmProjects\\Swag_Labs\\src\\resources\\Data\\Valid Credentials.xlsx', 2, 2)
    password = read_data_of_cell(
        'C:\\Users\\vipul\\PycharmProjects\\Swag_Labs\\src\\resources\\Data\\Valid Credentials.xlsx', 2, 3)
    pro_page = login_account_chrome(username=username, password=password)
    try:
        for i in range(1,7):
            pro_page.find_element(By.XPATH,Product_Page.add_to_cart_button_xpath(i)).click()

        pro_page.find_element(By.CLASS_NAME, Product_Page.cart_symbol_class()).click()
        if pro_page.current_url == cart_page_url():
            return True
        else:
            return False

    except ValueError:
        print("Element Not Found")

#Remove some of added products
def cart_button_product_add_remove_some():
    username = read_data_of_cell(
        'C:\\Users\\vipul\\PycharmProjects\\Swag_Labs\\src\\resources\\Data\\Valid Credentials.xlsx', 2, 2)
    password = read_data_of_cell(
        'C:\\Users\\vipul\\PycharmProjects\\Swag_Labs\\src\\resources\\Data\\Valid Credentials.xlsx', 2, 3)
    pro_page = login_account_chrome(username=username, password=password)
    try:
        for i in (1,3,4,2):
            pro_page.find_element(By.XPATH,Product_Page.add_to_cart_button_xpath(i=i)).click()
        for i in (3,2):
            pro_page.find_element(By.XPATH,Product_Page.add_to_cart_button_xpath(i=i)).click()
        pro_page.find_element(By.CLASS_NAME, Product_Page.cart_symbol_class()).click()
        if pro_page.current_url == cart_page_url():
            return True
        else:
            return False

    except ValueError:
        print("Element Not Found")

#Remove all selected items selected
def cart_button_product_add_remove_all():
    username = read_data_of_cell(
        'C:\\Users\\vipul\\PycharmProjects\\Swag_Labs\\src\\resources\\Data\\Valid Credentials.xlsx', 2, 2)
    password = read_data_of_cell(
        'C:\\Users\\vipul\\PycharmProjects\\Swag_Labs\\src\\resources\\Data\\Valid Credentials.xlsx', 2, 3)
    pro_page = login_account_chrome(username=username, password=password)
    try:
        for i in (1,3,4,2):
            pro_page.find_element(By.XPATH,Product_Page.add_to_cart_button_xpath(i=i)).click()
        for i in (1,3,2,4):
            pro_page.find_element(By.XPATH,Product_Page.add_to_cart_button_xpath(i=i)).click()
        pro_page.find_element(By.CLASS_NAME, Product_Page.cart_symbol_class()).click()
        if pro_page.current_url == cart_page_url():
            return True
        else:
            return False

    except ValueError:
        print("Element Not Found")

#Add all products availlable and then remove them all
    def cart_button_product_add_all_remove_all():
        username = read_data_of_cell(
            'C:\\Users\\vipul\\PycharmProjects\\Swag_Labs\\src\\resources\\Data\\Valid Credentials.xlsx', 2, 2)
        password = read_data_of_cell(
            'C:\\Users\\vipul\\PycharmProjects\\Swag_Labs\\src\\resources\\Data\\Valid Credentials.xlsx', 2, 3)
        pro_page = login_account_chrome(username=username, password=password)
        try:
            for i in range(1,7):
                pro_page.find_element(By.XPATH, Product_Page.add_to_cart_button_xpath(i=i)).click()
            for i in range(1,7):
                pro_page.find_element(By.XPATH, Product_Page.add_to_cart_button_xpath(i=i)).click()
            pro_page.find_element(By.CLASS_NAME, Product_Page.cart_symbol_class()).click()
            if pro_page.current_url == cart_page_url():
                return True
            else:
                return False

        except ValueError:
            print("Element Not Found")