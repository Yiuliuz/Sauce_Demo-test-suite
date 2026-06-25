import pytest
from pages.login_page import LoginPage
from playwright.sync_api import Page,expect


@pytest.mark.smoke
def test_login_as_standard_user(page: Page, credentials):
    login_page = LoginPage(page)
    login_page.login(*credentials)
    expect(page).to_have_url("https://www.saucedemo.com/inventory.html")

@pytest.mark.smoke
def test_user_field_can_be_filled(page: Page):
    login_page = LoginPage(page)
    login_page.navigate_to()
    login_page.fill_username("TESTING")
    expect(login_page.input_username).to_have_value("TESTING")

@pytest.mark.smoke
def test_password_field_can_be_filled(page: Page):
    login_page = LoginPage(page)
    login_page.navigate_to()
    login_page.fill_password("TESTING")
    expect(login_page.input_password).to_have_value("TESTING")

@pytest.mark.smoke
@pytest.mark.negative
def test_login_with_wrong_creds(page: Page):
    login_page = LoginPage(page)
    login_page.login("WRONG","CREDS")
    expect(page).to_have_url(login_page.base_url)
    expect(login_page.error_message).to_be_visible()
    expect(login_page.error_message).to_contain_text("Username and password do not match any user in this service")

@pytest.mark.smoke
@pytest.mark.negative
def test_login_with_missing_username(page: Page):
    login_page = LoginPage(page)
    login_page.login("","MISSINGUSERNAME")
    expect(page).to_have_url(login_page.base_url)
    expect(login_page.error_message).to_be_visible()
    expect(login_page.error_message).to_contain_text("Username is required")

@pytest.mark.smoke
@pytest.mark.negative
def test_login_with_missing_password(page: Page):
    login_page = LoginPage(page)
    login_page.login("MISSINGPASSWORD","")
    expect(page).to_have_url(login_page.base_url)
    expect(login_page.error_message).to_be_visible()
    expect(login_page.error_message).to_contain_text("Password is required")