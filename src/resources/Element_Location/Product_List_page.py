
class Product_Page:

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

    #Add to cart button any
    def add_to_cart_button_xpath(self,i):
        return f"/html/body/div[1]/div/div/div[2]/div/div/div/div[{i}]/div[2]/div[2]/button"

    #Card of the item
    def card_of_the_item(self,i):
        return f"/html/body/div[1]/div/div/div[2]/div/div/div/div[{i}]/div[1]/a/img"

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

