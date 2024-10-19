from conftest import sign_in_page, create_promo_page
import allure
import random
import string
from time import sleep


def generate_random_string(length):
    letters = string.ascii_letters + string.digits
    return ''.join(random.choice(letters) for _ in range(length))


@allure.feature('Create text promo')
def test_create_text_promo(sign_in_page, create_promo_page):
    sign_in_page.open_page()
    sign_in_page.fill_login_form('asdasd8', '123qwe')
    sign_in_page.check_dashboard_text('These are the summary of your account')
    create_promo_page.open_promotions_page()
    random_description = generate_random_string(random.randint(5, 10))
    create_promo_page.create_text_promo(random_description)


def test_create_image_promo(sign_in_page, create_promo_page):
    sign_in_page.open_page()
    sign_in_page.fill_login_form('asdasd8', '123qwe')
    sign_in_page.check_dashboard_text('These are the summary of your account')
    create_promo_page.open_promotions_page()
    create_promo_page.create_image_promo()


def test_create_url_promo(sign_in_page, create_promo_page):
    sign_in_page.open_page()
    sign_in_page.fill_login_form('asdasd8', '123qwe')
    sign_in_page.check_dashboard_text('These are the summary of your account')
    create_promo_page.open_promotions_page()
    create_promo_page.create_url_promo()
