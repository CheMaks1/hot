# from playwright.sync_api import BrowserContext
import pytest
from pages.advertiser_login import AdvertiserLogin
from pages.create_promo_page import PromoPage


@pytest.fixture()
def sign_in_page(page):
    return AdvertiserLogin(page)


@pytest.fixture()
def create_promo_page(page):
    return PromoPage(page)

# @pytest.fixture()
# def page(context: BrowserContext, playwright):
#     playwright.selectors.set_test_id_attribute("id")
#     page = context.new_page()
#     page.set_viewport_size({'width': 1920, 'height': 1080})
#     return page
