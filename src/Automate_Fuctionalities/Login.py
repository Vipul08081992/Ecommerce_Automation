from selenium import webdriver
from src.resources.Element_Location.Login_page import username_id,passsword_id,submit_id
from src.resources.Element_Location.URLs_of_Website import login_page_url,product_page_url
import time
from selenium.webdriver.common.by import By
#Login
def login_using_chrome(username,password):
    driver=webdriver.Chrome()
    driver.get(login_page_url())
    driver.maximize_window()
    try:
        driver.find_element(By.ID,username_id()).send_keys(username)
        driver.find_element(By.ID,passsword_id()).send_keys(password)
        driver.find_element(By.ID,submit_id()).click()
        time.sleep(5)
        if driver.current_url == product_page_url():
            return True
        else:
            return False
    except ValueError:
        print("Element Not Found")


def login_account_chrome(username,password):
    driver=webdriver.Chrome()
    driver.get(login_page_url())
    driver.maximize_window()
    driver.find_element(By.ID,username_id()).send_keys(username)
    driver.find_element(By.ID,passsword_id()).send_keys(password)
    driver.find_element(By.ID,submit_id()).click()
    time.sleep(5)
    return driver




