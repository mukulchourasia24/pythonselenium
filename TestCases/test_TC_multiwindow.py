from selenium.webdriver import Chrome
import pytest

@pytest.fixture()
def set_path():
    global driver
    path = "D:\\pythonpr\\pythonProject1\\chromedriver"
    driver = Chrome(executable_path=path)
    driver.get("https://www.w3schools.com/")

def test_manage_tab(set_path):
    driver.find_element_by_xpath("//a[text()='W3SCHOOLS SHOP']").click()
    all_tab = driver.window_handles
    mainWin =""
    print("iii")
    for tb in all_tab:
        driver.switch_to.window(tb)
        if (driver.current_url == "https://shop.w3schools.com/"):
            driver.find_element_by_xpath("//span[text()='T-Shirts']").click()
            driver.close()
        elif (driver.current_url == "https://www.w3schools.com/"):
            mainWin = tb
    driver.switch_to.window(mainWin)
    return driver.current_url

