from config.setup_logger import get_logger
import pandas as pd
import time, datetime
from utils.util import create_screenshot_directory
from selenium.webdriver.common.by import By
from utils.PageActions import PageActions

class AutomationFileReader(PageActions):
    logger = get_logger(__name__)
    def read_file(self, filename):
        '''Read csv file, sort by sequence number in ascending order and drop any empty rows'''
        self.df = pd.read_csv(filename, skip_blank_lines=True, comment='#').sort_values('Sequence', ascending=True)
        self.df.dropna(how="all", inplace=True)
        return self.df

    def perform_row_actions(self):
        '''Reads each row in the dataframe, finds element on browser with specified locator, and performs action stated in df (type, click, select, etc)'''
        actions = {
            "type": self.do_send_keys,
            "click": self.do_click,
            "clear": self.clear_field,
            "select": self.select_single_item,
            "get text": self.get_element_text
        }
        screenshot_folder_path = create_screenshot_directory()
        for i, row in self.df.iterrows():
            self.logger.info('SN: ' + str(row['Sequence']))
            locator_type = {
                "ID": (By.ID, row['Locator']),
                "CLASS": (By.CLASS_NAME, row['Locator']),
                "XPATH": (By.XPATH, row['Locator'])
            }
            locator = locator_type[row['Locator Type']]

            # check if there is an input cell to pass as an argument
            if pd.isnull(row['input']):
                actions[row['action']](locator)
            else:
                actions[row['action']](locator, row['input'])

            if row['Screenshot'] == 'Yes':
                file_name = str(row['Sequence']) + '-' + datetime.datetime.now().strftime('%Y-%m-%d_%H-%M-%S' + '.jpeg')
                file_path = screenshot_folder_path + '/' + file_name
                print(file_path)
                self.driver.save_screenshot(file_path)
            # waits 1 second before moving on to next row unless specified to wait longer in the dfg
            if pd.isnull(row['Wait']):
                time.sleep(0)
            else:
                time.sleep(row['Wait'])
        # for every row in df,get value of id, locate element on browser,check type of action and perform said action
        # if a row fails, save record of that row and continue to the next
        # return list of failures or true if everything passed
