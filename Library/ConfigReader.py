import configparser

def readConfigData(section, key):
    config = configparser.ConfigParser()
    config.read('./ConfigurationFiles/Config.cfg')
    return config.get(section, key)

# print(readConfigData("Details", "Application_URL"))

def fechElementLocators(section,key):
    config = configparser.ConfigParser()
    config.read('./ConfigurationFiles/Elements.cfg')
    return config.get(section, key)