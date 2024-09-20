import pytest
import allure
from locators.feed_page_locators import FeedPageLocators

class TestFeedPage:


    @allure.description('Нажимаем на кнопку "Лента Заказов" и проверяем отображение заголовка "Лента заказов"')
    @allure.title('Проверка перехода по кнопке "Лента Заказов"')
    def test_transition_order_feed(self, transition_page, feed_page):
        transition_page.go_to_order_feed()
        assert feed_page.search_inscription_feed() # проверяем отображение заголовка "Лента заказов"

    @allure.title('Проверка просмотра деталей заказа')
    @allure.description('Переходим в ленту заказов, кликаем на последний заказ и проверяем открытие модального окна')
    def test_view_order_details(self, feed_page, transition_page):
        # переходим на страницу ленты
        transition_page.go_to_order_feed()
        # нажимаем на карточку заказа и проверяем наличие окна деталей
        assert feed_page.view_order_details()

    @allure.title('Проверка наличия номера нового заказа в разделе "В работе"')
    @allure.description('Формируем заказ и получаем номер заказа, переходим в ленту заказов и'
                        ' проверяем наличие номера заказа в разделе "В работе"')
    def test_checking_new_order_in_progress(self, feed_page, transition_page, main_page, response_customer):
        # формируем заказ и получаем номер
        number = main_page.registration_order_with_number()
        # переходим в ленту заказов
        transition_page.go_to_order_feed()
        # проверяем загрузку ленты
        feed_page.search_inscription_feed()
        # проверяем наличие заказа в работе
        assert feed_page.search_number_at_work(number)

    @allure.title('Проверка увеличения счетчика заказов за все время/за день при создании нового заказа')
    @allure.description('В ленте заказов находим счетчик и сохраняем его значение в переменную, формируем заказ, '
                        'переходим в ленту, берем значение счетчика и сравниваем')
    @pytest.mark.parametrize('locator_counter', [FeedPageLocators.TOTAL_ORDERS, FeedPageLocators.TOTAL_ORDERS_TODAY])
    def test_increasing_order_counter_total(self, feed_page, transition_page, main_page,
                                            response_customer, locator_counter):
        # переходим в ленту заказов
        transition_page.go_to_order_feed()
        # получаем текущее значение счетчика
        counter_before = feed_page.getting_counter_order_total(locator_counter)
        # переходим в конструктор
        transition_page.go_to_constructor()
        # оформляем заказ
        main_page.registration_order()
        # переходим в ленту заказов
        transition_page.go_to_order_feed()
        # получаем текущее значение счетчика
        counter_after = feed_page.getting_counter_order_total_after(locator_counter, counter_before)
        # проверяем изменение значения счетчика
        assert counter_before < counter_after

    @allure.title('Проверка отображения заказов из истории в ленте')
    @allure.description('В истории заказов получаем номера заказов, переходим в ленту заказов и проверяем их наличие')
    def test_view_order_in_feed(self, feed_page, transition_page, account_page, customer_authorized):
        # нажимам кнопку Личный Кабинет
        transition_page.login_to_personal_account()
        # нажимаем таб История
        transition_page.go_to_order_history()
        # получаем номер заказа в истории
        number = account_page.getting_orders_in_history()
        # нажимаем кнопку Лена заказов
        transition_page.go_to_order_feed()
        # проверяем наличие заказа в ленте
        assert feed_page.search_orders_in_feed(number)

