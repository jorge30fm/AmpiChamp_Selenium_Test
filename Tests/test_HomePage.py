import pytest

from selenium.webdriver.common.action_chains import ActionChains

from Tests.test_general import BaseTest
from Pages.LoginPage import LoginPage
from Config.config import TestData
from Pages.HomePage import HomePage


class Test_Home(BaseTest):
    def test_home_page_title(self):
        self.homePage = HomePage(self.driver)
        self.loginPage = LoginPage(self.driver)
        self.homePage = self.loginPage.login(TestData.EMAIL, TestData.PASSWORD)
        title = self.homePage.get_title(TestData.HOME_PAGE_TITLE)
        assert title == TestData.HOME_PAGE_TITLE

    def test_is_all_app_link_visible(self):
        self.homePage = HomePage(self.driver)
        flag = self.homePage.is_all_applications_link_exist()
        assert flag
    def test_navigate_to_i129f(self):
        self.homePage = HomePage(self.driver)
        self.homePage.navigate_to_I129F()

