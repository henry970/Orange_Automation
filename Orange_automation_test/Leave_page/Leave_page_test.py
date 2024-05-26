import time

import pytest
from selenium.common import WebDriverException, TimeoutException, ElementClickInterceptedException
from selenium.webdriver import ActionChains
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from Orange_automation_test.LeaveLocators.Admin_page_locators import LeavePageLocators


class LeavePage:
    def __init__(self, driver):
        self.driver = driver

    def click_leave_button(self):
        click_leave_button = WebDriverWait(self.driver, 20).until(
             EC.element_to_be_clickable(LeavePageLocators.CLICK_LEAVE_BUTTON))
        click_leave_button.click()
        time.sleep(5)


