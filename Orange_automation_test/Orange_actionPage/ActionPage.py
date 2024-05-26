import logging
import time

import pytest
from selenium.common import WebDriverException, TimeoutException, ElementClickInterceptedException
from selenium.webdriver import ActionChains
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from Orange_automation_test.OrangeLocatorPgae.loginLocators import ActionPageLocators


class LoginPage:
    def __init__(self, driver):
        self.driver = driver

    def open_login_page(self, url):
        self.driver.get(url)

    def enter_username(self, username):
        username_field = WebDriverWait(self.driver, 20).until(
            EC.presence_of_element_located(ActionPageLocators.USERNAME_FIELD))
        username_field.send_keys(username)

    def enter_password(self, password):
        password_field = WebDriverWait(self.driver, 20).until(
            EC.presence_of_element_located(ActionPageLocators.PASSWORD_FIELD))
        password_field.send_keys(password)

    def click_login_button(self):
        login_button = WebDriverWait(self.driver, 20).until(
            EC.element_to_be_clickable(ActionPageLocators.LOGIN_BUTTON))
        login_button.click()
        time.sleep(20)
