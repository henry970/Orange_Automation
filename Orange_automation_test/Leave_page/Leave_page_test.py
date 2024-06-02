import time

import pytest
from selenium.common import WebDriverException, TimeoutException, ElementClickInterceptedException
from selenium.webdriver import ActionChains
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from Orange_automation_test.LeaveLocators.Leave_page_locators import LeavePageLocators

# class LeavePage:
#     def __init__(self, driver):
#         self.driver = driver
#
#     def click_leave_button(self):
#         click_leave_button = WebDriverWait(self.driver, 20).until(
#              EC.element_to_be_clickable(LeavePageLocators.CLICK_LEAVE_BUTTON))
#         click_leave_button.click()
#         time.sleep(5)

import logging
import time
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException
from Orange_automation_test.LeaveLocators.Leave_page_locators import LeavePageLocators
# Set up logging
logging.basicConfig(filename='test.log', level=logging.INFO,
                    format='%(asctime)s:%(levelname)s:%(message)s')


class LeavePage:
    def __init__(self, driver):
        self.driver = driver

    def click_leave_button(self):
        try:
            # Wait until the leave button is clickable
            logging.info("Waiting for the leave button to be clickable.")
            click_leave_button = WebDriverWait(self.driver, 30).until(
                EC.element_to_be_clickable(LeavePageLocators.CLICK_LEAVE_BUTTON))
            logging.info("Leave button is clickable, proceeding to click it.")

            # Click the leave button
            click_leave_button.click()
            logging.info("Leave button clicked.")

            # Optional: Sleep for 5 seconds to observe the result manually
            time.sleep(5)

        except TimeoutException:
            # Log the error and take a screenshot
            logging.error("Failed to click the leave button - TimeoutException")
            self.driver.save_screenshot('screenshot_failed_click_leave_button.png')
            logging.info("Screenshot taken: screenshot_failed_click_leave_button.png")
