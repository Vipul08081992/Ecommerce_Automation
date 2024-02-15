import pytest
from src.Automate_Fuctionalities.product_page_cart_button_functionality import cart_button_no_product_add
# Cart List
class Test_cart_functionality:
# Test1:When no Product Added
    @staticmethod
    def test_without_product():
        assert cart_button_no_product_add() == True


