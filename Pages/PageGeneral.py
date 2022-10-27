from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class BasePage:
    """Parent class of all pages. Contains all the generic methods and utilities"""
    def __init__(self, driver):
        self.driver = driver

    def do_click(self, by_locator):
        """Click element on a page based on specified locator"""
        WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located(by_locator)).click()

    def do_send_keys(self, by_locator, text):
        """send keys/text to specified input field"""
        WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located(by_locator)).send_keys(text)

    def get_element_text(self, by_locator):
        """get text from html based on specified locator"""
        element = WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located(by_locator))
        return element.text

    def get_title(self, title):
        """get the title of the html page"""
        WebDriverWait(self.driver, 10).until(EC.title_is(title))
        return self.driver.title

    def is_visible(self, by_locator):
        """checks if html element is enabled in the page, returns boolean"""
        element = WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located(by_locator))
        return bool(element)
