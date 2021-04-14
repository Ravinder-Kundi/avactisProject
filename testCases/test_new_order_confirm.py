from selenium.common.exceptions import NoSuchElementException

from pageObjects.login_page import LoginPage
from Utilties.readProperties import ReadConfig
from testCases.base_test import BaseTest
from Utilties.customLogger import LogGen
from pageObjects.admin_new_order import New_orders
import allure
from allure_commons.types import AttachmentType

class Test_new_orders(BaseTest):
    logger = LogGen.loggen()
    adminEmail = ReadConfig.getUserEmail()
    password = ReadConfig.getPassword()

    def test_neworder_confirm(self):
        self.logger.info("********** test new order starting *******")
        self.newOrders = New_orders(self.driver)
        self.logger.info("******** test new order verifiing *********")
        self.logger.info("******** login on admin page  *********")
        self.newOrders.do_login(self.adminEmail,self.password)

        self.newOrders.click_order_menu()
        try:
            self.newOrders.new_order_info()
            self.newOrders.table_order_data()
            self.logger.info("******** Test new order is passed *******")
            self.driver.save_screenshot(".//Screenshots//" + "test_new_order_confirm.png")
        except NoSuchElementException:
            self.logger.error("********** Test new order is failed ***********")




