import pytest
from pages.advertiser_login import AdvertiserLogin
from pages.create_promo_page import PromoPage


@pytest.fixture()
def sign_in_page(page):
    return AdvertiserLogin(page)


@pytest.fixture()
def create_promo_page(page):
    return PromoPage(page)
