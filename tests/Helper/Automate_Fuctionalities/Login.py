from selenium import webdriver
from tests.resourses.Element_Location.Login_page import username_id,passsword_id,submit_id
from tests.resourses.Element_Location.URLs_of_Website import login_page_url,product_page_url
from tests.resourses.Element_Location.Product_List_page import Product_Page
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
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
        WebDriverWait(driver, 5).until(
            EC.presence_of_element_located((By.XPATH,Product_Page.heading_prodouct())))
        if driver.current_url == product_page_url():
            return True
        else:
            return False
    except ValueError:
        print("Element Not Found")







