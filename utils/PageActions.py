from config.setup_logger import get_logger
import time
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select
from selenium.common.exceptions import TimeoutException, NoSuchElementException, InvalidElementStateException
from sys import exit


class PageActions:
    """Parent class of all pages. Contains all the generic methods and utilities"""
    logger = get_logger(__name__)

    EMAIL_EL = (By.ID, "loginOffcanvasFormLoginEmail")
    PASSWORD_EL = (By.ID, "loginOffcanvasFormLoginPassword")
    LOGIN_BTN_EL = (By.ID, "login_nav_right")
    START_NOW_BTN_EL = (
        By.XPATH, '//*[@id="stickyBlockStartPoint"]/div/div/div[2]/div[2]/button')

    def __init__(self, driver):
        self.driver = driver

    def navigate_to_i129f(self, email, password):
        """Logs in to ampichap and navigates to the form i-129f"""
        self.driver.get("https://novabrains.com/app/7")

        self.do_click(self.START_NOW_BTN_EL)
        self.do_send_keys(self.EMAIL_EL, email)
        self.do_send_keys(self.PASSWORD_EL, password)
        self.do_click(self.LOGIN_BTN_EL)
        time.sleep(1)
        self.driver.get("https://novabrains.com/app/7")
        time.sleep(1)
        self.do_click(self.START_NOW_BTN_EL)
        check_success = self.is_visible((By.ID, "part_full_text_111"))
        self.logger.info('LOGIN SUCCESSFUL')
        return check_success

    def do_click(self, by_locator):
        """Click element on a page based on specified locator"""
        locator_type, locator_identifier = by_locator
        try:
            WebDriverWait(self.driver, 10).until(
                EC.visibility_of_element_located(by_locator)).click()
        except TimeoutException:
            self.logger.error('FAILURE! Element could not be found - ' +
                         locator_type + ' - ' + locator_identifier + ' - CLICK')
            exit(1)
        else:
            self.logger.info('SUCCESS! ' + locator_type + ' - ' +
                        locator_identifier + ' - CLICK')

    def do_send_keys(self, by_locator, text):
        """send keys/text to specified input field"""
        locator_type, locator_identifier = by_locator
        try:
            WebDriverWait(self.driver, 10).until(
                EC.visibility_of_element_located(by_locator)).send_keys(text)
        except TimeoutException:
            self.logger.error('FAILURE! Element could not be found - ' + locator_type +
                         ' - ' + locator_identifier + ': ' + text + '- ENTER TEXT')
            exit(1)
        else:
            self.logger.info('SUCCESS! ' + locator_type + ' - ' +
                         locator_identifier + ': ' + text + '- ENTER TEXT')

    def select_single_item(self, by_locator, selection):
        '''Selects item based on its value attribute from a dropdown list'''
        locator_type, locator_identifier = by_locator
        try:
            element = WebDriverWait(self.driver, 10).until(
                EC.visibility_of_element_located(by_locator))
            select_element = Select(element)
            select_element.select_by_value(selection)
        except TimeoutException:
            self.logger.error('FAILURE! Element could not be found - ' + locator_type + ' - ' + locator_identifier + ' - SELECT DROPDOWN')
            exit(1)
        except NoSuchElementException:
            self.logger.error('FAILURE! Dropdown option could not be found - ' + selection + ' - SELECT DROPDOWN OPTION')
            exit(1)
        else:
            self.logger.info('SUCCESS! ' + selection + ' selected - SELECT DROPDOWN OPTION')

    def clear_field(self, by_locator):
        """clears text on input field"""
        locator_type, locator_identifier = by_locator
        try:
            WebDriverWait(self.driver, 10).until(
                EC.visibility_of_element_located(by_locator)).clear()
        except TimeoutException:
            self.logger.error('FAILURE! Element could not be found - ' +
                         locator_type + ' - ' + locator_identifier + ' - CLEAR TEXT')
            exit(1)
        except InvalidElementStateException:
            self.logger.error('FAILURE! Element is not clearable - ' + locator_type + ' - ' + locator_identifier + ' CLEAR TEXT')
            exit(1)
        else:
             self.logger.info('SUCCESS! ' + locator_type + ' - ' +
                        locator_identifier + ' - CLEAR TEXT')

    def is_visible(self, by_locator):
        """checks if html element is enabled in the page, returns boolean"""
        locator_type, locator_identifier = by_locator
        try:
            element = WebDriverWait(self.driver, 10).until(
                EC.visibility_of_element_located(by_locator))
        except TimeoutException:
            self.logger.error('FAILURE! Element could not be found - ' + locator_type +
                         ' - ' + locator_identifier +  '- CHECK VISIBLE')
            exit(1)
        else:
            self.logger.info('SUCCESS! ' + locator_type + ' - ' +
                         locator_identifier +  '- CHECK VISIBLE')
            return bool(element)

    def get_element(self, by_locator):
        """find element by specified locator"""
        locator_type, locator_identifier = by_locator
        try:
            element = WebDriverWait(self.driver, 10).until(
                EC.visibility_of_element_located(by_locator))
        except TimeoutException:
            self.logger.error('FAILURE! Element could not be found - ' + locator_type +
                         ' - ' + locator_identifier +  '- GET ELEMENT')
            exit(1)
        else:
            self.logger.info('SUCCESS! ' + locator_type + ' - ' +
                         locator_identifier +  '- GET ELEMENT TEXT')
            return element

    def get_element_text(self, by_locator):
        """get text from html based on specified locator"""
        locator_type, locator_identifier = by_locator
        try:
            element = WebDriverWait(self.driver, 10).until(
                EC.visibility_of_element_located(by_locator))
        except TimeoutException:
            self.logger.error('FAILURE! Element could not be found - ' + locator_type +
                         ' - ' + locator_identifier +  '- GET ELEMENT TEXT')
            exit(1)
        else:
            self.logger.info('SUCCESS! ' + locator_type + ' - ' +
                         locator_identifier +  '- GET ELEMENT TEXT')
            return element.text
