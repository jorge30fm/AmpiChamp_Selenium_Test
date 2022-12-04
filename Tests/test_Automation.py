
import os
from selenium.webdriver.common.by import By
from test_general import BaseTest
from utils.PageActions import PageActions
from utils.Automation_File_Reader import AutomationFileReader
from dotenv import load_dotenv

load_dotenv()

class Test_Form_Automation(BaseTest):
    def test_navigate_to_i129f(self):
        '''test if automation script can log in and navigate to I-129F'''
        self.pageActions =  PageActions(self.driver)  # type: ignore
        email = os.environ.get("EMAIL")
        password = os.environ.get("PASSWORD")
        form_desc= self.pageActions.navigate_to_i129f(email, password)
        assert form_desc

    def test_file_reader(self):
        '''tests if script can read csv file and perform the automation actions'''
        self.file_reader = AutomationFileReader(self.driver)  # type: ignore
        self.file_reader.read_file('automation_files/automationfile.csv')
        self.file_reader.perform_row_actions()



# TODO:




# if field gets saved
# go back assert value of input

# screenshots

#asserts, logs, screenshots





