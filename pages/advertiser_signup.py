from selenium.webdriver.common.by import By


class AdvertiserSignup:
    def __init__(self, driver):
        self.driver = driver

    def open_signup_page(self):
        self.driver.get('http://qa6.hot.lan/advertiser-signup')

    def fill_signup_form(self, username, email, name, password, confirm_password):
        username_field = self.driver.find_element(By.ID, 'registrationform-login')
        email_field = self.driver.find_element(By.ID, 'registrationform-alternative_email')
        name_field = self.driver.find_element(By.ID, 'display_name')
        password_field = self.driver.find_element(By.ID, 'registrationform-password')
        password_confirm_field = self.driver.find_element(By.ID, 'registrationform-password2')
        button_confirm = self.driver.find_element(By.ID, 'modal__button_signup')
        username_field.send_keys(username)
        email_field.send_keys(email)
        name_field.send_keys(name)
        password_field.send_keys(password)
        password_confirm_field.send_keys(confirm_password)
        button_confirm.click()
