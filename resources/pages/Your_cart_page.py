from selenium.webdriver.common.by import By

from utils.String_formating import format_string_low_replace
from utils.convertlist_todict import two_list_to_dict


class Your_cart_page:
    def __init__(self,driver):
        self.driver=driver
    heading_locator=(By.XPATH,"//span[@class='title']")
    items_in_cart_name_locator=(By.XPATH,"//div[@class='inventory_item_name']")
    items_in_cart_price_locator=(By.XPATH,"//div[@class='inventory_item_price']")
    def specific_item_remove_button_locator(self,item):
        item_change = format_string_low_replace(item)
        item_cart = "add-to-cart-" + item_change
        specific_item_remove_button_locator = f"//button[@id='remove-{item_cart}']"
        return specific_item_remove_button_locator

    continue_shopping_locator=(By.NAME,"continue-shopping")
    checkout_locator=(By.NAME,"checkout")
    count_of_item_locator=(By.XPATH,"//span[@class='shopping_cart_badge']")
#Get Elements:
    def heading(self):
        return self.driver.find_element(*self.heading_locator)
    def items_in_cart_name(self):
        return self.driver.find_elements(*self.items_in_cart_name_locator)
    def items_in_cart_price(self):
        return self.driver.find_elements(*self.items_in_cart_price_locator)
    def specific_item_remove_button(self,item):
        return self.driver.find_element(*self.specific_item_remove_button_locator(item))
    def continue_shopping(self):
        return self.driver.find_element(*self.continue_shopping_locator)
    def checkout(self):
        return self.driver.find_element(*self.checkout_locator)
    def count_of_item(self):
        return self.driver.find_element(*self.count_of_item_locator)
#Action on Page:
    def get_heading_of_page(self):
        return self.heading().text
    def get_items_in_cart_name(self):
        names=[]
        web_element=self.items_in_cart_name()
        for ele in web_element:
            names.append(ele.text)
        return names

    def get_items_in_cart_price(self):
        prices = []
        web_element = self.items_in_cart_price()
        for ele in web_element:
            prices.append(ele.text)
        return prices
    def get_item_name_price_pair(self):
        names=self.get_items_in_cart_name()
        prices=self.get_items_in_cart_price()
        pairs=two_list_to_dict(names,prices)
        return pairs
    def click_on_specific_item_remove_button(self,item):
        self.specific_item_remove_button(item).click()
    def number_of_item_in_cart(self):
        return len(self.items_in_cart_name())
    def count_of_cart(self):
        return self.count_of_item().text
    def back_to_shopping(self):
        self.continue_shopping().click()
    def open_checkout_page(self):
        self.checkout().click()
    