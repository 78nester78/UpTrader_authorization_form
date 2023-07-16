import pytest
import time
from base_page import BasePage
from setting import *
from registration_page import RegistrationPage


def test_reg_form(browser):
    """Проверяем доступность формы регистрации"""
    reg_form = RegistrationPage(browser)
    reg_form.go_to_reg_form()

    assert reg_form.check_reg_form()


def test_check_boxs(browser):
    """Проверяем регистрацию нового пользователя с валидными данными"""
    check_box_form = RegistrationPage(browser)
    check_box_form.go_to_reg_form()
    check_box_form.enter_name_reg_form(valid_name)
    check_box_form.enter_surname_reg_form(valid_surname)
    check_box_form.enter_email_reg_form(valid_email)
    check_box_form.enter_phone_reg_form(valid_phone)
    check_box_form.enter_password(valid_password)
    check_box_form.enter_repeat_password_reg_form(valid_password)
    check_box_form.scroll_down()
    check_box_form.check_box_1()
    check_box_form.check_box_2()
    check_box_form.check_box_3()
    check_box_form.click_registration_button()
    check_reg = check_box_form.check_registration()

    assert 'Вы зарегистрированы!' in check_reg
