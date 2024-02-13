import pytest
from src.Automate_Fuctionalities.Login import login_using_chrome

#Test1:Verify with Valid username and password

def test_valid_credentials_chrome():
    assert login_using_chrome(username,password) == True