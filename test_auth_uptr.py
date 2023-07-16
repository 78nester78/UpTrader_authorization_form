import pytest
import time
from base_page import BasePage
from setting import *


def test_valid_auth(browser):
    """Проверяем авторизацию с валидными данными"""
    auth_page = BasePage(browser)
    auth_page.go_to_site()
    auth_page.enter_email(valid_email)
    auth_page.enter_password(valid_password)
    auth_page.click_button()

    assert 'Счет' in auth_page.check_auth()


@pytest.mark.parametrize("email",
                         ['', ' ', '@yandex.ru', 'ivanovyandex.ru', 'ivanov@yandex.'],
                         ids=["empty", "space", "without user name", "without @", "without domain"])
def test_invalid_email_auth(browser, email):
    """Проверяем авторизацию с невалидным значением электронной почты"""
    auth_page = BasePage(browser)
    auth_page.go_to_site()
    auth_page.enter_email(email)
    auth_page.enter_password(valid_password)

    assert auth_page.check_invalid_email() in ['Обязательное поле', 'Не является корректным адресом электронной почты']


@pytest.mark.parametrize("password",
                         ['', ' ', '12345', '!"№;%:'],
                         ids=["empty", "space", "incomplete password", "special characters"])
def test_invalid_password_wrong_auth(browser, password):
    """Проверяем авторизацию с невалидным значением пароля"""
    auth_page = BasePage(browser)
    auth_page.go_to_site()
    auth_page.enter_email(valid_email)
    auth_page.enter_password(password)
    auth_page.click_button()
    time.sleep(1)
    assert auth_page.check_invalid_password() in ['Обязательное поле', 'Неверный пароль']









