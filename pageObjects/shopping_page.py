import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By

from Utilties.readProperties import ReadConfig
from pageObjects.basePage import BasePage
from pageObjects.billing_shipping_page import Billing

class Shopping(BasePage):
    del_cart= (By.CSS_SELECTOR,"[class='del-goods']")
    shop_cart= (By.CSS_SELECTOR,"[class='fa fa-shopping-cart']")
    add_to_cart = (By.XPATH, "//input[@value='Add To Cart']")
    out_of_stock = (By.CSS_SELECTOR, "[class='en btn btn-primary button_out_of_stock']")
    cart_btn =(By.CSS_SELECTOR,"[class ='fa fa-shopping-cart']")
    checkout_btn= (By.CSS_SELECTOR,"[class='btn btn-primary']")
    fname = (By.NAME, "billingInfo[Firstname]")
    lname = (By.NAME, "billingInfo[Lastname]")
    email = (By.NAME, "billingInfo[Email]")
    zipcode = (By.NAME, "billingInfo[Postcode]")
    city = (By.NAME, "billingInfo[City]")
    address = (By.NAME, "billingInfo[Streetline1]")
    phone = (By.NAME, "billingInfo[Phone]")
    checkbox = (By.NAME, "checkbox_shipping_same_as_billing")
    c_checkout_btn = (By.CSS_SELECTOR, "[class= 'en btn btn-primary button_continue_checkout']")
    checkout_form_1 = (By.CSS_SELECTOR, "[id='checkout_1']")

    def __init__(self,driver):
        super().__init__(driver)

        self.driver.get(ReadConfig.getStoreUrl())

    def shop_title(self):
        title = ReadConfig.getStoreTitle()
        return title

    def shopping_cart(self):
        self.is_visble(self.shop_cart)
        self.do_click(self.shop_cart)

    def goods_del_cart(self):
        self.do_click(self.shop_cart)
        cart =self.is_visble(self.del_cart)
        if  cart == True:
            self.do_click(self.del_cart)
        else:
            assert False

    def Titlebar(self, selection):
        row = ['APPAREL', 'COMPUTERS', 'DVD', 'FURNITURE', 'SPORT', 'DIGITAL DISTRIBUTION']
        index = row.index(selection.upper())
        xpath = (By.XPATH,"//div[@class='header-navigation']//li[" + str(index + 1) + "]")
        self.do_click(xpath)

    def Submenu(self,smenu):
        xpath = (By.XPATH, "//img[@alt='" + smenu + "']")
        self.do_click(xpath)

    def Item(self, item):
        xpath =(By.XPATH, "//img[@alt='" + item + "']")
        self.do_click(xpath)
        self.do_click(self.add_to_cart)


    def Cart_btn(self):
        self.do_click(self.cart_btn)

    def Checkout_btn(self):
        self.do_click(self.checkout_btn)




