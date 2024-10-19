from playwright.sync_api import Page


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
