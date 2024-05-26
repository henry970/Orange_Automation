import time

import pytest
from selenium.common import WebDriverException, TimeoutException, ElementClickInterceptedException
from selenium.webdriver import ActionChains
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from Orange_automation_test.AdminLocators.Admin_page_locators import AdminPageLocators


class AdminPage:
    def __init__(self, driver):
        self.driver = driver

    def click_admin_button(self):
        Click_admin_button = WebDriverWait(self.driver, 20).until(
             EC.element_to_be_clickable(AdminPageLocators.CLICK_ADMIN_BUTTON))
        Click_admin_button.click()
        time.sleep(5)


