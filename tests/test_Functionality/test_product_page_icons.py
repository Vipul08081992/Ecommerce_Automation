import pytest
from src.Automate_Fuctionalities.cart_button_functionality import cart_button_no_product_add,cart_button_product_all_add,cart_button_product_add_remove_some,cart_button_product_add,cart_button_product_add_remove_all,cart_button_product_add_all_remove_all
from src.Automate_Fuctionalities.menu_button_functionality import menu_button_product_add_all_remove_all,menu_button_product_add_remove_all,menu_button_product_add_remove_some,menu_button_product_all_add,menu_button_product_add,menu_button_no_product_add


# Cart List
@pytest.mark.positive
class Test_cart_functionality:
# Test1:When no Product Added
    @staticmethod
    def test_without_product():
        assert cart_button_no_product_add() == True

#Test2: When add some items
    @staticmethod
    def test_some_item_added():
        assert cart_button_product_add() == True

#Test3: When add some items the remove some but not all
    @staticmethod
    def test_add_items_remove_some():
        assert cart_button_product_add_remove_some() == True

#Test4: Add all items
    @staticmethod
    def test_add_all_items():
        assert cart_button_product_all_add() == True

#Test5: When add some items the remove them all
    @staticmethod
    def test_add_remove_some_item():
        assert cart_button_product_add_remove_all() == True

#Test6: Add all item and remove all
    @staticmethod
    def test_add_remove_all_items():
        assert cart_button_product_add_all_remove_all() ==True


@pytest.mark.positive
class Test_menu_functionality:
# Test1:When no Product Added
    @staticmethod
    def test_without_product():
        assert menu_button_no_product_add() == True

#Test2: When add some items
    @staticmethod
    def test_some_item_added():
        assert menu_button_product_add() == True

#Test3: When add some items the remove some but not all
    @staticmethod
    def test_add_items_remove_some():
        assert menu_button_product_add_remove_some() == True

#Test4: Add all items
    @staticmethod
    def test_add_all_items():
        assert menu_button_product_all_add() == True

#Test5: When add some items the remove them all
    @staticmethod
    def test_add_remove_some_item():
        assert menu_button_product_add_remove_all() == True

#Test6: Add all item and remove all
    @staticmethod
    def test_add_remove_all_items():
        assert menu_button_product_add_all_remove_all() ==True


