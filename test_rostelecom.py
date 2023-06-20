import pytest
import random
from pages.auth_page import AuthPage
from settings import valid_email, valid_password, valid_login, valid_phone, valid_ls
from selenium import webdriver
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By


driver = webdriver.Chrome()


def test_registration_email(web_browser):

    page = AuthPage(web_browser)

    page.registration.click()

    page.name.send_keys('Ольга')

    page.lastname.send_keys('Корнеева')

    page.region.send_keys('Калининградская обл')

    page.email_or_phone.send_keys(valid_email)

    page.password.send_keys(valid_password)

    page.confirmation.send_keys(valid_password)

    page.register.click()

    page.auth_code.send_keys(valid_email)
    page.get_code.click()

    page2 = pytest.driver.get('https://e.mail.ru/inbox?newreg=1&app_id_mytracker=58519')
    element = WebDriverWait(driver, 10).until(
        EC.text_to_be_present_in_element(By.TAG_NAME, 'div > span', 'Код подтверждения')
    )
    page2.element.click()
    element2 = driver.find_element(By.TAG_NAME, 'div > p')
    for i in element2:
        numb = i.text.split(' ')
        number = numb[2]
        my_code = number.get_text()
    page = AuthPage(web_browser)

    page.rt_code.send_keys(my_code)

    assert page.get_current_url() == 'https://start.rt.ru/?tab=main'


def test_registration_phone(web_browser):

    page = AuthPage(web_browser)

    page.registration.click()

    page.name.send_keys('Ольга')

    page.lastname.send_keys('Корнеева')

    page.region.send_keys('Калининградская обл')

    page.email_or_phone.send_keys(valid_phone)

    page.password.send_keys(valid_password)

    page.confirmation.send_keys(valid_password)

    page.register.click()

    page.auth_code.send_keys(valid_phone)
    page.get_code.click()

    page.rt_code.send_keys()

    assert page.get_current_url() == 'https://start.rt.ru/?tab=main'


@pytest.mark.parametrize
def test_registration_phone_negativ(web_browser):

    page = AuthPage(web_browser)

    page.registration.click()

    page.name.send_keys('Ольга')

    page.lastname.send_keys('Корнеева')

    page.region.send_keys('Калининградская обл')

    page.email_or_phone.send_keys(valid_phone)

    page.password.send_keys(valid_password)

    page.confirmation.send_keys(valid_password)

    page.register.click()

    page.auth_code.send_keys(valid_phone)
    page.get_code.click()

    page.rt_code.send_keys()

    assert page.get_current_url() == 'https://start.rt.ru/?tab=main'


def test_authorization_login(web_browser):

    page = AuthPage(web_browser)

    page.login.send_keys(valid_login)

    page.password.send_keys(valid_password)

    page.btn.click()

# КАКУЮ СТРАНИЦУ НИЖЕ УКАЗАТЬ?
    assert page.get_current_url() == 'https://start.rt.ru/?tab=main'


@pytest.mark.parametrize
def test_authorization_login_negativ(web_browser):

    page = AuthPage(web_browser)

    page.login.send_keys(valid_login)

    page.password.send_keys(valid_password)

    page.btn.click()

    assert page.get_current_url() == 'https://start.rt.ru/?tab=main'


def test_authorization_email(web_browser):

    page = AuthPage(web_browser)

    page.email.send_keys(valid_email)

    page.password.send_keys(valid_password)

    page.btn.click()

    # КАКУЮ СТРАНИЦУ НИЖЕ УКАЗАТЬ?
    assert page.get_current_url() == 'https://start.rt.ru/?tab=main'


def test_authorization_phone(web_browser):

    page = AuthPage(web_browser)

    page.phone.send_keys(valid_phone)

    page.password.send_keys(valid_password)

    page.btn.click()

    # КАКУЮ СТРАНИЦУ НИЖЕ УКАЗАТЬ?
    assert page.get_current_url() == 'https://start.rt.ru/?tab=main'

def test_authorization_ls(web_browser):

    page = AuthPage(web_browser)

    page.ls.send_keys(valid_ls)

    page.password.send_keys(valid_password)

    page.btn.click()

    # КАКУЮ СТРАНИЦУ НИЖЕ УКАЗАТЬ?
    assert page.get_current_url() == 'https://start.rt.ru/?tab=main'


def test_authorization_code_email(web_browser):

    page = AuthPage(web_browser)

    page.code.click()

    page.auth_code.send_keys(valid_email)

    page.get_code.click()

    page2 = pytest.driver.get('https://e.mail.ru/inbox/')

    element = WebDriverWait(driver, 10).until(
        EC.text_to_be_present_in_element(By.TAG_NAME, 'div > span', 'Код авторизации в личном кабинете')
    )

    page2.element.click()

    element2 = driver.find_element(By.TAG_NAME, 'div > p')

    for i in element2:
        numb = i.text.split(' ')
        number = numb[2]
        my_code = number.get_text()

    page = AuthPage(web_browser)

    page.rt_code.send_keys(my_code)

    assert page.get_current_url() == 'https://start.rt.ru/?tab=main'


def test_authorization_code_phone(web_browser):

    page = AuthPage(web_browser)

    page.code.click()

    page.auth_code.send_keys(valid_phone)

    page.get_code.click()

    page.rt_code.send_keys()

    assert page.get_current_url() == 'https://start.rt.ru/?tab=main'


def test_pass_recovery_phone(web_browser):

    page = AuthPage(web_browser)

    page.recovery.click()

    page.phone.send_keys(valid_phone)

    symbols = page.captcha.get_text()

    page.symbol.send_keys(symbols)

    page.contin.click()

    page.rt_code.send_keys()

    new_pass = random

    page.new_pass.send_keys(new_pass)

    page.confirm.send_keys(new_pass)

    page.save.click()

    assert page.get_current_url() == 'https://start.rt.ru/?tab=main'


def test_pass_recovery_email(web_browser):

    page = AuthPage(web_browser)

    page.recovery.click()

    page.email.send_keys(valid_email)

    symbols = page.captcha.get_text()

    page.symbol.send_keys(symbols)

    page.contin.click()

    page2 = pytest.driver.get('https://e.mail.ru/inbox/')
    element = WebDriverWait(driver, 10).until(
        EC.text_to_be_present_in_element(By.TAG_NAME, 'div > span', 'Код подтверждения')
    )
    page2.element.click()
    element2 = driver.find_element(By.TAG_NAME, 'div > p')
    for i in element2:
        numb = i.text.split(' ')
        number = numb[2]
        my_code = number.get_text()
    page = AuthPage(web_browser)

    page.rt_code.send_keys(my_code)

    new_pass = random

    page.new_pass.send_keys(new_pass)

    page.confirm.send_keys(new_pass)

    page.save.click()

    assert page.get_current_url() == 'https://start.rt.ru/?tab=main'


@pytest.mark.parametrize
def test_pass_recovery_email_negativ(web_browser):

    page = AuthPage(web_browser)

    page.recovery.click()

    page.email.send_keys(valid_email)

    symbols = page.captcha.get_text()

    page.symbol.send_keys(symbols)

    page.contin.click()

    page2 = pytest.driver.get('https://e.mail.ru/inbox/')
    element = WebDriverWait(driver, 10).until(
        EC.text_to_be_present_in_element(By.TAG_NAME, 'div > span', 'Код подтверждения')
    )
    page2.element.click()
    element2 = driver.find_element(By.TAG_NAME, 'div > p')
    for i in element2:
        numb = i.text.split(' ')
        number = numb[2]
        my_code = number.get_text()
    page = AuthPage(web_browser)

    page.rt_code.send_keys(my_code)

    new_pass = random

    page.new_pass.send_keys(new_pass)

    page.confirm.send_keys(new_pass)

    page.save.click()

    assert page.get_current_url() == 'https://start.rt.ru/?tab=main'


def test_pass_recovery_ls(web_browser):

    page = AuthPage(web_browser)

    page.recovery.click()

    page.ls.send_keys(valid_ls)

    symbols = page.captcha.get_text()

    page.symbol.send_keys(symbols)

    page.contin.click()

    page2 = pytest.driver.get('https://e.mail.ru/inbox/')
    element = WebDriverWait(driver, 10).until(
        EC.text_to_be_present_in_element(By.TAG_NAME, 'div > span', 'Код подтверждения')
    )
    page2.element.click()
    element2 = driver.find_element(By.TAG_NAME, 'div > p')
    for i in element2:
        numb = i.text.split(' ')
        number = numb[2]
        my_code = number.get_text()
    page = AuthPage(web_browser)

    page.rt_code.send_keys(my_code)

    new_pass = random

    page.new_pass.send_keys(new_pass)

    page.confirm.send_keys(new_pass)

    page.save.click()

    assert page.get_current_url() == 'https://start.rt.ru/?tab=main'


def test_pass_recovery_login(web_browser):

    page = AuthPage(web_browser)

    page.recovery.click()

    page.login.send_keys(valid_login)

    symbols = page.captcha.get_text()

    page.symbol.send_keys(symbols)

    page.contin.click()

    page2 = pytest.driver.get('https://e.mail.ru/inbox/')
    element = WebDriverWait(driver, 10).until(
        EC.text_to_be_present_in_element(By.TAG_NAME, 'div > span', 'Код подтверждения')
    )
    page2.element.click()
    element2 = driver.find_element(By.TAG_NAME, 'div > p')
    for i in element2:
        numb = i.text.split(' ')
        number = numb[2]
        my_code = number.get_text()
    page = AuthPage(web_browser)

    page.rt_code.send_keys(my_code)

    new_pass = random

    page.new_pass.send_keys(new_pass)

    page.confirm.send_keys(new_pass)

    page.save.click()

    assert page.get_current_url() == 'https://start.rt.ru/?tab=main'