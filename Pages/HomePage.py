from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains

from .PageGeneral import BasePage
from .AppOverviewPage import OverviewPage


class HomePage(BasePage):
    """Contains properties and methods that allow navigation to the I-129F application from the navbar"""
    All_APPLICATIONS_LINK = (By.ID, "coursesMegaMenu")
    IMMIGRATION_LINK = (By.ID, "businessMegaMenu")
    I129F_LINK = (By.LINK_TEXT, "app-i129f-4")

    def __init__(self, driver):
        super().__init__(driver)
        self.actions = ActionChains(driver)

    def get_home_page_title(self, title):
        """Get document title of the homepage"""
        return self.get_title(title)

    def is_all_applications_link_exist(self):
        """returns true if link to see all available applications in nav bar exists"""
        return self.is_visible(self.All_APPLICATIONS_LINK)

    def navigate_to_I129F(self):
        all_app_link = self.get_element(self.All_APPLICATIONS_LINK)

        self.actions\
            .move_to_element(all_app_link).perform()
        self.actions\
            .move_to_element(self.get_element(self.IMMIGRATION_LINK)).perform()
        self.actions\
            .click(self.get_element(self.I129F_LINK)).perform()
        return OverviewPage(self.driver)