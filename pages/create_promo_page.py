from playwright.sync_api import expect
from pages.locators import text_promo_locators as loc
from pages.locators import login_locators as loc1
from pages.base_page import BasePage
from time import sleep


class PromoPage(BasePage):
    page_url = 'profile#/create-promotion'

    def fill_login_form(self, login, password):
        self.page.locator(loc1.login_field_loc).fill(login)
        self.page.locator(loc1.password_field_loc).fill(password)
        self.page.locator(loc1.button_loc).click()

    def create_text_promo(self, desc_text):
        text_promo = self.page.locator(loc.text_ads_loc)
        text_promo.click()
        next_button = self.page.locator(loc.next_button_loc)
        next_button.click()
        url = self.page.locator(loc.url_loc)
        display_url = self.page.locator(loc.display_url_loc)
        headline = self.page.locator(loc.headline_loc)
        description = self.page.locator(loc.description_loc)
        url.fill('http://torrent.com')
        display_url.fill('random-display-url.com')
        headline.fill('etoheadline')
        description.fill(desc_text)
        next_button.click()
        self.page.locator(loc.geolocation_loc).locator("nth=0").click()
        self.page.locator(loc.geolocation_loc).locator("nth=1").click()
        location_for_test = self.page.locator(loc.birmingham_loc)
        location_for_test.click()
        next_button.click()
        self.page.locator(loc.escort_category_loc).locator('nth=0').click()
        next_button.click()
        cpc = self.page.locator(loc.cpc_loc)
        daily = self.page.locator(loc.daily_loc)
        finish_button = self.page.locator(loc.finish_button_loc)
        cpc.fill('1')
        daily.fill('11')
        finish_button.click()
        created_text_ad = self.page.locator(f"//div[contains(text(), '{desc_text}')]")
        expect(created_text_ad).to_be_visible(timeout=15000)
        expect(created_text_ad).to_have_text(desc_text)

    def create_image_promo(self):
        self.page.locator(loc.image_ads_loc).click()
        self.page.locator(loc.next_button_loc).click()
        self.page.locator(loc.phone_number_loc).fill('19179072366')
        self.page.locator(loc.next_button_loc).click()
        self.page.locator(loc.choose_profile_card_loc).click()
        self.page.locator(loc.next_button_loc).click()
        self.page.locator(loc.choose_photo_loc).locator('nth=1').click()
        self.page.locator(loc.next_button_loc).click()
        self.page.locator(loc.checkout_button_loc).click()

    def create_url_promo(self):

        self.page.locator(loc.url_ads_loc).click()
        self.page.locator(loc.next_button_loc).click()
        self.page.locator(loc.url_url_loc).type(
            'https://adultsearch.com/georgia/atlanta/female-escorts/1112314', delay=10
        )
        self.page.locator(loc.next_button_loc).locator('nth=0').click()
        self.page.wait_for_selector(loc.shemale_category_loc)
        self.page.locator(loc.shemale_category_loc).locator('nth=0').click()
        self.page.locator(loc.next_button_loc).locator('nth=0').click()
        self.page.locator(loc.cpc_url_loc).fill('1')
        self.page.locator(loc.daily_url_loc).fill('11')
        self.page.locator(loc.next_button_loc).locator('nth=0').click()
        self.page.locator(loc.next_button_loc).locator('nth=2').click()
