from Base import InitiateDriver
from Library import ConfigReader

def test_registration_invalida_data():
    driver = InitiateDriver.startBrowser()
    driver.find_element_by_name(ConfigReader.fechElementLocators("Registration", "username")).send_keys("hello")
