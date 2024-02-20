
class Product_Page:

    #Product Heading
    @staticmethod
    def heading_prodouct():
        return "//div[@class='aap_logo']"

    #Cart Symbol
    @staticmethod
    def cart_symbol_class():
        return "shopping_cart_link"

    #Menu button
    @staticmethod
    def menu_button_id():
        return "react-burger-menu-btn"

    #Filter button
    @staticmethod
    def filter_button_class():
        return "product_sort_container"

    # Add to cart button any
    @staticmethod
    def add_to_cart_button_xpath():
        return "//button[contains(text(),'Add to cart')]"

    #Remove Item from cart
    @staticmethod
    def remove_from_cart_button_xpath():
        return "//button[contains(text(),'Remove')]"

    #Card of the item
    def card_of_the_item(self,i):
        return "//img[@class='inventory_item_img']"

class Side_menu:
        # Cross button
    @staticmethod
    def cross_button_id():
        return "react-burger-cross-btn"

    #All Item
    @staticmethod
    def all_item_id():
        return "inventory_sidebar_link"

    #About
    @staticmethod
    def about_id():
        return "about_sidebar_link"

    #Logout
    @staticmethod
    def logout_id():
        return "logout_sidebar_link"

    #Reset App State
    @staticmethod
    def reset_app_state_id():
        return "reset_sidebar_link"

class Filter:
    #Name (A to Z) option
    @staticmethod
    def name_AtoZ_css():
        return "option[value*='az']"

    #Name (Z to A) option
    @staticmethod
    def name_ZtoA_css():
        return "option[value*='za']"

    #Price (low to high)option
    @staticmethod
    def price_ltoh_css():
        return "option[value*='lohi']"

    # Price (high to low)option
    @staticmethod
    def price_htot_css():
        return "option[value*='hilo']"


