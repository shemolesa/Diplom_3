import pytest
import allure
from locators.feed_page_locators import FeedPageLocators

class TestFeedPage:

    @allure.title('Проверка просмотра деталей заказа')
    @allure.description('Переходим в ленту заказов, кликаем на последний заказ и проверяем открытие модального окна')
    def test_view_order_details(self, feed_page):
        assert feed_page.view_order_details()

    @allure.title('Проверка наличия номера нового заказа в разделе "В работе"')
    @allure.description('Формируем заказ и получаем номер заказа, переходим в ленту заказов и проверяем наличие номера заказа в разделе "В работе"')
    def test_checking_new_order_in_progress(self, feed_page, response_customer):
        assert feed_page.search_number_at_work()

    @allure.title('Проверка увеличения счетчика заказов за все время/за день при создании нового заказа')
    @allure.description('В ленте заказов находим счетчик и сохраняем его значение в переменную, формируем заказ, переходим в ленту, берем значение счетчика и сравниваем')
    @pytest.mark.parametrize('locator_counter', [FeedPageLocators.TOTAL_ORDERS, FeedPageLocators.TOTAL_ORDERS_TODAY])
    def test_increasing_order_counter_total(self, feed_page, response_customer, locator_counter):
        counter_value = feed_page.comparison_counters(locator_counter)
        assert counter_value[0] < counter_value[1]

    @allure.title('Проверка отображения заказов из истории в ленте')
    @allure.description('В истории заказов получаем номера заказов, переходим в ленту заказов и проверяем их наличие')
    def test_view_order_in_feed(self, feed_page, customer_authorized):
        assert feed_page.search_orders_in_feed()

