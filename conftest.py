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
    requests.delete(URL_CUSTOMER, headers={'Authorization': access_token})

@allure.step('Регистрация нового тестового покупателя, авторизация, формирование заказов и последующее удаление')
@pytest.fixture()
def customer_authorized(response_customer, account_page, main_page):
    # формируем заказ
    main_page.registration_order()
    return response_customer[0], response_customer[1], response_customer[2]


@allure.step('Инициация драйвера  и последующее удаление')
@pytest.fixture(params=['chrome', 'firefox']) #инициация вебдрайвера
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

