import time

import pytest
from selenium.common import WebDriverException, TimeoutException, ElementClickInterceptedException
from selenium.webdriver import ActionChains
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from Orange_automation_test.TimeLocators.Time_page_locators import TimePageLocators


class TimePage:
    def __init__(self, driver):
        self.driver = driver

    def click_time_button(self):
        click_time_button = WebDriverWait(self.driver, 20).until(
             EC.element_to_be_clickable(TimePageLocators.CLICK_TIME_BUTTON))
        click_time_button.click()
        time.sleep(5)


