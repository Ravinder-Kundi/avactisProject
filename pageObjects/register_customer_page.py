import random
import string

from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.common.by import By

from Utilties.readProperties import ReadConfig
from pageObjects.basePage import BasePage


class RegisterCustomer(BasePage):
    sign_in = (By.XPATH, "//div[@class='menu cmsmenu']//li[1]")
    register_btn = (By.XPATH, "//button[@class='btn btn-default']")
    register_form = (By.CLASS_NAME, 'registration_form')
    r_email = (By.NAME, 'customer_info[Customer][Email]')
    r_password = (By.NAME, 'customer_info[Customer][Password]')
    r_repaswd = (By.NAME, 'customer_info[Customer][RePassword]')
    r_firstName = (By.NAME, 'customer_info[Customer][FirstName]')
    r_lastName = (By.NAME, 'customer_info[Customer][LastName]')
    r_country = (By.ID, 'customer_info_Customer_Country')
    r_state = (By.ID, 'customer_info_Customer_State')
    r_zipcode = (By.NAME, 'customer_info[Customer][ZipCode]')
    r_address1 = (By.NAME, 'customer_info[Customer][Streetline1]')
    r_phone = (By.NAME, 'customer_info[Customer][Phone]')
    r_Reg_button = (By.XPATH, "//input[@type='submit']")
    reg_customer_email = (By.NAME, 'email')
    reg_customer_passwd = (By.NAME, 'passwd')
    reg_Cus_btn_signIn = (By.XPATH, "//input[@type='submit']")
    Sign_out = (By.XPATH, "//li[1]/span/a")
    reg_customer_signIn = (By.XPATH, '//span/a')
    welcome_header = (By.XPATH, "//span[@class = 'header_wel']")

    def __init__(self, driver):
        super().__init__(driver)

        self.driver.get(ReadConfig.getStoreUrl())

    def Store_title(self):
        title = ReadConfig.getStoreTitle()
        return title

    def sign_in_link(self):
        act_title = self.Store_title()
        if act_title == self.driver.title:
            assert True
            self.is_visible(self.sign_in)
            self.do_click(self.sign_in)
        else:
            assert False

    def Register_button(self):

        self.do_click(self.sign_in)

        if self.is_visible(self.register_btn):
            self.do_click(self.register_btn)
            assert True

        else:
            assert False

        if self.is_visible(self.register_form):
            assert True
        else:
            assert False

    def registerForm(self, email, password, repasswd, fName, lname, zcode, address, phone):
        self.clear_text_field(self.r_email)
        self.do_send_keys(self.r_email, email)
        self.clear_text_field(self.r_password)
        self.do_send_keys(self.r_password, password)
        self.clear_text_field(self.r_repaswd)
        self.do_send_keys(self.r_repaswd, repasswd)
        self.clear_text_field(self.r_firstName)
        self.do_send_keys(self.r_firstName, fName)
        self.clear_text_field(self.r_lastName)
        self.do_send_keys(self.r_lastName, lname)
        self.clear_text_field(self.r_zipcode)
        self.do_send_keys(self.r_zipcode, zcode)
        self.clear_text_field(self.r_address1)
        self.do_send_keys(self.r_address1, address)
        self.clear_text_field(self.r_phone)
        self.do_send_keys(self.r_phone, phone)
        self.do_click(self.r_Reg_button)

    def registerCustomer(self, email, password):
        self.do_send_keys(self.reg_customer_email, email)
        self.do_send_keys(self.reg_customer_passwd, password)
        self.do_click(self.reg_Cus_btn_signIn)

    def checkRegister(self):
        try:
            x = self.driver.find_element_by_xpath("//div[@class='note note-danger']").text
            if x == "This account name is already taken. Please choose a different account name.":
                print("--This account name is already Registered--")
            else:
                print(x)
                assert False

        except NoSuchElementException:
            print("-----Welcome New User!!-----")

    def checkSignin(self):
        try:
            x = self.driver.find_element_by_xpath("//div[@class='note note-danger']").text
            print(x)
            assert True

        except NoSuchElementException:
            print("*** you sign in sucessfully ***  ")

    def c_sign_in(self):
        self.do_click(self.sign_in)

    def signOut(self):
        self.do_click(self.Sign_out)

    def reg_signIn(self):
        self.do_click(self.reg_customer_signIn)

    def random_generator(self, size=6, chars=string.ascii_lowercase + string.digits):
        return ''.join(random.choice(chars) for x in range(size))

    def welcome_cus(self):
        self.is_visble(self.welcome_header)
