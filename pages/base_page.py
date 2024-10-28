from playwright.sync_api import Page
from pages.locators import login_locators as loc


class BasePage:
    base_url = 'http://qa6.hot.lan/'
    page_url = None

    def __init__(self, page: Page):
        self.page = page

    def open_page(self):
        self.page.goto(f'{self.base_url}signin')

    def open_promotions_page(self):
        if self.page_url:
            self.page.goto(f'{self.base_url}{self.page_url}')
        else:
            raise NotImplementedError('Page can not be opened for this page class')

    def fill_login_form(self, login, password):
        login_field = self.page.locator(loc.login_field_loc)
        password_field = self.page.locator(loc.password_field_loc)
        button = self.page.locator(loc.button_loc)
        login_field.fill(login)
        password_field.fill(password)
        if button.is_enabled():
            button.click()
        else:
            self.page.locator(loc.title_for_click_loc).click()
