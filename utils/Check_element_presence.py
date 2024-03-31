#Check element is present or not:
from selenium.common.exceptions import NoSuchElementException
def is_element_present(driver, locator):
    try:
        driver.find_element(*locator)
        return True
    except NoSuchElementException:
        return False
