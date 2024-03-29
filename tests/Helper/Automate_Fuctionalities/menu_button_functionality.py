import time

from selenium.webdriver.common.by import By
from tests.resourses.Element_Location.Product_List_page import Product_Page,Side_menu
from tests.Helper.Functions_in_websites.Login_Logout import login_account_chrome
from tests.utils.Read_Data import read_data_of_cell


#1.When no Product Added
def menu_button_no_product_add():
    username = read_data_of_cell(
        '/src/resources/Data/Valid Credentials.xlsx', 2, 2)
    password = read_data_of_cell(
        '/src/resources/Data/Valid Credentials.xlsx', 2, 3)
    pro_page=login_account_chrome(username=username, password=password)
    try:
        pro_page.find_element(By.ID,Product_Page.menu_button_id()).click()
        time.sleep(5)
        return pro_page.find_element(By.ID,Side_menu.all_item_id()).is_displayed()

    except ValueError:
        print("Element Not Found")

#2.Product are added
def menu_button_product_add():
    username = read_data_of_cell(
        '/src/resources/Data/Valid Credentials.xlsx', 2, 2)
    password = read_data_of_cell(
        '/src/resources/Data/Valid Credentials.xlsx', 2, 3)
    pro_page = login_account_chrome(username=username, password=password)
    items_to_add = pro_page.find_elements(By.XPATH, Product_Page.add_to_cart_button_xpath())
    try:
        for i in (1,4):
            items_to_add[i].click()
        pro_page.find_element(By.ID,Product_Page.menu_button_id()).click()
        time.sleep(5)
        return pro_page.find_element(By.ID,Side_menu.all_item_id()).is_displayed()
    except ValueError:
        print("Element Not Found")

#3.Add all the products availlable
def menu_button_product_all_add():
    username = read_data_of_cell(
        '/src/resources/Data/Valid Credentials.xlsx', 2, 2)
    password = read_data_of_cell(
        '/src/resources/Data/Valid Credentials.xlsx', 2, 3)
    pro_page = login_account_chrome(username=username, password=password)
    try:
        items_to_add = pro_page.find_elements(By.XPATH, Product_Page.add_to_cart_button_xpath())
        for i in range(len(items_to_add)):
            items_to_add[i].click()
        pro_page.find_element(By.ID, Product_Page.menu_button_id()).click()
        time.sleep(5)
        return pro_page.find_element(By.ID,Side_menu.all_item_id()).is_displayed()
    except ValueError:
        print("Element Not Found")

#4.Remove some of added products
def menu_button_product_add_remove_some():
    username = read_data_of_cell(
        '/src/resources/Data/Valid Credentials.xlsx', 2, 2)
    password = read_data_of_cell(
        '/src/resources/Data/Valid Credentials.xlsx', 2, 3)
    pro_page = login_account_chrome(username=username, password=password)
    try:
        items_to_add = pro_page.find_elements(By.XPATH, Product_Page.add_to_cart_button_xpath())
        for i in (1,3,4,2):
            items_to_add[i].click()
        items_to_remove=pro_page.find_elements(By.XPATH,Product_Page.remove_from_cart_button_xpath())
        for i in (1,3):
            items_to_remove[i].click()
        pro_page.find_element(By.ID, Product_Page.menu_button_id()).click()
        time.sleep(5)
        return pro_page.find_element(By.ID,Side_menu.all_item_id()).is_displayed()
    except ValueError:
        print("Element Not Found")

#5.Remove all selected items selected
def menu_button_product_add_remove_all():
    username = read_data_of_cell(
        '/src/resources/Data/Valid Credentials.xlsx', 2, 2)
    password = read_data_of_cell(
        '/src/resources/Data/Valid Credentials.xlsx', 2, 3)
    pro_page = login_account_chrome(username=username, password=password)
    try:
        items_to_add = pro_page.find_elements(By.XPATH, Product_Page.add_to_cart_button_xpath())
        for i in (1, 3, 4, 2):
            items_to_add[i].click()
        items_to_remove = pro_page.find_elements(By.XPATH, Product_Page.remove_from_cart_button_xpath())
        for i in range(len(items_to_remove)):
            items_to_remove[i].click()
        pro_page.find_element(By.ID, Product_Page.menu_button_id()).click()
        time.sleep(5)
        return pro_page.find_element(By.ID,Side_menu.all_item_id()).is_displayed()
    except ValueError:
        print("Element Not Found")

#6.Add all products available and then remove them all
def menu_button_product_add_all_remove_all():
    username = read_data_of_cell(
        '/src/resources/Data/Valid Credentials.xlsx', 2, 2)
    password = read_data_of_cell(
        '/src/resources/Data/Valid Credentials.xlsx', 2, 3)
    pro_page = login_account_chrome(username=username, password=password)
    try:
        items_to_add = pro_page.find_elements(By.XPATH, Product_Page.add_to_cart_button_xpath())
        for i in range(len(items_to_add)):
            items_to_add[i].click()
        items_to_remove = pro_page.find_elements(By.XPATH, Product_Page.remove_from_cart_button_xpath())
        for i in range(len(items_to_remove)):
            items_to_remove[i].click()
        pro_page.find_element(By.ID, Product_Page.menu_button_id()).click()
        time.sleep(5)
        return pro_page.find_element(By.ID,Side_menu.all_item_id()).is_displayed()
    except ValueError:
            print("Element Not Found")


