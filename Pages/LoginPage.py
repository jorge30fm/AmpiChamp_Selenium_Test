from selenium.webdriver.common.by import By
from .PageGeneral import BasePage

class LoginPage(BasePage):
    """Contains methods and properties to navigate the login page"""
    EMAIL = (By.ID, "signupModalFormLoginEmail")
    PASSWORD = (By.ID, "signupModalFormLoginPassword")
    LOGIN_BTN = (By.CLASS_NAME, "btn-ampichap")
    SIGNUP_LINK = (By.LINK_TEXT, "Sign up here")

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