from playwright.sync_api import expect
from pages.locators import login_locators as loc
from pages.base_page import BasePage


class AdvertiserLogin(BasePage):

    def fill_login_form(self, login, password):
        login_field = self.page.locator(loc.login_field_loc)
        password_field = self.page.locator(loc.password_field_loc)
        button = self.page.locator(loc.button_loc)
        login_field.fill(login)
        password_field.fill(password)
        button.click()

    def check_error_alert_text_is(self, text):
        error_alert_text = self.page.locator(loc.error_alert_text_loc)
        expect(error_alert_text).to_have_text(text)

    def check_dashboard_text(self, text):
        dashboard_text = self.page.locator(loc.dashboard_text_loc)
        expect(dashboard_text).to_be_visible(timeout=15000)
        expect(dashboard_text).to_have_text(text)
