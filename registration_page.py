import time
from selenium.webdriver.common.action_chains import ActionChains
from base_page import BasePage
from locators import RegistrationLocators
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from locators import RegistrationLocators


class RegistrationPage(BasePage):
    def go_to_reg_form(self):
        self.go_to_site()
        reg_elem = self.find_element(RegistrationLocators.BOOKMARK_REGISTRATION)
        return reg_elem.click()

    def check_reg_form(self):
        check_form = self.find_element(RegistrationLocators.NAME_FIELD)
        return check_form

    def enter_name_reg_form(self, name):
        search_name_field = self.find_element(RegistrationLocators.NAME_FIELD)
        search_name_field.click()
        search_name_field.send_keys(name)
        return search_name_field.text

    def enter_surname_reg_form(self, surname):
        search_surname_field = self.find_element(RegistrationLocators.SURNAME_FIELD)
        search_surname_field.click()
        search_surname_field.send_keys(surname)
        return search_surname_field.text

    def enter_email_reg_form(self, email):
        search_email_field = self.find_element(RegistrationLocators.EMAIL_FIELD)
        search_email_field.click()
        search_email_field.send_keys(email)
        return search_email_field.text

    def enter_phone_reg_form(self, phone):
        search_phone_field = self.find_element(RegistrationLocators.PHONE_FIELD)
        search_phone_field.click()
        search_phone_field.send_keys(phone)
        return search_phone_field.text

    def enter_password_reg_form(self, password):
        search_pas_field = self.find_element(RegistrationLocators.PASSWORD_FIELD)
        search_pas_field.click()
        search_pas_field.send_keys(password)
        return search_pas_field.text

    def enter_repeat_password_reg_form(self, password):
        search_repeat_pas_field = self.find_element(RegistrationLocators.REPEAT_PASSWORD_FIELD)
        search_repeat_pas_field.click()
        search_repeat_pas_field.send_keys(password)
        return search_repeat_pas_field.text

    def scroll_down(self, offset=0):
        self.driver.execute_script("window.scrollBy(0, document.body.scrollHeight)")

    def check_box_1(self):
        search_check_box_1 = self.find_element(RegistrationLocators.CHECK_BOX_1)
        return self.driver.execute_script("arguments[0].click();", search_check_box_1)

    def check_box_2(self):
        search_check_box_2 = self.find_element(RegistrationLocators.CHECK_BOX_2)
        return self.driver.execute_script("arguments[0].click();", search_check_box_2)

    def check_box_3(self):
        search_check_box_3 = self.find_element(RegistrationLocators.CHECK_BOX_3)
        return self.driver.execute_script("arguments[0].click();", search_check_box_3)

    def click_registration_button(self):
        search_button = self.find_element(RegistrationLocators.REGISTRATION_BUTTON)
        return search_button.click()

    def check_registration(self):
        check_reg = self.find_element(RegistrationLocators.CHECK_REGISTRATION)
        return check_reg.text

