from selenium.webdriver import Chrome
from selenium.webdriver import Firefox
from Library import ConfigReader

def startBrowser():
    global driver
    if ((ConfigReader.readConfigData('Details', 'Browser')) == 'chrome'):
        path = "D:\\pythonpr\\pythonProject1\\chromedriver"
        driver = Chrome(executable_path=path)
    elif ((ConfigReader.readConfigData('Details', 'Browser')) == 'firefox'):
        path = "D:\\pythonpr\\pythonProject1\\geckodriver"
        driver = Firefox(executable_path=path)
    else:
        path = "D:\\pythonpr\\pythonProject1\\chromedriver"
        driver = Chrome(executable_path=path)

    driver.get(ConfigReader.readConfigData('Details', 'Application_URL'))

    driver.maximize_window()
    return driver

def closeBrowser():
    driver.close()