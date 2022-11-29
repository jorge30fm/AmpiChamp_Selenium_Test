import pandas as pd
from selenium.webdriver.common.by import By
from PageActions import PageActions


class AutomationFileReader(PageActions):
    def read_file(self, file):
        self.df = pd.read_csv(file).sort_values('Sequence', ascending=True)
        return self.df
    def perform_row_actions(self):
        actions = {
            "type": self.do_send_keys,
            "click": self.do_click,
            "clear": self.clear_field
        }
        for i, row in self.df.iterrows():
            id = row['ID']
            if row['input']:
                actions[row['action']]((By.ID, id), row['input'])
            else:
                actions[row['action']]((By.ID, id))
            print(id)
        # for every row in df,get value of id, locate element on browser,check type of action and perform said action
        # if a row fails, save record of that row and continue to the next
        # return list of failures or true if everything passed
