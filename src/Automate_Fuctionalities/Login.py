from selenium import webdriver
from src.resources.Element_Location.Login_page import username_id,passsword_id,submit_id
from src.resources.Element_Location.Product_List_page import cart_symbol_class
import time
from selenium.webdriver.common.by import By
#Login
def login_using_chrome(username,password):
    driver=webdriver.Chrome()
    driver.get("https://www.saucedemo.com/")
    driver.maximize_window()
    try:
        driver.find_element(By.ID,username_id()).send_keys(username)
        driver.find_element(By.ID,passsword_id()).send_keys(password)
        driver.find_element(By.ID,submit_id()).click()
        time.sleep(5)
        if driver.current_url == "https://www.saucedemo.com/inventory.html":
            return True
        else:
            return False
    except ValueError:
        print("Element Not Found")



