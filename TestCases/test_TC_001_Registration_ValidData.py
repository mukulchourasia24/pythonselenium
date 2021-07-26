from selenium.webdriver import Chrome
from Base import InitiateDriver
from selenium.webdriver.support.select import Select
from Library import ConfigReader
from Pages import Registration

def test_ValidateRegisteration():
    driver = InitiateDriver.startBrowser()
    # Enter data in textbox
    driver.find_element_by_name(ConfigReader.fechElementLocators("Registration", "username")).send_keys("hello")
    register = Registration.RegistrationClass(driver)
    register.enter_email("testing@frf.ol")
    register.enter_password("abcd123")
    register.enter_conf_password("abcd123")
    register.clear_username()
    register.re_enter_username("hey")
    # driver.find_element_by_xpath("//input[@name='fld_email']").send_keys("testing@frf.ol")
    # driver.find_element_by_name("fld_password").send_keys("abcd123")
    # driver.find_element_by_name("fld_cpassword").send_keys("abcd123")
    # driver.find_element_by_name("fld_username").clear()
    # driver.find_element_by_name("fld_username").send_keys("hey")

    # Working on Radio button
    driver.find_element_by_xpath("//input[@value='office']").click()

    # Working on dropdown
    obj = Select(driver.find_element_by_name("sex"))
    obj.select_by_visible_text("Male")
    # obj.select_by_value("2")
    # obj.select_by_index(1)

    # Working on checkbox
    driver.find_element_by_name("terms").click()

    # Work on button
    # driver.find_element_by_xpath("//input[@type='submit']").click()

    # Work on Links
    # driver.find_element_by_link_text("Read Detail").click()

    # driver.close()