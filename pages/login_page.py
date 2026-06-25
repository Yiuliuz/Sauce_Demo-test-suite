from playwright.sync_api import Page, expect
from pages.base_page import BasePage

class LoginPage(BasePage):
   def __init__(self, page: Page):
      super().__init__(page)

      self.input_username = page.locator('[data-test=\"username\"]')
      self.input_password = page.locator("[data-test=\"password\"]")
      self.login_button = page.locator("[data-test=\"login-button\"]")
      self.error_message = page.locator("[data-test=\"error\"]")

   def login(self, username, password):
      self.navigate_to()
      self.fill_username(username)
      self.fill_password(password)
      self.login_button.click()
   
   def fill_username(self,username):
      self.input_username.fill(username)

   def fill_password(self,password):
      self.input_password.fill(password)