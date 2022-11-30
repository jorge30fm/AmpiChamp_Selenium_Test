import pandas as pd
import numpy as np
import time
from selenium.webdriver.common.by import By
from PageActions import PageActions


class AutomationFileReader(PageActions):
    def read_file(self, filename):
        '''Read csv file, sort by sequence number in ascending order and drop any empty rows'''
        self.df = pd.read_csv(filename, skip_blank_lines=True, comment='#').sort_values('Sequence', ascending=True)
        self.df.dropna(how="all", inplace=True)
        print(self.df)
        return self.df

    def perform_row_actions(self):
        '''Reads each row in the dataframe, finds element on browser with specified locator, and performs action stated in df (type, click, select, etc)'''
        actions = {
            "type": self.do_send_keys,
            "click": self.do_click,
            "clear": self.clear_field,
            "select": self.select_single_item
        }

        for i, row in self.df.iterrows():
            locator_type = {
                "ID": (By.ID, row['Locator']),
                "CLASS": (By.CLASS_NAME, row['Locator'])
            }
            locator = locator_type[row['Locator Type']]

            # check if there is an input cell to pass as an argument
            if pd.isnull(row['input']):
                actions[row['action']](locator)
            else:
                print(row['input'])
                actions[row['action']](locator, row['input'])

            # waits 1 second before moving on to next row unless specified to wait longer in the dfg
            if pd.isnull(row['Wait']):
                time.sleep(1)
            else:
                time.sleep(row['Wait'])
        # for every row in df,get value of id, locate element on browser,check type of action and perform said action
        # if a row fails, save record of that row and continue to the next
        # return list of failures or true if everything passed
