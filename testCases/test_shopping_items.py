import allure
from allure_commons.types import AttachmentType

from Utilties import XLUtils
from Utilties.customLogger import LogGen
from pageObjects.shopping_page import Shopping
from testCases.base_test import BaseTest


class Test_shop_asGuest(BaseTest):
    logger = LogGen.loggen()
    path = "TestData/LoginData (version 1).xlsx"

    @allure.severity(allure.severity_level.NORMAL)
    def test_guest_shopping(self):
        self.pro_rows = XLUtils.getRowCount(self.path, 'Products')
        for i in range(2, self.pro_rows + 1):
            self.menu = XLUtils.readData(self.path, 'Products', i, 1)
            self.submenu = XLUtils.readData(self.path, 'Products', i, 2)

            self.item = XLUtils.readData(self.path, 'Products', i, 3)
            self.shop = Shopping(self.driver)
            self.shop.Titlebar(self.menu)
            if self.submenu != "x":
                self.shop.Submenu(self.submenu)

            self.shop.Item(self.item)
            self.logger.info("******* item added to cart  **********")
            self.driver.save_screenshot(".\\Screenshots\\" + "  .png")
            allure.attach(self.driver.get_screenshot_as_png(), name=" Test Shopping item",
                          attachment_type=AttachmentType.PNG)
