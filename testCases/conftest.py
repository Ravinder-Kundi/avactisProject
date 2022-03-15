import pytest
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from webdriver_manager.chrome import ChromeDriverManager
from webdriver_manager.firefox import GeckoDriverManager


@pytest.fixture(params=['edge'], scope='class')
def init_driver(request):
    if request.param == "edge":

        value = webdriver.Edge(executable_path="resources/msedgedriver.exe")
        print("****** Browser MS Edge ******")
    if request.param == "firefox":
        value = webdriver.Firefox(executable_path=GeckoDriverManager().install())
        print("****** Browser Firefox ******")
    if request.param == "chrome":
        value = webdriver.Chrome(ChromeDriverManager().install())
        print("****** Browser Chrome ******")
        options = Options()

        options.add_experimental_option('excludeSwitches', ['enable-logging'])

    request.cls.driver = value
    request.cls.driver.maximize_window()
    yield value
    print("Running one time tearDown")
    print(".....Closing browser......")


############ PyTest Html Report #####################

def pytest_configure(config):
    config._metadata['Project Name'] = 'Avactis Shopping'
    config._metadata['Module Name'] = 'Customers'
    config._metadata['Tester'] = 'Ravinder'


# it's hook for delete/Modify Enviorment info to HTML Report

@pytest.mark.optionalhook
def pytest_metadata(metadata):
    metadata.pop("JAVA_HOME", None)
    metadata.pop("Plugins", None)
