"""GUI TESTING AUTOMATION CODE USING SELENIUM"""
from selenium import webdriver

# webdriver is an API (application programming interface)
from selenium.webdriver.chrome.service import Service as ChromeService

from selenium.webdriver import ChromeOptions
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from webdriver_manager.chrome import ChromeDriverManager

#keep browser open even if script is done running
chrome_options = ChromeOptions()
chrome_options.add_experimental_option("detach", True)

driver = webdriver.Chrome(
    options=chrome_options,
    service=ChromeService(ChromeDriverManager().install())
)

driver.get("https://novabrains.com/") #AUT link

driver.maximize_window()

print('Driver title:', driver.title)
print('Driver name', driver.name)
print('Driver URL', driver.current_url)


getStartedBtn = driver.find_element(By.ID, 'btn_get_started')
getStartedBtn.click()

WebDriverWait(driver, 5).until(EC.url_changes(driver.current_url))

print(driver.current_url)

if driver.current_url == "https://novabrains.com/login/":
    print('Get Started Button Working')
else:
    print('Get Started Button NOT Working')


# driver.get("https://novabrains.com/login/")
# login_email = driver.find_element(By.ID, 'signupModalFormLoginEmail')
# print(login_email)
# driver.quit()
