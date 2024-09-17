import pytest
import allure


class TestAccountPage:


    @allure.title('Проверка перехода в личный кабинет авторизованного пользователя')
    @allure.description('Открываем сайт, переходим на страницу входа и логинимся. нажимаем кнопку "Личный кабинет" и проверяем отображение страницы личного кабинета')
    def test_login_to_personal_account_authorized(self, main_page, account_page, response_customer):
        assert account_page.login_to_personal_account_authorized(response_customer[2])

    @allure.title('Проверка перехода в личный кабинет без авторизации')
    @allure.description('Открываем сайт без авторизации пользователя и нажимаем кнопку "Личный кабинет". Проверяем отображение страницы входа')
    def test_login_to_personal_account_unauthorized(self, account_page, main_page):
        assert account_page.login_to_personal_account_unauthorized()

    @allure.title('Проверка выхода из аккаунта')
    @allure.description('Открываем сайт, переходим на страницу входа и логинимся. нажимаем кнопку "Личный кабинет", нажимаем кнопку "Выход" и проверяем отображение страницы входа')
    def test_logout_from_account(self, account_page, response_customer):
        assert account_page.logout_from_account(response_customer[2])

    @allure.title('Проверка перехода к разделу  "История заказов" под пользователями: без заказов и с заказами')
    @allure.description('Открываем сайт, переходим на страницу входа и логинимся. нажимаем кнопку "Личный кабинет" и переходим на вкладку "История заказов". Проверяем наличие контейнера заказов')
    @pytest.mark.parametrize('customer', ['response_customer', 'customer_authorized'])
    def test_transition_order_history(self, main_page, account_page, customer, request):
        response_fixture = request.getfixturevalue(customer)  # преобразовываем фикстуру
        assert account_page.transition_order_history()
