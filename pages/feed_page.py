import allure
from pages.base_page import BasePage
from locators.feed_page_locators import FeedPageLocators


class FeedPage(BasePage):

    @allure.step('Поиск надписи Лента Заказов')
    def search_inscription_feed(self):
        # находим надпись и передаем
        return self.find_element_with_wait(FeedPageLocators.INSCRIPTION_ORDER_FEED)

    @allure.step('Просмотр деталей заказа')
    def view_order_details(self):
        self.click_to_element(FeedPageLocators.LAST_ORDER_CARD) # нажимаем на карточку заказа
#       находим модальное окно с деталями заказа и передаем результат
        return self.find_element_with_wait(FeedPageLocators.MODAL_WINDOW)

    @allure.step('Проверка номера заказа в разделе "В работе"')
    def search_number_at_work(self, number):
        # форматируем локатор заказа
        locator_formatted = self.format_locators(FeedPageLocators.ORDER_AT_WORK, number)
        # ждем исчезновения надписи
        self.waiting_for_text_to_change(FeedPageLocators.ORDERS_READY, 'Все текущие заказы готовы!')
        # ищем заказ в работе и передаем результат
        return self.find_element_with_wait(locator_formatted)

    @allure.step('Получение значения счетчика заказов')
    def getting_counter_order_total(self, locator_counter):
        # получаем значение счетчика и сохраняем в переменную
        counter_total = self.get_text_from_element(locator_counter)
        return counter_total # передаем переменную со значением счетчика

    @allure.step('Получение значения счетчика после создания заказа')
    def getting_counter_order_total_after(self, locator_counter, counter_before):
        # получаем значение счетчика заказов в ленте
        new_counter_total = self.getting_counter_order_total(locator_counter)
        # если значение счетчика не изменилось, ждем изменения с снова получаем значение
        if new_counter_total == counter_before:
            self.waiting_for_text_to_change(locator_counter, counter_before)  # ждем отображения номера заказа
            # получаем значение счетчика заказов в ленте
            new_counter_total = self.getting_counter_order_total(locator_counter)
        return new_counter_total # передаем новое значение счетчика

    @allure.step('Поиск в ленте заказов из истории')
    def search_orders_in_feed(self, number):
        # форматируем локатор номера заказа
        locator_formatted = self.format_locators(FeedPageLocators.NUMBER_FEED, number)
        # находим заказа в ленте и возвращаем результат
        return self.find_element_with_wait(locator_formatted)
