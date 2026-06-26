from pages.base_page import BasePage
from playwright.sync_api import Page, expect

class InventoryPage(BasePage):
    def __init__(self, page: Page):
        super().__init__(page)

        self.side_bar_menu = page.get_by_text("All ItemsAboutLogoutReset App")
        
        self.sort_btn = page.locator('[data-test="product-sort-container"]')
        
        self.shopping_cart_badge_span = page.locator('[data-test="shopping-cart-badge"]')
        
        self.products=[]
        self.collect_products_and_returns_value()

        self.buttons = {
            "open_menu" : page.get_by_role("button", name="Open Menu"),
            "close_menu" : page.get_by_role("button", name="Close Menu"),
            "about_link" : page.locator('[data-test="about-sidebar-link"]'),
            "reset_app": page.locator('[data-test="reset-sidebar-link"]'),
            "logout" : page.locator('[data-test="logout-sidebar-link"]'),
            "add_backpack_to_cart" : page.locator('[data-test="add-to-cart-sauce-labs-backpack"]'),
            "remove_backpack_from_cart" :  page.locator('[data-test="remove-sauce-labs-backpack"]'),
            "cart" : page.locator('[data-test="shopping-cart-link"]')
        }

        self.social_links = {
        "twitter" :  page.locator('[data-test="social-twitter"]'),
        "facebook" : page.locator('[data-test="social-facebook"]'),
        "linkedin" : page.locator('[data-test="social-linkedin"]')
        }

    def click_button(self,button_name: str):
        button = self.buttons[button_name]
        expect(button).to_be_visible()
        button.click()

    def open_social_link(self,social: str):
        with self.page.expect_popup() as popup_info:
            self.social_links[social].click()
        return popup_info.value

    def sort_products(self,option: str):
        self.sort_btn.select_option(option)

    def collect_products_and_returns_value(self,value: str=""):
        self.products.clear()
        self.products=self.page.locator("[data-test=\"inventory-item\"]").all()
        if value == "names":
            return self._get_products_names()
        elif value == "prices":
            return self._get_products_prices()
        else:
            return

    def _get_products_names(self):
        names=[]
        for product in self.products:
            title=product.locator('[data-test="inventory-item-name"]')
            names.append(title.text_content())
        return names
    
    def _get_products_prices(self):
        prices=[]
        for product in self.products:
            title=product.locator('[data-test="inventory-item-price"]')
            price=title.text_content()
            price=price[1:]
            prices.append(float(price))
        return prices


    
        

        