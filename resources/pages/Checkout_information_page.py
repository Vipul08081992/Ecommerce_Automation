from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
class Checkout_information_page:
    def __init__(self,driver):
        self.driver=driver
    heading_locator=(By.XPATH,"//span[@class='title']")
    cancel_locator=(By.ID,"cancel")
    continue_locator=(By.ID,"continue")
    firstName_locator=(By.NAME,"firstName")
    lastName_locator=(By.NAME,"lastName")
    postalCode_locator=(By.NAME,"postalCode")
    error_message_locator=(By.XPATH,"//div[@class='error-message-container error']")
    error_close_button_locator=(By.XPATH,"//button[@class='error-button']")
#Get Element:
    def heading(self):
        return self.driver.find_element(*self.heading_locator)
    def cancel_button(self):
        return self.driver.find_element(*self.cancel_locator)
    def continue_button(self):
        return self.driver.find_element(*self.continue_locator)
    def firstName(self):
        return self.driver.find_element(*self.firstName_locator)
    def lastName(self):
        return self.driver.find_element(*self.lastName_locator)
    def postalCode(self):
        return self.driver.find_element(*self.postalCode_locator)
    def error_message(self):
        return self.driver.find_element(*self.error_message_locator)
    def error_close_button(self):
        return self.driver.find_element(*self.error_close_button_locator)
#Action on page:
    def back_to_cart(self):
        self.cancel_button().click()
    def open_overview_page(self,first,last,pincode):
        action=ActionChains(self.driver)
        action.click(self.firstName()).send_keys_to_element(self.firstName(),first).perform()
        action.click(self.lastName()).send_keys_to_element(self.lastName(),last).perform()
        action.click(self.postalCode()).send_keys_to_element(self.postalCode(),pincode).perform()
        self.continue_button().click()
    def error_message_text(self):
        return self.error_message().text
    def close_error_message(self):
        self.error_close_button().click()
