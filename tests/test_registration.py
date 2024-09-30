from time import sleep
from pages.advertiser_signup import AdvertiserSignup


def test_incorrect_login(driver):
    signup_page = AdvertiserSignup(driver)
    signup_page.open_signup_page()
    signup_page.fill_signup_form(
        'testusername',
        'testusername@gmail.com',
        'testusername',
        '123qwe',
        '123qwe'
    )
    sleep(5)