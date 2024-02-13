from selenium import webdriver
from src.resources.Element_Location.Login_page import username_id,passsword_id,submit_id
import time
from selenium.webdriver.common.by import By
#Login
def login_using_chrome(username,password):
    driver=webdriver.Chrome()
    driver.get("https://www.saucedemo.com/")
    driver.maximize_window()

    driver.find_element(By.ID,username_id()).send_keys(username)
    driver.find_element(By.ID,passsword_id()).send_keys(password)
    driver.find_element(By.ID,submit_id()).click()
    time.sleep(5)


login_using_chrome()
