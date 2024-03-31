from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
def explicit_waits(driver,t_in_sec,element):
    try:
        element=WebDriverWait(driver,t_in_sec).until(EC.presence_of_element_located(element))
    except:
        print('No Element Present')