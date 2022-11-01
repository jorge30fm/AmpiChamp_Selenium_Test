import pytest



from .test_general import BaseTest
from Config.config import TestData
from Pages.AppOverviewPage import OverviewPage
from Pages.LoginPage import LoginPage
from Pages.HomePage import HomePage

class Test_App_Overview(BaseTest):
    def test_app_overview_page_title(self):
        self.overviewPage = OverviewPage(self.driver)
        LoginPage(self.driver).login(TestData.EMAIL, TestData.PASSWORD)
        HomePage(self.driver).navigate_to_I129F()
        title =  self.overviewPage.get_overview_page_title(TestData.I129F_OVERVIEW_PAGE_TITLE)
        assert title == TestData.I129F_OVERVIEW_PAGE_TITLE
    def test_start_now_btn_exists(self):
        self.overviewPage = OverviewPage(self.driver)
        flag = self.overviewPage.start_now_btn_exists()
        assert flag
    def tet_start_app(self):
        self.overviewPage = OverviewPage(self.driver)
        self.overviewPage.do_start_application()