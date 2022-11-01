from selenium.webdriver.common.by import By

from Config.config import TestData
from .PageGeneral import BasePage
from .AppFormPage import AppForm

class OverviewPage(BasePage):
    """Contains methods and properties to navigate I-129F Application Overview Page"""
    START_NOW_BTN = (By.CLASS_NAME, 'btn-ampichap')

    def get_overview_page_title(self, title):
        """Get document title of the overview page of I-129F form"""
        return self.get_title(title)
    def start_now_btn_exists(self):
        """Check if the start now button is visible"""
        return self.is_visible(self.START_NOW_BTN)
    def do_start_application(self):
        """Click start now button to start application"""
        self.do_click(self.START_NOW_BTN)
        return AppForm(self.driver)