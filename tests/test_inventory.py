import pytest

from pages.inventory_page import InventoryPage
from playwright.sync_api import expect

@pytest.mark.smoke
def test_there_is_six_displayed_products(authenticate_page):
    expect(authenticate_page.locator("[data-test=\"inventory-item\"]")).to_have_count(6)

def test_open_and_close_side_bar_menu(authenticate_page):

    inventory_page = InventoryPage(authenticate_page)
    
    inventory_page.click_button("open_menu")
    expect(inventory_page.side_bar_menu).to_be_visible()

    inventory_page.click_button("close_menu")
    expect(inventory_page.side_bar_menu).to_be_hidden()

def test_add_product_to_cart_and_then_remove_it(authenticate_page):
    
    inventory_page = InventoryPage(authenticate_page)
    
    inventory_page.click_button("add_backpack_to_cart")
    expect(inventory_page.shopping_cart_badge_span).to_be_visible()

    inventory_page.click_button("remove_backpack_from_cart")
    expect(inventory_page.shopping_cart_badge_span).to_be_hidden()

@pytest.mark.parametrize(
        "social,social_link",
        [
            pytest.param("twitter","https://x.com/saucelabs",id="twitter"),
            pytest.param("facebook","https://www.facebook.com/saucelabs",id="facebook"),
            pytest.param("linkedin","https://www.linkedin.com/company/sauce-labs/",id="linkedin")
        ]
)
def test_social_buttons(authenticate_page,social,social_link):

    inventory_page = InventoryPage(authenticate_page)

    new_tab = inventory_page.open_social_link(social)
    expect(new_tab).to_have_url(social_link)

@pytest.mark.parametrize(
        "value,option,rev",
        [
            pytest.param("names","za",True,id="Reverse sort by name"),
            pytest.param("prices","lohi",False,id="Sort by price"),
            pytest.param("prices","hilo",True,id="Reverse sort by price"),
            pytest.param("names","az",False,id="Sort by name")
        ]
)
def test_sort_products(authenticate_page,value,option,rev):
    
    inventory_page = InventoryPage(authenticate_page)
    
    before_values = inventory_page.collect_products_and_returns_value(value)

    inventory_page.sort_products(option)

    after_values = inventory_page.collect_products_and_returns_value(value)

    sorted_values = before_values.copy()
    sorted_values.sort(reverse = rev)
    
    assert after_values == sorted_values, (
    f"\nExpected: {sorted_values}\nActual: {after_values}"
)

def test_go_to_cart(authenticate_page):

    inventory_page = InventoryPage(authenticate_page)

    inventory_page.click_button("cart")

    expect(authenticate_page).to_have_url("https://www.saucedemo.com/cart.html")

def test_go_to_about_us(authenticate_page):

    inventory_page = InventoryPage(authenticate_page)

    inventory_page.click_button("open_menu")

    inventory_page.click_button("about_link")
    
    expect(authenticate_page).to_have_url("https://saucelabs.com/")

def test_logout(authenticate_page):
    
    inventory_page = InventoryPage(authenticate_page)

    inventory_page.click_button("open_menu")

    inventory_page.click_button("logout")

    expect(authenticate_page).to_have_url("https://www.saucedemo.com/")

@pytest.mark.known_issue
@pytest.mark.xfail(
    reason="Bug: 'Reset App State' does not fully reset button states; only one of the two buttons is restored.",
    strict=True,
)
def test_reset_app_state(authenticate_page):
    inventory_page = InventoryPage(authenticate_page)

    inventory_page.click_button("add_backpack_to_cart")

    expect(inventory_page.shopping_cart_badge_span).to_be_visible()
    expect(inventory_page.buttons["remove_backpack_from_cart"]).to_be_visible()

    inventory_page.click_button("open_menu")
    inventory_page.click_button("reset_app")

    expect(inventory_page.shopping_cart_badge_span).to_be_hidden()
    expect(inventory_page.buttons["remove_backpack_from_cart"]).to_be_hidden()