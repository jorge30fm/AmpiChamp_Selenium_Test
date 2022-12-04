from config.setup_logger import get_logger
import pandas as pd
import time, datetime
from utils.util import create_screenshot_directory
from selenium.webdriver.common.by import By
from utils.PageActions import PageActions

class AutomationFileReader(PageActions):
    '''Contains methods to read csv file and iterate throwgh its rows to perform the automation'''

    #set up the log file
    logger = get_logger(__name__)

    def read_file(self, filename):
        '''Read csv file, sort by sequence number in ascending order and drop any empty rows'''
        self.df = pd.read_csv(filename, skip_blank_lines=True, comment='#').sort_values('Sequence', ascending=True)
        self.df.dropna(how="all", inplace=True)
        return self.df

    def perform_row_actions(self):
        '''Reads each row in the dataframe, finds element on browser with specified locator, and performs action stated in df (type, click, select, etc). Logs the sequence number of each row to the log file to keep track of each step. Checks if row action requires a screenshot and saves the jpeg file to a newly created directory'''
        actions = {
            "type": self.do_send_keys,
            "click": self.do_click,
            "clear": self.clear_field,
            "select": self.select_single_item,
            "get text": self.get_element_text
        }
        #creates directory to save screenshot files
        screenshot_folder_path = create_screenshot_directory()

        # iterate throw rows in dataframe to perform row actions
        for i, row in self.df.iterrows():
            # log sequence number to keep track of each automation step
            self.logger.info('SN: ' + str(row['Sequence']))

            locator_type = {
                "ID": (By.ID, row['Locator']),
                "CLASS": (By.CLASS_NAME, row['Locator']),
                "XPATH": (By.XPATH, row['Locator'])
            }
            locator = locator_type[row['Locator Type']]

            # check if there is an input cell to pass as an argument to the send keys function
            if pd.isnull(row['input']):
                actions[row['action']](locator)
            else:
                actions[row['action']](locator, row['input'])

            # checks if cell requires a screenshot
            if row['Screenshot'] == 'Yes':
                #name screenshot file with timestamp
                file_name = str(row['Sequence']) + '-' + datetime.datetime.now().strftime('%Y-%m-%d_%H-%M-%S' + '.jpeg')
                file_path = screenshot_folder_path + '/' + file_name

                self.driver.save_screenshot(file_path)

            # waits 1 second before moving on to next row unless specified to wait longer in the dfg
            if pd.isnull(row['Wait']):
                time.sleep(0)
            else:
                time.sleep(row['Wait'])

