import pytest
from selenium.webdriver.common.by import By

from test_general import BaseTest
from PageActions import PageActions
from Automation_File_Reader import AutomationFileReader

class Test_Form_Automation(BaseTest):
    def test_navigate_to_i129f(self):
        self.pageActions =  PageActions(self.driver)  # type: ignore
        form_desc= self.pageActions.navigate_to_i129f("jorge30fm@gmail.com","Test123!")
        assert form_desc
    def test_file_reader(self):
        self.file_reader = AutomationFileReader(self.driver)  # type: ignore
        self.file_reader.read_file('automationfile.csv')
        self.file_reader.perform_row_actions()
        assert True

# TODO:
# allow blank lines in csv /comments - done

# waits and wait column
# excecute row - success
# if element is on the screen
# if field gets saved
# go back assert value of input
# generate log/report
# screenshots



#asserts, waits, logs, screenshots





