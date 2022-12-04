import pytest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.firefox.service import Service as FirefoxService
from webdriver_manager.chrome import ChromeDriverManager
from webdriver_manager.firefox import GeckoDriverManager


@pytest.fixture(params=["chrome"], scope="class")
def init_driver(request):
    '''initializes selenium driver for chrome'''
    # TODO: set up other browser web drivers (firefox, safari, edge)
    web_driver = webdriver.Chrome(
        service=ChromeService(ChromeDriverManager().install()))
    # if request.param =="firefox":
    #     web_driver = webdriver.Firefox(service=FirefoxService(GeckoDriverManager().install()))
    request.cls.driver = web_driver
    yield
