from playwright.sync_api import expect
from pages.locators import login_locators as loc
from pages.base_page import BasePage


class AdvertiserLogin(BasePage):
    db_text = 'These are the summary of your account'
    inc_log_text = 'Incorrect username/email or password.'

    def check_error_alert_text_is(self):
        error_alert_text = self.page.locator(loc.error_alert_text_loc)
        expect(error_alert_text).to_have_text(self.inc_log_text)

    def check_dashboard_text(self):
        dashboard_text = self.page.locator(loc.dashboard_text_loc)
        expect(dashboard_text).to_be_visible(timeout=15000)
        expect(dashboard_text).to_have_text(self.db_text)

    def check_search_input_after_login(self):
        search_bar = self.page.locator(loc.search_input_loc)
        expect(search_bar).to_be_visible()

    def check_error_message_empty_pw(self):
        error_message_empty_pw = self.page.locator(loc.error_empty_password_loc)
        expect(error_message_empty_pw).to_be_visible()

    def check_error_message_empty_login(self):
        error_message_empty_login = self.page.locator(loc.error_empty_login_loc)
        expect(error_message_empty_login).to_be_visible()
