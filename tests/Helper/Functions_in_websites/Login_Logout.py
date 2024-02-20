from selenium import webdriver
from selenium.webdriver.support.wait import WebDriverWait
from tests.resourses.Element_Location.Login_page import heading
from tests.resourses.Element_Location.Login_page import username_id,passsword_id,submit_id
from tests.resourses.Element_Location.Product_List_page import Product_Page,Side_menu
from tests.resourses.Element_Location.URLs_of_Website import login_page_url
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from tests.utils.Read_Data import read_data_of_cell


def login_account_chrome():
    username = read_data_of_cell('/src/resources/Data/Valid Credentials.xlsx', 2, 2)
    password = read_data_of_cell('/src/resources/Data/Valid Credentials.xlsx', 2, 3)
    driver=webdriver.Chrome()
    driver.get(login_page_url())
    driver.maximize_window()
    driver.find_element(By.ID,username_id()).send_keys(username)
    driver.find_element(By.ID,passsword_id()).send_keys(password)
    driver.find_element(By.ID,submit_id()).click()
    WebDriverWait(driver, 5).until(
        EC.presence_of_element_located((By.XPATH, Product_Page.heading_prodouct())))
    return driver

def logout_chrome(side_menu):
    driver=side_menu
    driver.find_element(By.ID,Product_Page.menu_button_id()).click()
    WebDriverWait(driver, 5).until(
        EC.presence_of_element_located((By.ID,Side_menu.reset_app_state_id())))
    driver.find_element(By.ID,Side_menu.reset_app_state_id()).click()
    driver.find_element(By.ID,Side_menu.logout_id()).click()
    WebDriverWait(driver, 5).until(
        EC.presence_of_element_located((By.ID,heading())))

