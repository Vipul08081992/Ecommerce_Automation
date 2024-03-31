from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
class Login_page:
    def __init__(self,driver):
        self.driver=driver
    heading_locator=(By.XPATH,"//div[@class='login_logo']")
    username_locator=(By.ID,"user-name")
    password_locator=(By.ID,"password")
    login_locator=(By.ID,"login-button")
    error_locator=(By.XPATH,"//div[@class='error-message-container error']")
    cross_button_of_error_locator=(By.XPATH,"//button[@class='error-button']")
#Get elements:
    def heading(self):
        return self.driver.find_element(*self.heading_locator)
    def username(self):
        return self.driver.find_element(*self.username_locator)
    def password(self):
        return self.driver.find_element(*self.password_locator)
    def login_button(self):
        return self.driver.find_element(*self.login_locator)
    def error(self):
        return self.driver.find_element(*self.error_locator)

    def cross_button_of_error(self):
        return self.driver.find_element(*self.cross_button_of_error_locator)
#Actions on page:
    def login(self,username,password):
        action=ActionChains(self.driver)
        action.click(self.username()).send_keys_to_element(self.username(),username).perform()
        action.click(self.password()).send_keys_to_element(self.password(),password).perform()
        self.login_button().click()

    def get_error_text(self):
        return self.error().text
    def click_on_error_cross_button(self):
        self.cross_button_of_error().click()
    def title_of_page(self):
        return self.driver.title



