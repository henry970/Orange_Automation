import pytest
from selenium import webdriver

from Orange_automation_test.Orange_actionPage.ActionPage import LoginPage


@pytest.fixture(scope="module")
def driver_setup():
    driver = webdriver.Chrome()
    driver.implicitly_wait(20)
    driver.maximize_window()
    yield driver
    driver.quit()


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
