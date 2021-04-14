from selenium.webdriver import ActionChains
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.action_chains import ActionChains
"""*****This class is Parent class of all pages******"""
""" It's contains all the generic methods and utlities for all the pages"""

class BasePage:

    def __init__(self,driver):
        self.driver = driver

    def do_click(self, by_locator):
        WebDriverWait(self.driver, 20).until(EC.visibility_of_element_located(by_locator)).click()

    def do_send_keys(self, by_locator, text):
        WebDriverWait(self.driver, 20).until(EC.visibility_of_element_located(by_locator)).send_keys(text)

    def get_element_text(self, by_locator):
        element = WebDriverWait(self.driver, 20).until(EC.visibility_of_element_located(by_locator))
        return element.text

    def is_visible(self, by_locator):
        element = WebDriverWait(self.driver, 15).until(EC.visibility_of_element_located(by_locator))
        return bool(element)

    def get_title(self,title):
        WebDriverWait(self.driver, 20).until(EC.title_is(title))
        return self.driver.title

    def drop_down(self,by_locator):
        element = WebDriverWait(self.driver, 20).until(EC.visibility_of_element_located(by_locator))
        actions = ActionChains(self.driver)
        actions.move_to_element(element).perform()

    def clear_text_field(self,by_locator):
        element = WebDriverWait(self.driver, 20).until((EC.visibility_of_element_located(by_locator)))
        element.clear()


