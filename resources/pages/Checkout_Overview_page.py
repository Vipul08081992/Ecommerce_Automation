from selenium.webdriver.common.by import By

from utils.convert_string_to_float import convert_string_to_float
from utils.convertlist_todict import two_list_to_dict


class Checkout_information_page:
    def __init__(self,driver):
        self.driver=driver
    heading_locator=(By.XPATH,"//span[@class='title']")
    cancel_locator=(By.ID,"cancel")
    finish_locator=(By.NAME,"finish")
    items_in_cart_name_locator = (By.XPATH, "//div[@class='inventory_item_name']")
    items_in_cart_price_locator = (By.XPATH, "//div[@class='inventory_item_price']")
    item_total_locator=(By.XPATH,"//div[@class='summary_subtotal_label']")
    tax_locator=(By.XPATH,"//div[@class='summary_tax_label']")
    total_locator=(By.XPATH,"//div[@class='summary_total_label']")
#Get Element:
    def heading(self):
        return self.driver.find_element(*self.heading_locator)
    def cancel(self):
        return self.driver.find_element(*self.cancel_locator)
    def finish(self):
        return self.driver.find_element(*self.finish_locator)
    def items_in_cart_name(self):
        return self.driver.find_elements(*self.items_in_cart_name_locator)
    def items_in_cart_price(self):
        return self.driver.find_elements(*self.items_in_cart_price_locator)
    def item_total(self):
        return self.driver.find_element(*self.item_total_locator)
    def tax(self):
        return self.driver.find_element(*self.tax_locator)
    def total(self):
        return self.driver.find_element(*self.total_locator)

#Action on page:
    def heading_text(self):
        return self.heading().text
    def back_to_information_page(self):
        self.cancel().click()
    def complete_checkout(self):
        self.finish().click()
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
    def tax_value(self):
        tax=self.tax().text
        value=convert_string_to_float(tax)
        return value
    def total_value(self):
        total=self.total().text
        value=convert_string_to_float(total)
        return value

    def calculate_item_total(self):
        sum=0
        prices=self.get_items_in_cart_price()
        for i in prices:
            v=convert_string_to_float(i)
            sum=sum+v
        return sum
    def calculate_total_amount(self):
        item_total=self.calculate_item_total()
        tax=self.tax_value()
        sum=item_total+tax
        return sum


