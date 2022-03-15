import pytest,allure
from allure_commons.types import AttachmentType
from selenium.common.exceptions import NoSuchElementException

from Utilties.customLogger import LogGen
from pageObjects.shopping_page import Shopping
from testCases.base_test import BaseTest
from pageObjects.register_customer_page import RegisterCustomer
from pageObjects.billing_shipping_page import Billing
from Utilties import XLUtils

class Test_Shopping_Cart(BaseTest):
    logger = LogGen.loggen()
    path = "TestData/LoginData (version 1).xlsx"

    @pytest.mark.sanity
    @allure.severity(allure.severity_level.NORMAL)
    def test_Store_homePagetitle(self):
        self.shop = Shopping(self.driver)
        self.logger.info("************* test store Home Page title test is started ***************")
        self.logger.info("************* Verifying store Home Page title test **************")
        act_title = self.shop.shop_title()
        if act_title == self.driver.title:
            self.logger.info("************* test store Home Page title test is pass***************")
            print(act_title)
            assert True

        else:
            self.driver.save_screenshot(".\\Screenshots\\" + "test_store_homepage_title.png")
            self.logger.info("*************Home Page title test is fail ***************")


    @pytest.mark.regression
    @allure.severity(allure.severity_level.NORMAL)
    def test_shop_rcustomer(self):
        self.logger.info("******** Sign in as Register customer ******** ")

        self.sigin= RegisterCustomer(self.driver)
        self.rows = XLUtils.getRowCount(self.path, 'Customer')
        self.email=XLUtils.readData(self.path,'Customer', 2, 1)
        self.passwd =XLUtils.readData(self.path,'Customer', 2, 2)
        self.sigin.registerCustomer(self.email,self.passwd)

        self.pro_rows =XLUtils.getRowCount(self.path,'Products')
        for i in range(2, self.pro_rows + 1):
            self.menu = XLUtils.readData(self.path,'Products', i, 1)
            self.submenu = XLUtils.readData(self.path,'Products', i, 2)

            self.item = XLUtils.readData(self.path, 'Products', i, 3)
            self.shop = Shopping(self.driver)
            self.shop.Titlebar(self.menu)
            if self.submenu != "x":
                self.shop.Submenu(self.submenu)

            self.shop.Item(self.item)
            self.logger.info("******* item added to cart  **********")
            print("item added to cart")

        self.billing = Billing(self.driver)
        self.billing.cart_btn_click()
        self.billing.checkout_btn_click()
        self.billing.checkbox_click()
        self.billing.c_checkout()
        self.billing.shipping_op_radio()
        self.billing.checkout_button_click()
        self.billing.place_order_click()
        try:
            self.billing.order_msg_no()
            self.logger.info("***** Order placed successfully *******")
            self.driver.save_screenshot(".\\Screenshots\\" + " test_shopping_cart order placed successfully .png")
        except NoSuchElementException:
            self.logger.info("***** order havn't placed  *******")
            self.logger.error("***** error occur to place the order  *******")
            self.driver.save_screenshot(".\\Screenshots\\" + " test _shopping_cart error occur to place the order .png")
            allure.attach(self.driver.get_screenshot_as_png(), name=" Test Shopping Cart error occur",
                          attachment_type=AttachmentType.PNG)
        self.sigin.signOut()