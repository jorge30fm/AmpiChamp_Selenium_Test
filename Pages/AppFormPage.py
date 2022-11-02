from selenium.webdriver.common.by import By

from Config.config import TestData
from .PageGeneral import BasePage

class AppForm(BasePage):
    """Automatas filling out the I-129F Form"""
    FIRST_NAME_INPUT = (By.ID, "input_129_4-PrelInf-PrelInf-010")
    def save_continue(self):
        self.do_click((By.CLASS_NAME, "btn-ampichap"))

    def get_app_form_page_title(self, title):
        """Gets title of html page to check we are in the correct application"""
        return self.get_title(title)

    def first_name_input_exists(self):
        """Checks if the first name input is present to make sure we are in the form section"""
        return self.is_visible(self.FIRST_NAME_INPUT)

    def fill_preliminary_info(self):
        """Automates filling out the preliminary info section"""
        self.do_send_keys((By.ID, "input_129_4-PrelInf-PrelInf-010"), "Peter")
        self.do_send_keys((By.ID, "input_129_4-PrelInf-PrelInf-020"), "Jackson")
        self.do_send_keys((By.ID, "input_129_4-PrelInf-PrelInf-030"), "Smith")
        self.do_send_keys((By.ID, "input_129_4-PrelInf-PrelInf-050"), "petersmith@gmail.com")
        self.do_send_keys((By.ID, "input_129_4-PrelInf-PrelInf-060"), "1234567891")
        self.do_send_keys((By.ID, "input_129_4-PrelInf-PrelInf-090"), "Martha")
        self.do_send_keys((By.ID, "input_129_4-PrelInf-PrelInf-100"), "Carmen")
        self.do_send_keys((By.ID, "input_129_4-PrelInf-PrelInf-110"), "Fuentes")
        self.save_continue()

    def fill_eligibility_check_common_criteria(self):
        """Automates filling out the elegibility check common criteria section (Assumes User is US Citizen and Not Married)"""
        self.do_click((By.ID, "lbl_129_4-ElChck-CitMarr-000_Yes"))
        self.do_click((By.ID, "lbl_129_4-ElChck-CitMarr-010_No"))
        self.save_continue()

    def fill_eligibility_check_k1(self):
        """Automates filling out the elegibility check k1 section (assumes petitioner is free to marry, can marry within 90 days, and met fiance at least 2 years prior"""
        self.do_click((By.ID, "lbl_129_4-ElChck-K1-000_Yes"))
        self.do_click((By.ID, "lbl_129_4-ElChck-K1-010_Yes"))
        self.do_click((By.ID, "lbl_129_4-ElChck-K1-020_Yes"))
        self.save_continue()

    def fill_crime_history(self):
        """Automates filling out the crime history portion of the elegibility check. Assumes Client has NOT been arrested or convicted"""
        self.do_click((By.ID, "lbl_129_4-ElChck-CrimHist-000_No"))
        self.save_continue()

    def fill_general_information(self):
        self.do_click((By.ID, "lbl_129_4-PetInf-Gen-000_Male"))
        self.do_send_keys((By.ID, "input_129_4-PetInf-Gen-020e"), "1234567")
        self.do_send_keys((By.ID, "input_129_4-PetInf-Gen-030"), "123456798123")
        self.do_send_keys((By.ID, "input_129_4-PetInf-Gen-040"), "123456789")
        self.save_continue()

    def fill_personal_information(self):

        self.save_continue()

    def fill_birth_information(self):
        self.save_continue()

    def fill_family_information(self):
        self.save_continue()

    def fill_employment_history(self):
        self.save_continue()

    def fill_misc_information(self):
        self.save_continue()

    def fill_citizenship_information(self):
        self.save_continue()

    def fill_petitioner_previous_spouses_list(self):
        self.save_continue()
