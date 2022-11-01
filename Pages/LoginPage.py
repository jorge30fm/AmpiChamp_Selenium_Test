from selenium.webdriver.common.by import By

from Config.config import TestData
from .PageGeneral import BasePage
from .HomePage import HomePage

class LoginPage(BasePage):
    """Contains methods and properties to navigate the login page"""
    EMAIL = (By.ID, "signupModalFormLoginEmail")
    PASSWORD = (By.ID, "signupModalFormLoginPassword")
    LOGIN_BTN = (By.CLASS_NAME, "btn-ampichap")
    SIGNUP_LINK = (By.LINK_TEXT, "Sign up here")

    def __init__(self, driver):
        super().__init__(driver)
        self.driver.get(TestData.LOGIN_PAGE_URL)


    def get_login_page_title(self, title):
        """Get document title of the login page"""
        return self.get_title(title)

    def is_signup_link_exist(self):
        """Check if the signup link is visible"""
        return self.is_visible(self.SIGNUP_LINK)

    def login(self, email, password):
        """Used to log in to the application using email and passwrod"""
        self.do_send_keys(self.EMAIL, email)
        self.do_send_keys(self.PASSWORD, password)
        self.do_click(self.LOGIN_BTN)
        return HomePage(self.driver)