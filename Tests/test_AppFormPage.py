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
    def test_populate_preliminary_info(self):
        self.appForm = AppForm(self.driver)
        self.appForm.fill_preliminary_info()
    def test_populate_elegibility_check_common_criteria(self):
        self.appForm = AppForm(self.driver)
        self.appForm.fill_eligibility_check_common_criteria()
    def test_populate_elegibility_check_k1(self):
        self.appForm = AppForm(self.driver)
        self.appForm.fill_eligibility_check_k1()
    def test_populate_crime_history(self):
        self.appForm = AppForm(self.driver)
        self.appForm.fill_crime_history()
    def test_populate_general_info(self):
        self.appForm = AppForm(self.driver)
        self.appForm.fill_general_information()
