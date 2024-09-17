import pytest
import data
from selenium import webdriver
from selenium.webdriver.chrome.options import Options as ChromeOptions
from selenium.webdriver.firefox.options import Options as FirefoxOptions
from pages.main_page import MainPage
from pages.recovery_page import RecoveryPage
from pages.account_page import AccountPage
from pages.feed_page import FeedPage
import requests
import allure
from helpers import generate_data_customer
from data import URL_CUSTOMER, URL_CUSTOMER_REG


@allure.step('Регистрация нового тестового покупателя, авторизация и последующее удаление')
@pytest.fixture()
def response_customer(account_page):
    response_customer = None
    # генерируем данные покупателя
    payload = generate_data_customer()
    # отправляем запрос на регистрацию тестового покупателя и сохраняем ответ в переменную
    response_customer = requests.post(URL_CUSTOMER_REG, data=payload)
    # получаем токен пользователя
    access_token = response_customer.json()['accessToken']
    account_page.login_customer(payload)
    yield response_customer, access_token, payload
     #удаляем тестового покупателя
    response_delete = requests.delete(URL_CUSTOMER, headers={'Authorization': access_token})

@allure.step('Инициация драйвера  и последующее удаление')
@pytest.fixture(params=['chrome'])  #инициация вебдрайвера (params=['chrome', 'firefox'])
def driver(request):
    if request.param == 'chrome':
        chrome_options = ChromeOptions()
        chrome_options.add_argument('--window-size=1920,1080')
        driver = webdriver.Chrome(options=chrome_options)
    elif request.param == 'firefox':
        firefox_options = FirefoxOptions()
        driver = webdriver.Firefox(options=firefox_options)
    driver.get(data.URL_MAIN_PAGE)
    yield driver
    driver.quit()


@allure.step('создание объекта главной страницы')
@pytest.fixture()
def main_page(driver):
    main_page = MainPage(driver)
    return main_page

@allure.step('создание объекта страницы личного кабинет')
@pytest.fixture()
def recovery_page(driver):
    recovery_page = RecoveryPage(driver)
    return recovery_page

@allure.step('создание объекта страницы личного кабинета')
@pytest.fixture()
def account_page(driver):
    account_page = AccountPage(driver)
    return account_page

@allure.step('создание объекта страницы ленты заказов')
@pytest.fixture()
def feed_page(driver):
    feed_page = FeedPage(driver)
    return feed_page

@allure.step('Регистрация нового тестового покупателя, авторизация, формирование заказов и последующее удаление')
@pytest.fixture()
def customer_authorized(account_page, main_page):
    # генерируем данные покупателя
    payload = generate_data_customer()
    # отправляем запрос на регистрацию тестового покупателя и сохраняем ответ в переменную
    response = requests.post(URL_CUSTOMER_REG, data=payload)
    # получаем токен пользователя
    access_token = response.json()['accessToken']
    account_page.login_customer(payload)
    main_page.registration_order()
    yield customer_authorized, access_token, payload
    #удаляем тестового покупателя
    response_delete = requests.delete(URL_CUSTOMER, headers={'Authorization': access_token})

