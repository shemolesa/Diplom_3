import pytest
import allure
import data
from helpers import formation_locators


class TestMainPage:

    @allure.title('Проверка просмотра деталей ингредиента')
    @allure.description("Кликаем на ингредиент и проверяем наличие в классе признака открытого окна")
    def test_view_ingredient_details(self, main_page):
        # проверяем что в названии класса есть признак открытого окна
        assert 'Modal_modal_opened' in main_page.view_ingredient_details()

    @allure.description('Кликаем на ингредиент, закрываем открывшееся окно по кнопке и проверяем отсутствие признака '
                        'открытого окна в название класса окна')
    @allure.title('Проверка закрытия окна просмотра деталей ингредиента')
    def test_close_ingredient_details(self, main_page):
        # проверяем что в названии класса окна нет признака открытого окна
        assert 'Modal_modal_opened' not in main_page.close_ingredient_details()

    @allure.title('Проверка увеличения каунтера ингредиента при добавлении в заказ')
    @allure.description('Перетаскиваем ингредиент в заказ и проверяем, что каунтер ингредиента увеличился')
    @pytest.mark.parametrize('menu_ingredients, quantity', [[data.MENU_BUNS, '2'], [data.MENU_SAUCES, '1'],
                                                            [data.MENU_FILLINGS, '1']])
    def test_adding_ingredient(self, main_page, menu_ingredients, quantity):
        locators_ingredient = formation_locators(menu_ingredients) # формируем локатор ингредиента
        # проверяем значение каунтера ингредиента
        assert main_page.adding_ingredient(locators_ingredient, quantity) == quantity

    @allure.description('Формируем заказ, нажимаем кнопку "Оформить заказ" и ожидаем получение номера заказа')
    @allure.title('Проверка оформление заказа пользователем')
    def test_registration_order(self, main_page, response_customer):
        main_page.order_formation() #оформляем заказ
        assert main_page.getting_order_counter() != '9999' # проверяем появление номера заказа

    @allure.description('Нажимаем на кнопку "Конструктор" и проверяем отображение заголовка "Соберите бургер"')
    @allure.title('Проверка перехода по кнопке "Конструктор"')
    def test_transition_constructor(self, main_page, transition_page):
        transition_page.go_to_login_page() # нажимаем кнопку Войти в аккаунт
        transition_page.go_to_constructor()  # нажимаем кнопку Конструктор
        assert main_page.search_inscription_constructor() # проверяем отображение надписи "Соберите бургер"

