import time
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select


class PageActions:
    """Parent class of all pages. Contains all the generic methods and utilities"""

    EMAIL_EL = (By.ID, "loginOffcanvasFormLoginEmail")
    PASSWORD_EL = (By.ID, "loginOffcanvasFormLoginPassword")
    LOGIN_BTN_EL = (By.ID, "login_nav_right")
    START_NOW_BTN_EL = (
        By.XPATH, '//*[@id="stickyBlockStartPoint"]/div/div/div[2]/div[2]/button')

    def __init__(self, driver):
        self.driver = driver

    def navigate_to_i129f(self, email, password):
        """Navigate to the form i-129f """
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
        return check_success

    def do_click(self, by_locator):
        """Click element on a page based on specified locator"""
        WebDriverWait(self.driver, 20).until(
            EC.visibility_of_element_located(by_locator)).click()

    def do_send_keys(self, by_locator, text):
        """send keys/text to specified input field"""
        WebDriverWait(self.driver, 10).until(
            EC.visibility_of_element_located(by_locator)).send_keys(text)

    def select_single_item(self, by_locator, selection):
        element = WebDriverWait(self.driver, 10).until(
            EC.visibility_of_element_located(by_locator))
        select_element = Select(element)
        select_element.select_by_value(selection)

    def clear_field(self, by_locator):
        """clears text on input field"""
        WebDriverWait(self.driver, 10).until(
            EC.visibility_of_element_located(by_locator)).clear()

    def is_visible(self, by_locator):
        """checks if html element is enabled in the page, returns boolean"""
        element = WebDriverWait(self.driver, 10).until(
            EC.visibility_of_element_located(by_locator))
        return bool(element)

    def get_element(self, by_locator):
        """find element by specified locator"""
        element = WebDriverWait(self.driver, 10).until(
            EC.visibility_of_element_located(by_locator))
        return element

    def get_element_text(self, by_locator):
        """get text from html based on specified locator"""
        element = WebDriverWait(self.driver, 10).until(
            EC.visibility_of_element_located(by_locator))
        return element.text
