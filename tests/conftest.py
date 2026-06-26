import pytest
from config.enviroment import (SAUCE_STANDARD_USERNAME,SAUCE_PASSWORD)
from pages.login_page import LoginPage
from playwright.sync_api import Page, expect

@pytest.fixture
def credentials():
    username=SAUCE_STANDARD_USERNAME
    password=SAUCE_PASSWORD
    return [username,password]

@pytest.fixture
def authenticate_page(page: Page,credentials):
    login_page = LoginPage(page)
    login_page.login(*credentials)
    expect(page).to_have_url("https://www.saucedemo.com/inventory.html")
    return login_page.page