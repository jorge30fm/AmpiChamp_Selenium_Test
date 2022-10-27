
from selenium.webdriver.common.by import By
from .PageGeneral import BasePage

class LandingPage(BasePage):
    """Methods and properties to navigate the landing page of the application before logging in"""
    getStartedBtn = (By.ID, 'btn_get_started')