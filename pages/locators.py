from selenium.webdriver.common.by import By


class AuthLocators:
    page_right = (By.ID, 'page-right')
    page_left = (By.ID, 'page-left')
    authorization = (By.XPATH, '//section[@id="page-right"]/div/div/h1')
    card_of_auth = (By.CLASS_NAME, 'card-container__wrapper')
    menu_tub = (By.XPATH, "//div[@class='rt-tabs rt-tabs--orange rt-tabs--small tabs-input-container__tabs']")
    tub_phone = (By.ID, 't-btn-tab-phone')
    tub_email = (By.ID, 't-btn-tab-mail')
    tub_login = (By.ID, 't-btn-tab-login')
    tub_ls = (By.ID, 't-btn-tab-ls')
    active_tub_phone = (By.XPATH, '//div[@id="t-btn-tab-phone" and @class="rt-tab rt-tab--small rt-tab--active"]')
    auth_email = (By.ID, "username")
    auth_pass_eml = (By.ID, "password")
    auth_login = (By.ID, 'username')
    auth_pass_log = (By.ID, "password")
    auth_btn_enter = (By.ID, "kc-login")
    forgot_password_link = (By.ID, "forgot_password")
    register_link = (By.ID, 'kc-register')
    placeholder_name_of_user = (By.XPATH, '//span[@class="rt-input__placeholder"]')
    placeholder_email_passw = (By.XPATH, '//span[@class="rt-input__mask-start"]')
    error_message = (By.XPATH, '//span[@id="form-error-message"]')
    password_recovery = (By.XPATH, "//h1[contains(text(),'Восстановление пароля')]")
    registration = (By.XPATH, "//h1[contains(text(),'Регистрация')]")
    personal_accounts = (By.XPATH, "//*[contains(text(),'Личные кабинеты')]")
    first_name = (By.NAME, 'firstName')
    last_name = (By.NAME, 'lastName')
    email_registration = (By.ID, 'address')
    address_registration = (By.XPATH, "//*[contains(text(),'Регион')]")
    passw_registration = (By.ID, 'password')
    passw_registration_confirm = (By.ID, 'password-confirm')
    registration_btn = (By.NAME, 'register')
    redirect_auth = (By.XPATH, '//button[text()="Войти"]')
    page_left_registration = (By.ID, 'page-left')
    card_of_registration = (By.CLASS_NAME, 'card-container__wrapper')
    container_f_name = (By.XPATH, '//div[1][@class="rt-input-container"]')
    container_l_name = (By.XPATH, '//div[2][@class="rt-input-container"]')
    container_passw_confirm = (By.XPATH, '//div[@class="new-password-container"]')
    error_first_name = (By.XPATH, "//form/div[1]/div[1]/span")
    error_last_name = (By.XPATH, '//form/div[1]/div[2]/span')
    error_email = (By.XPATH, "//form/div[3]/span")
    error_passw = (By.XPATH, '//form/div[4]/div[1]/span')
    error_passw_confirm = (By.XPATH, '//form/div[4]/div[2]/span')
    error_account_exists = (By.XPATH, '//h2[text()="Учётная запись уже существует"]')
    email_confirm = (By.XPATH, "//section/div/div/h1")
