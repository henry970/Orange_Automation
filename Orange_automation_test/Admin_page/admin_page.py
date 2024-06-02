import logging
import time
from datetime import datetime

from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException, NoSuchElementException

from Orange_automation_test.AdminLocators.Admin_page_locators import AdminPageLocators


class AdminPage:
    def __init__(self, driver):
        self.driver = driver

    def click_admin_button(self):
        Click_admin_button = WebDriverWait(self.driver, 20).until(
            EC.element_to_be_clickable(AdminPageLocators.CLICK_ADMIN_BUTTON))
        Click_admin_button.click()
        time.sleep(5)
