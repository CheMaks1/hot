# from playwright.sync_api import BrowserContext
import pytest
from pages.advertiser_login import AdvertiserLogin
from pages.create_promo_page import PromoPage
from playwright.sync_api import sync_playwright


@pytest.fixture(scope="session")
def playwright():
    with sync_playwright() as p:
        yield p


@pytest.fixture(scope="session")
def browser(playwright):
    browser = playwright.chromium.launch(headless=True)
    yield browser
    browser.close()


@pytest.fixture(scope="function")
def context(browser):
    context = browser.new_context()
    yield context
    context.close()


@pytest.fixture()
def sign_in_page(context):
    page = context.new_page()
    yield AdvertiserLogin(page)
    page.close()


@pytest.fixture()
def create_promo_page(context):
    page = context.new_page()
    yield PromoPage(page)
    page.close()

# @pytest.fixture()
# def page(context: BrowserContext, playwright):
#     playwright.selectors.set_test_id_attribute("id")
#     page = context.new_page()
#     page.set_viewport_size({'width': 1920, 'height': 1080})
#     return page
