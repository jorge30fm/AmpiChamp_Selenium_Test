import pytest
from selenium.webdriver.common.by import By

from test_general import BaseTest
from PageActions import PageActions
from Automation_File_Reader import AutomationFileReader

class Test_Form_Automation(BaseTest):
    def test_navigate_to_i129f(self):
        self.pageActions =  PageActions(self.driver)
        form_desc= self.pageActions.navigate_to_i129f("jorge30fm@gmail.com","Test123!")
        # assert form_desc == "This app will help you bring your fiancé(e) or spouse to the United States. Check if you're eligible and follow simple steps to complete your application."
        assert form_desc
    def test_file_reader(self):
        self.file_reader = AutomationFileReader(self.driver)
        self.file_reader.read_file('automationfile.csv')
        self.file_reader.perform_row_actions()
        assert True


#Iterate overy every row to make sure each row is being read

#Open application on browser
#Locate element on page based on specified row
#Check input type
#Send text to input
#Click on element


