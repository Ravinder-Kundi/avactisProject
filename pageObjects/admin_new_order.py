import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By

from Utilties.readProperties import ReadConfig
from pageObjects.basePage import BasePage

class New_orders(BasePage):
    new_order=(By.CSS_SELECTOR,"  [class='dashboard-stat dashboard-stat-light blue-soft']")
    data_table_order =(By.CSS_SELECTOR,"[id='datatable_orders']")
    menu_order = (By.XPATH,"//li[@id='menu-orders']")
    adminemail = (By.NAME, 'AdminEmail')
    password = (By.NAME, 'Password')
    signin = (By.XPATH, "//button[@type='submit']")
    c_email= (By.CSS_SELECTOR,"[title='Customer Info']")




    def __init__(self,driver):
        super().__init__(driver)

        self.driver.get(ReadConfig.getApplicationURL())

    def do_login(self,username,password):
        self.clear_text_field(self.adminemail)
        self.do_send_keys(self.adminemail,username)
        self.clear_text_field(self.password)
        self.do_send_keys(self.password,password)
        self.do_click(self.signin)



    def click_order_menu(self):
        self.is_visible(self.menu_order)
        self.do_click(self.menu_order)

    def new_order_info(self):
        self.is_visible(self.new_order)
        newo= self.get_element_text(self.new_order)
        print(newo)
    def table_order_data(self):
        self.is_visible(self.data_table_order)
        dto = self.get_element_text(self.c_email)
        print(dto)
