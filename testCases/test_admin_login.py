from pageObjects.login_page import LoginPage
from Utilties.readProperties import ReadConfig
from testCases.base_test import BaseTest
from Utilties.customLogger import LogGen
import allure
from allure_commons.types import AttachmentType

class Test_login(BaseTest):

    adminEmail = ReadConfig.getUserEmail()
    password = ReadConfig.getPassword()
    title = ReadConfig.getPageTitle()
    logger = LogGen.loggen()

    @allure.severity(allure.severity_level.MINOR)
    def test_click_here(self):
        #self.logger = LogGen.loggen()
        self.logger.info("*************Test_Login***************")
        self.logger.info("*************verifying_click_here***************")
        self.loginPage = LoginPage(self.driver)
        flag =self.loginPage.is_forget_password_link_exist()
        assert flag
        self.driver.save_screenshot(".\\Screenshots\\" + "test_click_here.png")
        self.logger.info("*************Pass_click_here***************")
        allure.attach(self.driver.get_screenshot_as_png(), name=" Test Click here screen", attachment_type=AttachmentType.PNG)

    @allure.severity(allure.severity_level.CRITICAL)
    def test_login_in(self):
        self.logger.info("*************Test_Login _in***************")
        self.logger.info("*************Verifying Login In***************")
        self.loginPage = LoginPage(self.driver)
        self.loginPage.do_login(self.adminEmail,self.password)
        self.driver.save_screenshot(".\\Screenshots\\" + "test_Login.png")
        self.logger.info("*************Pass Login in test***************")
        allure.attach(self.driver.get_screenshot_as_png(), name="Test login screen", attachment_type=AttachmentType.PNG)

    @allure.severity(allure.severity_level.CRITICAL)
    def test_Home_page_title(self):
        self.logger.info("*************Test Home page title ***************")
        self.logger.info("*************Verifying Home Page Title ***************")
        self.loginPage = LoginPage(self.driver)
        self.loginPage.do_login(self.adminEmail, self.password)
        act_title = self.loginPage.get_home_page_title(self.title)
        if act_title == self.title:
            assert True
            self.driver.close()
            self.logger.info("*************Home Page title test is pass***************")

        else:
            self.driver.save_screenshot(".\\Screenshots\\"+"test_Loginpage_title_is failed.png")
            self.driver.close()
            self.logger.error("*************Home Page title test is failed***************")
            allure.attach(self.driver.get_screenshot_as_png(), name=" Home Page title test is failed ",
                          attachment_type=AttachmentType.PNG)
            assert False
