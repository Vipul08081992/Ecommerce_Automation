from selenium.webdriver.common.by import By
class Checkout_complete:
    def __init__(self,driver):
        self.driver=driver
    heading_locator=(By.XPATH,"//span[@class='title']")
    center_text_locator=(By.XPATH,"//h2[@class='complete-header']")
    back_home_locator=(By.NAME,"back-to-products")
#Get Element:
    def heading(self):
        return self.driver.find_element(*self.heading_locator)
    def center_text(self):
        return self.driver.find_element(*self.center_text_locator)
    def back_home_button(self):
        return self.driver.find_element(*self.back_home_locator)
#Action:
    def heading_text(self):
        return self.heading().text
    def center_message(self):
        return self.center_text().text
    def back_to_product_page(self):
        self.back_home_button().click()