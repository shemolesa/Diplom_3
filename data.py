from locators.main_page_locators import MainPageLocators
URL_MAIN_PAGE = 'https://stellarburgers.nomoreparties.site/'
URL_CUSTOMER_REG = URL_MAIN_PAGE + 'api/auth/register'
URL_CUSTOMER = URL_MAIN_PAGE + 'api/auth/user'
URL_CUSTOMER_LOGIN = URL_MAIN_PAGE + 'api/auth/login'
URL_MENU_INGREDIENT = ''

TEST_EMAIL = 'test-email@ya.ru'
TEST_PASSWORD = 'TEST_PASSWORD'

PAUSE = 17

MENU_BUNS = ['61c0c5a71d1f82001bdaaa6d', '61c0c5a71d1f82001bdaaa6c']
MENU_FILLINGS = ['61c0c5a71d1f82001bdaaa6f', '61c0c5a71d1f82001bdaaa70', '61c0c5a71d1f82001bdaaa71', '61c0c5a71d1f82001bdaaa6e','61c0c5a71d1f82001bdaaa76', '61c0c5a71d1f82001bdaaa77', '61c0c5a71d1f82001bdaaa78', '61c0c5a71d1f82001bdaaa79', '61c0c5a71d1f82001bdaaa7a']
MENU_SAUCES = ['61c0c5a71d1f82001bdaaa72', '61c0c5a71d1f82001bdaaa73', '61c0c5a71d1f82001bdaaa74', '61c0c5a71d1f82001bdaaa75']

BURGER = [MainPageLocators.MENU_BUNS, MainPageLocators.MENU_SOUSES, MainPageLocators.MENU_FILLINGS, MainPageLocators.CONSTRUCTOR, MainPageLocators.BUTTON_CHECKOUT]