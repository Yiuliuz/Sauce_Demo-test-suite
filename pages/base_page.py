from playwright.sync_api import Page


class BasePage:
    def __init__(self,page: Page):
        self.page = page
        self.base_url="https://www.saucedemo.com/"

    def navigate_to(self,path : str= ""):
        url = f"{self.base_url}{path}"
        self.page.goto(url)


