from selenium import webdriver
import pytest
import pytest_html

@pytest.fixture(params=['edge'],scope='class')
def init_driver(request):
    if request.param == "edge":
        value = webdriver.Edge(executable_path="resources/msedgedriver.exe")
        print("****** Browser MS Edge ******")
    if request.param == "firefox":
        value = webdriver.Firefox(executable_path="resources/geckodriver.exe")
        print("****** Browser Firefox ******")
    if request.param == "chrome":
        value = webdriver.Chrome(executable_path="resources/chromedriver.exe")
        print("****** Browser Chrome ******")

    request.cls.driver = value
    request.cls.driver.maximize_window()
    yield value
    print("Running one time tearDown")
    print(".....Closing browser......")
"""
def pytest_addoption(parser):
    parser.addoption("--b")

@pytest.fixture(scope="session")
def browser(request):
    return request.config.getoption("--b")
"""
############ PyTest Html Report #####################

def pytest_configure(config):
    config._metadata['Project Name']= 'Avactis Shopping'
    config._metadata['Module Name'] = 'Customers'
    config._metadata['Tester'] = 'Ravinder'

#it's hook for delete/Modify Enviorment info to HTML Report

@pytest.mark.optionalhook
def pytest_metadata(metadata):
    metadata.pop("JAVA_HOME",None)
    metadata.pop("Plugins",None)