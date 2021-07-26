from Library import ConfigReader

class   RegistrationClass:
    def __init__(self, obj):
        global driver
        driver = obj

    def enter_username(self, username):
        driver.find_element_by_name(ConfigReader.fechElementLocators("Registration", "username")).send_keys(username)

    def enter_password(self, password):
        driver.find_element_by_name("fld_password").send_keys(password)

    def enter_conf_password(self, password):
        driver.find_element_by_name("fld_cpassword").send_keys(password)

    def enter_email(self, email):
        driver.find_element_by_xpath("//input[@name='fld_email']").send_keys(email)

    def clear_username(self):
        driver.find_element_by_name("fld_username").clear()

    def re_enter_username(self, username):
        driver.find_element_by_name("fld_username").send_keys(username)

