from selenium.webdriver.common.by import By

from utils.Check_element_presence import is_element_present


class Product_detail:
    def __init__(self,driver):
        self.driver=driver
    back_to_product_locator=(By.NAME,"back-to-products")
    product_name_locator=(By.XPATH,"//div[@class='inventory_details_name large_size']")
    product_price_locator=(By.XPATH,"//div[@class='inventory_details_price']")
    add_to_cart_button_locator=(By.ID,"add-to-cart")
    remove_button_locator=(By.ID,"remove")
    cart_symbol_locator=(By.ID,"shopping_cart_container")
    number_of_item_locator=(By.XPATH,"//span[@class='shopping_cart_badge']")
# Get Elements:
    def back_to_product_button(self):
        return self.driver.find_element(*self.back_to_product_locator)
    def product_name(self):
        return self.driver.find_element(*self.product_name_locator)
    def product_price(self):
        return self.driver.find_element(*self.product_price_locator)
    def add_to_cart_button(self):
        return self.driver.find_element(*self.add_to_cart_button_locator)
    def remove_button(self):
        return self.driver.find_element(*self.remove_button_locator)
    def cart_symbol(self):
        return self.driver.find_element(*self.cart_symbol_locator)
    def count_item_in_cart(self):
        return self.driver.find_element(*self.number_of_item_locator)
#Action on page:
    def back_to_product_page(self):
        self.back_to_product_button().click()
    def name_of_product(self):
        return self.product_name().text
    def price_of_product(self):
        return self.product_price().text
    def open_cart_page(self):
        self.cart_symbol().click()
    def items_in_cart(self):
        return self.count_item_in_cart().text
    def add_item_to_cart(self):
        self.add_to_cart_button().click()
    def remove_item_from_cart(self):
        self.remove_button().click()
    def check_item_is_not_add_in_cart(self):
        element=self.add_to_cart_button()
        result = is_element_present(driver=self.driver, locator=element)
        return result
    def check_item_is_add_in_cart(self):
        element=self.remove_button()
        result = is_element_present(driver=self.driver, locator=element)
        return result
