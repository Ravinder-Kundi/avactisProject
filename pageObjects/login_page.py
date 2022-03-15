from selenium.webdriver.common.by import By

from Utilties.readProperties import ReadConfig
from pageObjects.basePage import BasePage


class LoginPage(BasePage):
    # Admin Login page by locator####
    adminemail = (By.NAME, 'AdminEmail')
    password = (By.NAME, 'Password')
    signin = (By.XPATH, "//button[@type='submit']")
    link_signout_linktext = (By.CSS_SELECTOR, "[title='Sign Out']")
    homepage_title = (By.XPATH, '//h3')
    link_click_here = (By.ID, 'forget-password')
    dropdown = (By.XPATH, "//a[@class='dropdown-toggle']")

    def __init__(self, driver):
        super().__init__(driver)

        self.driver.get(ReadConfig.getApplicationURL())

    """ this is to get page title """

    def get_home_page_title(self, title):
        return self.get_title(title)

    """this is to check forget password link """

    def is_forget_password_link_exist(self):
        return self.is_visible(self.link_click_here)

    """ this is Admin login in """

    def do_login(self, username, password):
        self.clear_text_field(self.adminemail)
        self.do_send_keys(self.adminemail, username)
        self.clear_text_field(self.password)
        self.do_send_keys(self.password, password)
        self.do_click(self.signin)

    # sign out from Admin page
    def sign_out(self):
        self.drop_down(self.dropdown)
        self.do_click(self.link_signout_linktext)
