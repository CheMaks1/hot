from playwright.sync_api import expect
from pages.locators import create_promo_locators as loc
from pages.base_page import BasePage
from time import sleep


class PromoPage(BasePage):
    page_url = 'profile#/create-promotion'
    model_url_promo = 'https://adultsearch.com/georgia/atlanta/female-escorts/1112314'
    model_top_spot_promo = 'https://adultsearch.com/us/arizona/phoenix/tstv-shemale-escorts/1852559'

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
        phone_num = self.page.locator(loc.phone_number_loc)
        phone_num.press('Backspace')
        phone_num.type('16475280768', delay=100)
        self.page.locator(loc.next_button_loc).click()
        self.page.locator(loc.choose_profile_card_loc).first.click()
        self.page.locator(loc.next_button_loc).click()
        self.page.locator(loc.choose_photo_loc).locator('nth=1').click()
        self.page.locator(loc.next_button_loc).click()
        self.page.locator(loc.checkout_button_loc).click()
        list_promo = self.page.locator(loc.image_promotions_list_loc).locator('nth=0')
        expect(list_promo).to_be_visible(timeout=10000)

    def create_url_promo(self):
        self.page.locator(loc.url_ads_loc).click()
        self.page.locator(loc.next_button_loc).click()
        self.page.locator(loc.url_url_loc).type(self.model_url_promo, delay=10)
        self.page.locator(loc.next_button_loc).locator('nth=0').click()
        self.page.wait_for_selector(loc.shemale_category_loc)
        self.page.locator(loc.shemale_category_loc).locator('nth=0').click()
        self.page.locator(loc.next_button_loc).locator('nth=0').click()
        self.page.locator(loc.cpc_url_loc).fill('1')
        self.page.locator(loc.daily_url_loc).fill('11')
        self.page.locator(loc.next_button_loc).locator('nth=0').click()
        self.page.locator(loc.next_button_loc).locator('nth=2').click()

    def create_top_spot_promo(self):
        self.page.locator(loc.top_spot_loc).click()
        self.page.locator(loc.next_button_loc).click()
        self.page.locator(loc.destination_url_loc).type(self.model_top_spot_promo, delay=10)
        self.page.locator(loc.next_button_loc).locator('nth=0').click()
        choose_profile = self.page.locator(loc.choose_top_spot_profile_card_loc).locator('nth=0')
        expect(choose_profile).to_be_visible()
        choose_profile.click()
        self.page.locator(loc.next_button_loc).locator('nth=1').click()
        self.page.locator(loc.choose_top_spot_tumbnail_loc).locator('nth=0').click()
        self.page.locator(loc.next_button_loc).locator('nth=2').click()
        choose_category = self.page.locator(loc.top_spot_category_escort_loc)
        expect(choose_category).to_be_visible()
        choose_category.click()
        self.page.locator(loc.next_button_loc).locator('nth=4').click()
        next_category_button = self.page.locator(loc.next_button_loc).locator('nth=6')
        expect(next_category_button).to_be_visible()
        next_category_button.click()
        self.page.locator(loc.cpc_url_loc).fill('1')
        self.page.locator(loc.daily_url_loc).fill('11')
        self.page.locator(loc.next_button_loc).locator('nth=7').click()
        self.page.locator(loc.next_button_loc).locator('nth=8').click()
        sleep(3)
