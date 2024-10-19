from conftest import sign_in_page
import allure


@allure.feature('Incorrect login')
def test_incorrect_login(sign_in_page):
    sign_in_page.open_page()
    sign_in_page.fill_login_form('fasdoifj', 'asodjknf')
    sign_in_page.check_error_alert_text_is(
        'Incorrect username/email or password.'
    )


@allure.feature('Correct login')
def test_correct_login(sign_in_page):
    sign_in_page.open_page()
    sign_in_page.fill_login_form('asdasd8', '123qwe')
    sign_in_page.check_dashboard_text('These are the summary of your account')
