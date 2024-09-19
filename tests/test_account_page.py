import pytest
import allure


class TestAccountPage:


    @allure.title('Проверка перехода в личный кабинет авторизованного пользователя')
    @allure.description('Открываем сайт, переходим на страницу входа и логинимся. нажимаем кнопку "Личный кабинет" и проверяем отображение страницы личного кабинета')
    def test_login_to_personal_account_authorized(self, account_page, transition_page, response_customer):
        # нажимаем кнопку Личный Кабинет
        transition_page.login_to_personal_account()
        # проверяем наличие таба Профиль
        assert account_page.search_for_profile_tab()

    @allure.title('Проверка перехода в личный кабинет без авторизации')
    @allure.description('Открываем сайт без авторизации пользователя и нажимаем кнопку "Личный кабинет". Проверяем отображение страницы входа')
    def test_login_to_personal_account_unauthorized(self, account_page, transition_page):
        # нажимаем кнопку Личный Кабинет
        transition_page.login_to_personal_account()
        # проверяем наличие надписи Выход
        assert account_page.search_inscription_entrance()

    @allure.title('Проверка выхода из аккаунта')
    @allure.description('Открываем сайт, переходим на страницу входа и логинимся. нажимаем кнопку "Личный кабинет", нажимаем кнопку "Выход" и проверяем отображение страницы входа')
    def test_logout_from_account(self, account_page, transition_page, response_customer):
        # нажимаем кнопку Личный Кабинет
        transition_page.login_to_personal_account()
        # проверяем наличие таба Профиль
        account_page.search_for_profile_tab()
        # нажимаем таб Выход
        transition_page.logout_from_account()
        # # проверяем наличие надписи Выход
        assert account_page.search_inscription_entrance()

    @allure.title('Проверка перехода к разделу  "История заказов" под пользователями: без заказов и с заказами')
    @allure.description('Открываем сайт, переходим на страницу входа и логинимся. нажимаем кнопку "Личный кабинет" и переходим на вкладку "История заказов". Проверяем наличие контейнера заказов')
    @pytest.mark.parametrize('customer', ['response_customer', 'customer_authorized'])
    def test_transition_order_history(self, transition_page, account_page, customer, request):
        response_fixture = request.getfixturevalue(customer)  # преобразовываем фикстуру
        # нажимаем кнопку Личный Кабинет
        transition_page.login_to_personal_account()
        # нажимаем таб История
        transition_page.go_to_order_history()
        # проверяем наличие контейнера истории
        assert account_page.search_order_history()
