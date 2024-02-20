import pytest
from tests.Helper.Automate_Fuctionalities.Login import login_using_chrome
from tests.utils.Read_Data import read_data_of_row, read_data_of_cell


#Test1:Verify with valid Login credentials
@pytest.mark.positive
def test_valid_credentials_chrome():
    username = read_data_of_cell(
        'C:\\Users\\vipul\\PycharmProjects\\Swag_Labs\\src\\resources\\Data\\Valid Credentials.xlsx', 2, 2)
    password = read_data_of_cell(
        'C:\\Users\\vipul\\PycharmProjects\\Swag_Labs\\src\\resources\\Data\\Valid Credentials.xlsx', 2, 3)
    assert login_using_chrome(username=username,password=password)== True


#Test: Verify with invalid input
@pytest.mark.negative
@pytest.mark.parametrize("test_cred",read_data_of_row("C:\\Users\\vipul\\PycharmProjects\\Swag_Labs\\tests\\resourses\\Data\\Valid Credentials.xlsx"))
def test_valid_credentials_chrome(test_cred):
    username=test_cred["username"]
    password=test_cred["password"]
    assert login_using_chrome(username=username,password=password)== False