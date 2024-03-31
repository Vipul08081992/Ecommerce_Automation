from selenium.webdriver.common.by import By
from utils.String_formating import format_string_low_replace
from selenium.webdriver.support.ui import Select
from utils.Check_element_presence import is_element_present
class Product_page:
    def __init__(self,driver):
        self.driver=driver
    heading_locator=(By.XPATH,"//span[@class='title']")
    menu_button_locator=(By.ID,"react-burger-menu-btn")
    sort_dropdown_locator=(By.XPATH,"//select[@class='product_sort_container']")
    shopping_cart_locator=(By.XPATH,"//a[@class='shopping_cart_link']")
    cart_item_count_locator=(By.XPATH,"//span[@class='shopping_cart_badge']")
    item_name_locator=(By.XPATH,"//div[@class='inventory_item_name ']")
    item_price_locator=(By.XPATH,"//div[@class='inventory_item_price']")
    add_to_cart_button_locator=(By.XPATH,"//button[contains(text(),'Add to cart')]")
    remove_button_locator=(By.XPATH,"//button[contains(text(),'Remove')]")
    def specific_item_details_locator(self,item):
        specific_item_details_xpath= f"//img[@alt='{item}']"
        specific_item_details_locator=(By.XPATH,specific_item_details_xpath)
        return specific_item_details_locator
    def specific_item_name_locator(self,item):
        specific_item_name_locator=f"//div[text()='{item}']"
        return specific_item_name_locator
    def specific_item_add_to_cart_locator(self,item):
        item_change = format_string_low_replace(item)
        item_cart = "add-to-cart-" + item_change
        specific_item_add_to_cart_locator = f"//button[@id='add-to-{item_cart}']"
        return specific_item_add_to_cart_locator
    def specific_item_remove_button_locator(self,item):
        item_change = format_string_low_replace(item)
        item_cart = "add-to-cart-" + item_change
        specific_item_remove_button_locator = f"//button[@id='remove-{item_cart}']"
        return specific_item_remove_button_locator

#Get Elements:
    def heading(self):
        return self.driver.find_element(*self.heading_locator)
    def menu_button(self):
        return self.driver.find_element(*self.menu_button_locator)
    def sort_dropdown(self):
        return self.driver.find_element(*self.sort_dropdown_locator)
    def shopping_cart_button(self):
        return self.driver.find_element(*self.shopping_cart_locator)

    def items_present_name(self):
        items_present= self.driver.find_elements(*self.item_name_locator)
        return items_present
    def items_price(self):
        items_price = self.driver.find_elements(*self.item_price_locator)
        return items_price

    def cart_item_count(self):
        return self.driver.find_element(*self.cart_item_count_locator)
    def add_to_cart_button(self):
        add_to_cart_buttons=self.driver.find_elements(*self.add_to_cart_button_locator)
        return add_to_cart_buttons
    def remove_button(self):
        remove_buttons=self.driver.find_elements(*self.remove_button_locator)
        return remove_buttons

    def specific_item_details(self,item):
        return self.driver.find_element(*self.specific_item_details_locator(item))

    def specific_item_name(self,item):
        return self.driver.find_element(*self.specific_item_name_locator(item))
    def specific_item_add_to_cart(self,item):
        return self.driver.find_element(*self.specific_item_add_to_cart_locator(item))
    def specific_item_remove_button(self,item):
        return self.driver.find_element(*self.specific_item_remove_button_locator(item))

#Actions on the page:
    def heading_of_page(self):
        return self.heading().text
    def open_side_panel(self):
        return self.menu_button().click()
    def open_sort_dropdown(self):
        return self.sort_dropdown().click()
    def open_shopping_cart(self):
        return self.shopping_cart_button().click()
    def list_of_items_on_sale(self):
        item_names=[]
        web_element_name=self.items_present_name()
        for web_element in web_element_name:
            item_names.append(web_element.text)
        return item_names
    def list_of_items_price(self):
        items_price=[]
        web_element_name=self.items_price()
        for web_element in web_element_name:
            items_price.append(web_element.text)
        return items_price

    def count_on_cart_symbol(self):
        return self.cart_item_count().text

    def number_of_items_not_added_to_cart(self):
        add_cart= self.add_to_cart_button()
        return len(add_cart)
    def number_of_items_added_in_cart(self):
        remove_button=self.remove_button()
        return len(remove_button)
    def open_specific_item_details(self,item):
        self.specific_item_details(item).click()
    def name_of_item(self,item):
        return self.specific_item_name(item).text
    def add_item_to_cart(self,item):
        return self.specific_item_add_to_cart(item).click()
    def remove_item_from_cart(self,item):
        return self.specific_item_remove_button(item).click()

    def name_of_item_added_to_cart(self):
        items_in_cart=[]
        items_name=self.list_of_items_on_sale()
        for n in items_name:
            element=self.specific_item_remove_button_locator(n)
            result=is_element_present(driver=self.driver, locator=element)
            if result:
                items_in_cart.append(n)
        return items_in_cart
    def name_of_item_not_added_to_cart(self):
        items_not_in_cart = []
        items_name = self.list_of_items_on_sale()
        for n in items_name:
            element = self.specific_item_add_to_cart_locator(n)
            result = is_element_present(driver=self.driver, locator=element)
            if result:
                items_not_in_cart.append(n)
        return items_not_in_cart
class Side_panel(Product_page):
    panel_close_button_locator=(By.ID,"react-burger-cross-btn")
    all_item_locator=(By.ID,"inventory_sidebar_link")
    about_locator=(By.ID,"about_sidebar_link")
    logout_locator=(By.ID,"logout_sidebar_link")
    reset_app_state_locator=(By.ID,"reset_sidebar_link")
#Get Elements:
    def panel_close_button(self):
        return self.driver.find_element(*self.panel_close_button_locator)
    def all_item(self):
        return self.driver.find_element(*self.all_item_locator)
    def about(self):
        return self.driver.find_element(*self.about_locator)
    def logout(self):
        return self.driver.find_element(*self.logout_locator)
    def reset_app_state(self):
        return self.driver.find_element(*self.reset_app_state_locator)
#Actions in panel:
    def close_side_panel(self):
        self.panel_close_button().click()
    def text_all_item(self):
        return self.all_item().text
    def click_on_all_item(self):
        self.all_item().click()
    def text_about(self):
        return self.all_item().text
    def click_on_about(self):
        self.about().click()
    def text_logout(self):
        return self.all_item().text
    def click_on_logout(self):
        self.logout().click()
    def text_reset_app_state(self):
        return self.reset_app_state().text
    def click_on_reset_app_state(self):
        self.reset_app_state().click()
class Sort_dropdown(Product_page):
    def option_available(self):
        dropdown=Select(*self.sort_dropdown())
        option_available=[option.text for option in dropdown.options]
        return option_available
    def number_of_options(self):
        return len(*self.option_available())
    def select_option(self,Text):
        dropdown = Select(*self.sort_dropdown())
        dropdown.select_by_visible_text(Text)
        









