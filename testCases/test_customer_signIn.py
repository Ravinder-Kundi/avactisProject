import allure
import pytest
from allure_commons.types import AttachmentType

from Utilties import XLUtils
from Utilties.customLogger import LogGen
from pageObjects.register_customer_page import RegisterCustomer
from testCases.base_test import BaseTest


class Test_customer_signIn(BaseTest):
    logger = LogGen.loggen()
    path = ".//TestData/LoginData (version 1).xlsx"

    @pytest.mark.sanity
    @pytest.mark.regression
    @allure.severity(allure.severity_level.CRITICAL)
    def test_customer_signIn(self):

        self.c_sign = RegisterCustomer(self.driver)
        self.c_sign.c_sign_in()

        self.logger.info("********* Test customer sign in started *************")
        self.logger.info("********* Test customer sign in verifying *************")

        self.rows = XLUtils.getRowCount(self.path, 'Customer')
        self.c_email = XLUtils.readData(self.path, 'Customer', 2, 1)
        self.c_passwd = XLUtils.readData(self.path, 'Customer', 2, 2)
        sign_in = self.c_sign.registerCustomer(self.c_email, self.c_passwd)

        if sign_in == self.c_sign.welcome_header:
            self.logger.info("******** Customer Sign in Account ********")
            self.driver.save_screenshot(".\\Screenshots\\" + "customer_sign_in .png")
            allure.attach(self.driver.get_screenshot_as_png(), name=" Test customer sign in",
                          attachment_type=AttachmentType.PNG)
            self.c_sign.signOut()
        else:
            self.driver.save_screenshot(".\\Screenshots\\" + "customer_sign_in_Fail.png")
            self.c_sign.checkSignin()
            self.logger.error("******** customer sign in failed ********** ")
            allure.attach(self.driver.get_screenshot_as_png(), name=" Test Customer sign in is failed ",
                          attachment_type=AttachmentType.PNG)

        self.logger.info("********* Test customer sign in passed *************")
        self.logger.info("********* Test customer sign in finished  *************")
        self.driver.close()
