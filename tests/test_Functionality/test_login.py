import pytest
from tests.Helper.Automate_Fuctionalities.Login_functionality import  login_button_click
from tests.resourses.Element_Location.URLs_of_Website import product_page_url
from tests.Helper.Generic_functions.Read_Data import read_data_of_row


#Test: Verify login functionality
@pytest.mark.parametrize("test_cred",read_data_of_row("C:\\Users\\vipul\\PycharmProjects\\Swag_Labs\\tests\\resourses\\Data\\Valid Credentials.xlsx"))
def test_valid_credentials_chrome(test_cred):
    username=test_cred["username"]
    password=test_cred["password"]
    output_list=login_button_click(username, password)
    assert output_list[0] == product_page_url()
    output_list[1].quit()