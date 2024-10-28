from conftest import sign_in_page
import allure
from time import sleep


@allure.feature('Incorrect Login')
@allure.description('Проверка логина с неверным паролем')
def test_incorrect_login(sign_in_page):
    sign_in_page.open_page()
    sign_in_page.fill_login_form('asdasd8', 'asodjknf')
    sign_in_page.check_error_alert_text_is()


@allure.feature('Correct Login Advertiser')
@allure.description('Проверка логина рекламного юзера')
def test_login_advertiser(sign_in_page):
    sign_in_page.open_page()
    sign_in_page.fill_login_form('asdasd8', '123qwe')
    sign_in_page.check_dashboard_text()


@allure.feature('Correct Login Regular')
@allure.description('Проверка логина обычного юзера')
def test_login_regular(sign_in_page):
    sign_in_page.open_page()
    sign_in_page.fill_login_form('check6047o', '123qwe')
    sign_in_page.check_search_input_after_login()


@allure.feature('Login with empty password, check error message')
@allure.description('Проверка входа с пустым паролем, и алерта')
def test_empty_password_login(sign_in_page):
    sign_in_page.open_page()
    sign_in_page.fill_login_form('asdasd8', '')
    sign_in_page.check_error_message_empty_pw()


@allure.feature('Login with empty login, check error message')
@allure.description('Проверка входа с пустым логином, и алерта')
def test_empty_login(sign_in_page):
    sign_in_page.open_page()
    sign_in_page.fill_login_form('', '123qwe')
    sign_in_page.check_error_message_empty_login()
