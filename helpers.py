import allure
import random
import string
from data import MENU_BUNS, MENU_SAUCES, MENU_FILLINGS


@allure.step('Генерация строкового значения')
def generate_string(length):
    letters = string.ascii_lowercase
    random_string = ''.join(random.choice(letters) for i in range(length))
    return random_string

@allure.step('Генерация email')
def generate_email():
    email_str = generate_string(8)+"@yandex.ru"
    return email_str

@allure.step('Генерация данных покупателя для регистрации')
def generate_data_customer():
    customer = {
    "email": generate_email(),
    "password": generate_string(8),
    "name": generate_string(8)
}
    return customer

@allure.step('Генерация ингредиента')
def generate_ingredient(list_ingredients):
    random_ingredients = random.choice(list_ingredients)
    return random_ingredients

@allure.step('Формирование локатора ингредиента')
def formation_locators(list_ingredient):
    ingredient = generate_ingredient(list_ingredient)
    menu_ingredient = 'xpath', f'.//a[@href="/ingredient/{ingredient}"]'
    counter_ingredient = 'xpath', f'//a[@href="/ingredient/{ingredient}"]//p[@class="counter_counter__num__3nue1"]'
    locators = [menu_ingredient, counter_ingredient]
    return locators

@allure.step('Формирование списка локаторов ингредиентов бургера')
def formation_ingredient_burger():
    locators_ingredients = {
    'bun': formation_locators(MENU_BUNS)[0],
    'sauce': formation_locators(MENU_SAUCES)[0],
    'filling': formation_locators(MENU_FILLINGS)[0]
    }
    return locators_ingredients

