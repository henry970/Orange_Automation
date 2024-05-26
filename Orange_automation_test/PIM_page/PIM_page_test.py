import time

import pytest
from selenium.common import WebDriverException, TimeoutException, ElementClickInterceptedException
from selenium.webdriver import ActionChains
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


from Orange_automation_test.PIMLocators.Pim_page_locators import PImPageLocators


class PIMPage:
    def __init__(self, driver):
        self.driver = driver

    def click_pim_button(self):
        Click_pim_button = WebDriverWait(self.driver, 20).until(
             EC.element_to_be_clickable(PImPageLocators.CLICK_PIM_BUTTON))
        Click_pim_button.click()
        time.sleep(5)


