import allure
import pytest
from allure_commons.types import AttachmentType

from Utilties import XLUtils
from Utilties.customLogger import LogGen
from pageObjects.register_customer_page import RegisterCustomer
from testCases.base_test import BaseTest

class Test_register_customer(BaseTest):
    logger = LogGen.loggen()
    path = ".//TestData/LoginData (version 1).xlsx"

    @pytest.mark.sanity
    @pytest.mark.regression
    @allure.severity(allure.severity_level.CRITICAL)
    def test_sign_in(self):
        self.logger.info("*************Test Sign in ***************")
        self.logger.info("*************Verifying Sign in  ***************")
        self.signin = RegisterCustomer(self.driver)
        self.signin.sign_in_link()
        self.driver.save_screenshot(".\\Screenshots\\" + "test_Sign in.png")
        self.logger.info("*************  test sign in passed ************")

    @pytest.mark.sanity
    @pytest.mark.regression
    @allure.severity(allure.severity_level.CRITICAL)
    def test_register_Customer(self):

        self.reg = RegisterCustomer(self.driver)
        self.reg.Register_button()
        self.logger.info("**************test_register_customer_ddt*************************")
        self.logger.info("*******  started Register Customer DDT Test **********")
        self.rows = XLUtils.getRowCount(self.path, 'Customer')
        print("count excel file rows : ",self.rows)
        self.logger.info("******* Reading data from excel **********")
        self.email = self.reg.random_generator()+'@gmail.com'
        self.logger.info("******* New customer email entered   **********")
        for r in range(2, self.rows):

            self.password = XLUtils.readData(self.path, 'Customer', r, 2)
            self.repasswd = XLUtils.readData(self.path, 'Customer', r, 3)
            self.fname = XLUtils.readData(self.path, 'Customer', r, 4)
            self.lname= XLUtils.readData(self.path, 'Customer', r, 5)
            self.zipcode = XLUtils.readData(self.path, 'Customer', r, 6)
            self.address = XLUtils.readData(self.path, 'Customer', r, 7)
            self.phone  = XLUtils.readData(self.path, 'Customer', r, 8)


            reg = self.reg.registerForm(self.email, self.password, self.repasswd, self.fname,
                                   self.lname, self.zipcode, self.address, self.phone)

            self.driver.save_screenshot(".\\Screenshots\\" + "registration.png")
            self.logger.info("*******  test_register_customer_ddt , Data added to form  **********")
            if reg == self.reg.checkRegister():
                assert True
            else:
                self.driver.save_screenshot(".\\Screenshots\\" + "registration.png")
                self.logger.info("test_register_customer_ddt", "Pass", "Registration was successful")
                self.logger.info("******* Ending Register Customer DDT Test **********")
                allure.attach(self.driver.get_screenshot_as_png(), name=" Test Register Customer Sucessful",
                              attachment_type= AttachmentType.PNG)
            self.reg.signOut()
            self.driver.close()

