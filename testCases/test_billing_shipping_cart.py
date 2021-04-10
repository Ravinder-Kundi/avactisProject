import pytest
import allure
from allure_commons.types import AttachmentType

from Utilties.customLogger import LogGen
from testCases.base_test import BaseTest
from pageObjects.billing_shipping_page import Billing
from Utilties import XLUtils
from selenium.common.exceptions import NoSuchElementException



class Test_billing_shipping(BaseTest):

    logger = LogGen.loggen()
    path = "TestData/guest.xlsx"

    @pytest.mark.sanity
    @allure.severity(allure.severity_level.NORMAL)
    def test_addtocart(self):
        self.logger.info("*******  veriying billing form   **********")
        self.billing = Billing(self.driver)
        self.billing.shop_product()

        self.driver.save_screenshot(".\\Screenshots\\" + " test form .png")

    @pytest.mark.sanity
    @pytest.mark.regression
    @allure.severity(allure.severity_level.NORMAL)
    def test_billing_from(self):

        self.billing = Billing(self.driver)

        self.logger.info("********* Test Billing form *********")
        self.billing.cart_btn_click()
        self.billing.checkout_btn_click()
        self.logger.info("********* Reading Data from Excel *********")
        self.guest = XLUtils.getRowCount(self.path,'Sheet1')
        print( "number of rows g excel : ", self.guest)
        try:
            self.billing.check_billing_form()
            for g in range(2, self.guest + 1):
                self.name= XLUtils.readData(self.path,'Sheet1',g,  1)
                self.lname = XLUtils.readData(self.path, 'Sheet1', g, 2)
                self.email = XLUtils.readData(self.path, 'Sheet1', g, 3)
                self.zcode = XLUtils.readData(self.path,'Sheet1',g, 4)
                self.city = XLUtils.readData(self.path, 'Sheet1', g, 5)
                self.address = XLUtils.readData(self.path, 'Sheet1', g, 6)
                self.Phone= XLUtils.readData(self.path,'Sheet1', g, 7)

                self.billing.fill_billing_form1(self.name, self.lname, self.email)

                self.billing.fill_billing_form2(self.zcode, self.city, self.address, self.Phone)

                self.logger.info("************* DDT form data entered ************")
        except NoSuchElementException:
            self.driver.save_screenshot(".\\Screenshots\\" + " test Billing form .png")
            self.logger.info("******* Test Billing form coudn't find  **********")
            self.logger.error("***** error occur *******")

        self.billing.checkbox_click()
        self.billing.c_checkout()
        self.logger.info("********* checkout continue  *********")
        self.billing.shipping_op_radio()
        self.billing.checkout_button_click()
        self.billing.place_order_click()
        try:
            self.billing.order_msg_no()
            self.driver.save_screenshot(".\\Screenshots\\" + " test Billing order placed .png")
            self.logger.info("***** Order placed successfully *******")

        except NoSuchElementException:
            self.logger.error("***** order havn't placed  *******")
            self.logger.error("***** error occur *******")
            self.driver.save_screenshot(".\\Screenshots\\" + " test Billing_form order error .png")
            allure.attach(self.driver.get_screenshot_as_png(), name=" Test Billing form order error",
                          attachment_type=AttachmentType.PNG)

        self.driver.close()

