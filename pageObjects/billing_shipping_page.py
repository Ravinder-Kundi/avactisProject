from selenium.webdriver.common.by import By

from Utilties.readProperties import ReadConfig
from pageObjects.basePage import BasePage


class Billing(BasePage):
    product = (By.XPATH, "//h3[1]")
    add_to_cart = (By.XPATH, "//input[@value='Add To Cart']")
    billing_form = (By.CSS_SELECTOR, "[class='billing_form col-lg-6']")
    f_fname = (By.XPATH, "//input[@name = 'billingInfo[Firstname]']")
    f_lname = (By.CSS_SELECTOR, "input[name='billingInfo[Lastname]']")
    f_email = (By.CSS_SELECTOR, "input[name='billingInfo[Email]']")
    f_zipcode = (By.CSS_SELECTOR, "input[name='billingInfo[Postcode]']")
    f_city = (By.CSS_SELECTOR, "input[name='billingInfo[City]']")
    f_address = (By.CSS_SELECTOR, "input[name='billingInfo[Streetline1]']")
    f_phone = (By.CSS_SELECTOR, "input[name='billingInfo[Phone]']")
    f_checkbox = (By.NAME, "checkbox_shipping_same_as_billing")
    c_checkout_btn = (By.CSS_SELECTOR, "[class= 'en btn btn-primary button_continue_checkout']")
    cart_btn = (By.CSS_SELECTOR, "[class ='fa fa-shopping-cart']")
    checkout_btn = (By.CSS_SELECTOR, "[class='btn btn-primary']")
    cart_info_count = (By.CSS_SELECTOR, "[class='top-cart-info-count']")
    shipping_option = (By.XPATH, "//input[@value='BCE5D24D-666C-43CA-94A0-D6F775903BE2_3']")

    Checkout_Button = (By.XPATH, "//input[@onclick ='submitStep(2);']")
    place_order = (By.CSS_SELECTOR, "[class='en btn btn-primary button_place_order input_submit']")
    order_msg = (By.CSS_SELECTOR, "[class='note note-success note-bordered']")

    def __init__(self, driver):
        super().__init__(driver)

        self.driver.get(ReadConfig.getStoreUrl())

    def check_billing_form(self):
        self.is_visible(self.billing_form)

    def fill_billing_form1(self, firstname, lastname, Email):
        self.do_send_keys(self.f_fname, firstname)
        self.do_send_keys(self.f_lname, lastname)

        self.do_send_keys(self.f_email, Email)

    def fill_billing_form2(self, Zipcode, City, Address, Phone):
        self.do_send_keys(self.f_zipcode, Zipcode)
        self.do_send_keys(self.f_city, City)
        self.do_send_keys(self.f_address, Address)
        self.do_send_keys(self.f_phone, Phone)

    def checkbox_click(self):
        self.do_click(self.f_checkbox)

    def c_checkout(self):
        self.do_click(self.c_checkout_btn)

    def cart_btn_click(self):
        self.do_click(self.cart_btn)

    def cart_btn_text(self):
        c = self.get_element_text(self.cart_btn)
        return print(c)

    def checkout_btn_click(self):
        self.do_click(self.checkout_btn)

    def check_cart_count_info(self):
        self.do_click(self.cart_info_count)

    def shop_product(self):
        self.do_click(self.product)
        self.do_click(self.add_to_cart)

    def shipping_op_radio(self):
        self.is_visible(self.shipping_option)
        self.do_click(self.shipping_option)

    def checkout_button_click(self):
        self.do_click(self.Checkout_Button)

    def place_order_click(self):
        self.do_click(self.place_order)

    def order_msg_no(self):
        self.is_visible(self.order_msg)
        a = self.get_element_text(self.order_msg)
        print(a)
