import time
from Utilties import XLUtils
import pytest
from selenium import webdriver
from pageObjects.login_page import LoginPage
from Utilties.readProperties import ReadConfig
from testCases.base_test import BaseTest
from Utilties.customLogger import LogGen
import allure
from allure_commons.types import AttachmentType

class Test_DDT_Login(BaseTest):
    baseURL= ReadConfig.getApplicationURL()
    path = ".//TestData/LoginData.xlsx"
    logger = LogGen.loggen()
    homePage = ReadConfig.getPageTitle()

    @pytest.mark.regression
    @allure.severity(allure.severity_level.CRITICAL)
    def test_login_ddt(self):
        self.driver.get(self.baseURL)
        self.loginPage = LoginPage(self.driver)
        self.logger.info("******* Starting Test_DDT_Login Test **********")
        self.logger.info("******* Starting Login DDT Test **********")
        self.rows = XLUtils.getRowCount(self.path,'Sheet1')
        print("number of rows i a excel: ",self.rows)
        lst_status =[] #empty list
        self.logger.info("******* Reading data from excel **********")
        for r in range(2, self.rows + 1):
            self.user = XLUtils.readData(self.path, 'Sheet1', r, 1)
            self.password = XLUtils.readData(self.path, 'Sheet1', r, 2)
            self.status = XLUtils.readData(self.path, 'Sheet1', r, 3)
            self.loginPage.do_login(self.user,self.password)

            if self.status == "True":
                if self.driver.title == self.homePage:
                    self.logger.info("Login Test Passed")
                    lst_status.append("Pass")

                    self.loginPage.sign_out()
                else:
                    lst_status.append("Fail")
                    self.logger.info("Login Test Failed")
                    allure.attach(self.driver.get_screenshot_as_png(), name=" Test DDT Login screen",
                                  attachment_type=AttachmentType.PNG)

            elif self.status == "False":
                if self.driver.title != self.homePage:
                    lst_status.append("Pass")
                    self.logger.info("Login Test Passed")
                    allure.attach(self.driver.get_screenshot_as_png(), name=" Test DDT Login screen",
                                  attachment_type=AttachmentType.PNG)
                    self.driver.save_screenshot(".\\Screenshots\\" + "test_Login_DDT.png")
                else:
                    lst_status.append("Fail")
                    self.logger.info("Login Test Failed")
                    self.loginPage.sign_out()
                    allure.attach(self.driver.get_screenshot_as_png(), name="  Test DDT Login screen",
                                  attachment_type=AttachmentType.PNG)
            if r == 6:

                self.logger.info("test_login_ddt", "Pass", "Login was successful")
                self.logger.info("******* Ending Login DDT Test **********")
                self.driver.close()