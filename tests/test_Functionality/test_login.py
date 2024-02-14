import pytest
from src.Automate_Fuctionalities.Login import login_using_chrome
from src.utils.Read_Data import read_data_of_cell

#Test1:Verify with Valid username and password
@pytest.mark.positive
def test_valid_credentials_chrome():
    username=read_data_of_cell('C:\\Users\\vipul\\PycharmProjects\\Swag_Labs\\src\\resources\\Data\\Valid Credentials.xlsx',2,2)
    password=read_data_of_cell('C:\\Users\\vipul\\PycharmProjects\\Swag_Labs\\src\\resources\\Data\\Valid Credentials.xlsx',2,3)
    assert login_using_chrome(username=username,password=password) == True

#Test2:Valid username,blank password
@pytest.mark.negative
def test_blank_password_chrome():
    username=read_data_of_cell('C:\\Users\\vipul\\PycharmProjects\\Swag_Labs\\src\\resources\\Data\\Valid Credentials.xlsx',3,2)
    password=""
    assert login_using_chrome(username=username,password=password) == False

#Test3:Blank username,valid password
@pytest.mark.negative
def test_blank_username_chrome():
    username=""
    password=read_data_of_cell('C:\\Users\\vipul\\PycharmProjects\\Swag_Labs\\src\\resources\\Data\\Valid Credentials.xlsx',4,3)
    assert login_using_chrome(username=username,password=password) == False

#Test4:Invalid Credentials
@pytest.mark.negative
def test_invalid_credentials_chrome():
    username=read_data_of_cell('C:\\Users\\vipul\\PycharmProjects\\Swag_Labs\\src\\resources\\Data\\Valid Credentials.xlsx',5,2)
    password=read_data_of_cell('C:\\Users\\vipul\\PycharmProjects\\Swag_Labs\\src\\resources\\Data\\Valid Credentials.xlsx',5,3)
    assert login_using_chrome(username=username,password=password) == False

#Test5:Reverse valid credentials
@pytest.mark.negative
def test_reverse_valid_credentials_chrome():
    username=read_data_of_cell('C:\\Users\\vipul\\PycharmProjects\\Swag_Labs\\src\\resources\\Data\\Valid Credentials.xlsx',6,2)
    password=read_data_of_cell('C:\\Users\\vipul\\PycharmProjects\\Swag_Labs\\src\\resources\\Data\\Valid Credentials.xlsx',6,3)
    assert login_using_chrome(username=username,password=password) == False

#Test6:Uses valid username for both username and password.
@pytest.mark.negative
def test_uses_valid_username_for_both_username_and_password_chrome():
    username=read_data_of_cell('C:\\Users\\vipul\\PycharmProjects\\Swag_Labs\\src\\resources\\Data\\Valid Credentials.xlsx',7,2)
    password=read_data_of_cell('C:\\Users\\vipul\\PycharmProjects\\Swag_Labs\\src\\resources\\Data\\Valid Credentials.xlsx',7,3)
    assert login_using_chrome(username=username,password=password) == False

#Test7:Uses valid password for both username and password.
@pytest.mark.negative
def test_uses_valid_password_for_both_username_and_chrome():
    username=read_data_of_cell('C:\\Users\\vipul\\PycharmProjects\\Swag_Labs\\src\\resources\\Data\\Valid Credentials.xlsx',8,2)
    password=read_data_of_cell('C:\\Users\\vipul\\PycharmProjects\\Swag_Labs\\src\\resources\\Data\\Valid Credentials.xlsx',8,3)
    assert login_using_chrome(username=username,password=password) == False

#Test8:Both username, password blank
@pytest.mark.negative
def test_both_username_password_blank():
    username=""
    password=""
    assert login_using_chrome(username=username,password=password) == False