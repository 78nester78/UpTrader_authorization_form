from selenium.webdriver.common.by import By


class RegistrationLocators:

    BOOKMARK_REGISTRATION = (By.ID, 'login-page-nav-to-registration-page')
    CHECK_REG_FORM = (By.XPATH, '//*[@id="main-registration-form"]/div[1]/div[1]/div/label')
    NAME_FIELD = (By.ID, 'firstName')
    SURNAME_FIELD = (By.ID, 'lastName')
    EMAIL_FIELD = (By.ID, 'email')
    PHONE_FIELD = (By.XPATH, '//*[@id="main-registration-form"]/div[4]/div/div/input')
    PASSWORD_FIELD = (By.ID, 'password')
    REPEAT_PASSWORD_FIELD = (By.ID, 'passwordRepeat')
    CHECK_BOX_1 = (By.ID, 'agreement_0FieldId')
    CHECK_BOX_2 = (By.ID, 'agreement_1FieldId')
    CHECK_BOX_3 = (By.ID, 'agreement_2FieldId')
    REGISTRATION_BUTTON = (By.ID, 'registration-page-registration-button')
    CHECK_REGISTRATION = (By.XPATH, '//*[@id="root"]/div/div/div[1]/div[1]/div[3]/h3') #'Вы зарегистрированы!'


class AuthorizationLocators:

    EMAIL_AUTH_FIELD = (By.ID, 'emailOrPhone')
    PASSWORD_AUTH_FIELD = (By.ID, 'password')
    ENTRANCE_AUTH_BUTTON = (By.ID, 'login-page-sign-in-button')
    CHECK_AUTHORIZATION = (By.XPATH, '//*[@id="PageLayout__Header-clientAccounts"]/h1/span')
    CHECK_INVALID_EMAIL = (By.XPATH, '//*[@id="main-login-form"]/div[1]/div[1]/div/span/span')
    CHECK_INVALID_PASSWORD = (By.XPATH, '//*[@id="main-login-form"]/div[1]/div[2]/div/span')
