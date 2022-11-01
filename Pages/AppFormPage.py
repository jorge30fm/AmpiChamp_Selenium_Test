from selenium.webdriver.common.by import By

from Config.config import TestData
from .PageGeneral import BasePage

class AppForm(BasePage):
    FIRST_NAME_INPUT = (By.ID, "input_129_4-PrelInf-PrelInf-010")
    def get_app_form_page_title(self, title):
        return self.get_title(title)
    def first_name_input_exists(self):
        return self.is_visible(self.FIRST_NAME_INPUT)