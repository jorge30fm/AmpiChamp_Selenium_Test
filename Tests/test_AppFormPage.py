import pytest

from Tests.test_general import BaseTest
from Pages.LoginPage import LoginPage
from Config.config import TestData
from Pages.HomePage import HomePage
from Pages.AppFormPage import AppForm

class Test_AppForm(BaseTest):
    def test_appform_page_title(self):
        self.loginPage = LoginPage(self.driver)
        self.homePage = self.loginPage.login(TestData.EMAIL, TestData.PASSWORD)
        self.overviwPage= self.homePage.navigate_to_I129F()
        self.appForm = self.overviwPage.do_start_application()
        title = self.appForm.get_title(TestData.APP_FORM_TITLE)
        assert title == TestData.APP_FORM_TITLE
    def test_first_name_input_exists(self):
        self.appForm = AppForm(self.driver)
        flag = self.appForm.first_name_input_exists()
        assert flag