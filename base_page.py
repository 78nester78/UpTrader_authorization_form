import time
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from locators import AuthorizationLocators
from setting import *


class BasePage:
    def __init__(self, driver):
        self.driver = driver
        self.base_url = 'https://demo.uptr.dev/auth/login'

    def go_to_site(self):
        self.driver.get(self.base_url)
        pass

    def find_element(self, locator, time=10):
        return WebDriverWait(self.driver, time).until(EC.presence_of_element_located(locator), message=f'Не найден {locator}')

    def enter_email(self, email):
        search_email_field = self.find_element(AuthorizationLocators.EMAIL_AUTH_FIELD)
        search_email_field.click()
        search_email_field.send_keys(email)
        return search_email_field.text

    def enter_password(self, password):
        search_pas_field = self.find_element(AuthorizationLocators.PASSWORD_AUTH_FIELD)
        search_pas_field.click()
        search_pas_field.send_keys(password)
        return search_pas_field.text

    def click_button(self):
        click_auth_button = self.find_element(AuthorizationLocators.ENTRANCE_AUTH_BUTTON)
        return click_auth_button.click()

    def check_auth(self):
        check_auth_page = self.find_element(AuthorizationLocators.CHECK_AUTHORIZATION)
        return check_auth_page.text

    def check_invalid_email(self):
        check_invalid_email_auth_page = self.find_element(AuthorizationLocators.CHECK_INVALID_EMAIL)
        return check_invalid_email_auth_page.text

    def check_invalid_password(self):
        check_invalid_password_auth_page = self.find_element(AuthorizationLocators.CHECK_INVALID_PASSWORD)
        return check_invalid_password_auth_page.text



