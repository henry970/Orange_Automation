import pytest
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager

from Orange_automation_test.Admin_page.admin_page import AdminPage
from Orange_automation_test.Leave_page.Leave_page_test import LeavePage
from Orange_automation_test.Orange_actionPage.ActionPage import LoginPage
from Orange_automation_test.PIM_page.PIM_page_test import PIMPage


@pytest.fixture(scope="module")
def driver_setup():
    chrome_options = Options()
    chrome_options.add_argument("--headless")
    chrome_options.add_argument("--no-sandbox")
    chrome_options.add_argument("--disable-dev-shm-usage")
    chrome_options.add_argument("--disable-gpu")
    chrome_options.add_argument("--window-size=1920x1080")

    driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=chrome_options)
    driver.implicitly_wait(20)
    yield driver
    driver.quit()


#
# @pytest.fixture(scope="module")
# def driver_setup():
#     driver = webdriver.Chrome()
#     driver.implicitly_wait(20)
#     driver.maximize_window()
#     yield driver
#     driver.quit()


@pytest.fixture(scope="module")
def login(driver_setup):
    driver = driver_setup
    login_page = LoginPage(driver)
    login_page.open_login_page("https://opensource-demo.orangehrmlive.com/web/index.php/auth/login")
    return login_page


def test_login_page_on_orange_website(login):
    login.enter_username("Admin")
    login.enter_password("admin123")
    login.click_login_button()


# Admin page test
def test_admin_page_on_orange_website(login):
    test_Admin_page = AdminPage(login.driver)
    test_Admin_page.click_admin_button()


# Admin page test
def test_Pim_page_on_orange_website(login):
    test_Pim_page = PIMPage(login.driver)
    test_Pim_page.click_pim_button()


# Leave button
def test_leave_page_on_orange_website(login):
    test_leave_page = LeavePage(login.driver)
    test_leave_page.click_leave_button()
