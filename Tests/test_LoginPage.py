import pytest

from Pages.LoginPage import LoginPage
from Tests.test_general import BaseTest
from Config.config import TestData

class Test_Login(BaseTest):
    def test_signup_link_visible(self):
        self.loginPage = LoginPage(self.driver)
        flag = self.loginPage.is_signup_link_exist()
        assert flag
    def test_login_page_title(self):
        self.loginPage = LoginPage(self.driver)
        title = self.loginPage.get_title(TestData.LOGIN_PAGE_TITLE)
        assert title == TestData.LOGIN_PAGE_TITLE
    def test_login(self):
        self.loginPage = LoginPage(self.driver)
        self.loginPage.login(TestData.EMAIL, TestData.PASSWORD)