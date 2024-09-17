import allure
import data
from pages.base_page import BasePage
from locators.main_page_locators import MainPageLocators
from locators.feed_page_locators import FeedPageLocators
from locators.account_page_locators import AccountPageLocators


class FeedPage(BasePage):


    @allure.step('Просмотр деталей заказа')
    def view_order_details(self):
        # переходим в ленту
        self.transition_to_page_exception(MainPageLocators.BUTTON_ORDER_FEED, MainPageLocators.INSCRIPTION_ORDER_FEED,
                                           MainPageLocators.EXCEPTION)
        self.click_to_element(FeedPageLocators.LAST_ORDER_CARD) # нажимаем на карточку заказа
#       находим модальное окно с деталями заказа и передаем результат
        return self.find_element_with_wait(FeedPageLocators.MODAL_WINDOW)

    @allure.step('Получение номера заказа и проверка его в разделе "В работе"')
    def search_number_at_work(self):
        self.formation_burger(data.BURGER) # формируем бургер и оформляем заказ
        self.waiting_for_text_to_change(MainPageLocators.NUMBER_ORDER, '9999') # ждем получения номера заказа
        number = self.get_text_from_element(MainPageLocators.NUMBER_ORDER) # сохраняем номер заказа в переменную
        # закрываем окно с номером заказа
        self.close_order_window(MainPageLocators.BUTTON_CLOSE_ORDER, MainPageLocators.EXCEPTION)
        # переходим в ленту
        self.transition_to_page_exception(MainPageLocators.BUTTON_ORDER_FEED, MainPageLocators.INSCRIPTION_ORDER_FEED,
                                           MainPageLocators.EXCEPTION)
        text_at_work = self.get_text_from_element(FeedPageLocators.ORDERS_READY)
        # форматируем локатор заказа
        locator_formatted = self.format_locators(FeedPageLocators.ORDER_AT_WORK, number)
        self.waiting_for_text_to_change(FeedPageLocators.ORDERS_READY, 'Все текущие заказы готовы!')
        return self.find_element_with_wait(locator_formatted)

    @allure.step('Получение значения счетчика заказов')
    def getting_counter_order_total(self, locator_counter):
        # переходим в ленту
        self.transition_to_page_exception(MainPageLocators.BUTTON_ORDER_FEED, MainPageLocators.INSCRIPTION_ORDER_FEED,
                                          MainPageLocators.EXCEPTION)
        # получаем значение счетчика и сохранем в переменную
        counter_total = self.get_text_from_element(locator_counter)
        return counter_total # передаем переменную о значением счетчика

    @allure.step('Сравнение значения счетчика до создания заказа и после')
    def comparison_counters(self, locator_counter):
        counter_total = self.getting_counter_order_total(locator_counter) # получаем значение счетчика заказов в ленте
        # переходим в конструктор
        self.transition_to_page_exception(MainPageLocators.BUTTON_CONSTRUCTOR,
                                           MainPageLocators.INSCRIPTION_ASSEMBLE_BURGER, MainPageLocators.EXCEPTION)
        self.formation_burger(data.BURGER) # формируем бургер и оформляем заказ
        self.waiting_for_text_to_change(MainPageLocators.NUMBER_ORDER, '9999') # ждем отображения номера заказа
        self.close_order_window(MainPageLocators.BUTTON_CLOSE_ORDER, MainPageLocators.EXCEPTION)
        # получаем значение счетчика заказов в ленте
        new_counter_total = self.getting_counter_order_total(locator_counter)
        # если значение счетчика не изменилось, ждем изменения с снова получаем значение
        if new_counter_total == counter_total:
            self.waiting_for_text_to_change(locator_counter, counter_total)  # ждем отображения номера заказа
            # получаем значение счетчика заказов в ленте
            new_counter_total = self.getting_counter_order_total(locator_counter)
        return counter_total, new_counter_total # передаем значения счетчиков



    @allure.step('Заказы из истории отображаются в ленте')
    def search_orders_in_feed(self):
        # переходим в личный кабинет
        self.transition_to_page_exception(AccountPageLocators.BUTTON_PERSONAL_ACCOUNT, AccountPageLocators.TAB_PROFILE,
                                          MainPageLocators.EXCEPTION)
        # переходим в Историю
        self.transition_to_page_exception(AccountPageLocators.TAB_ORDER_HISTORY,
                                          AccountPageLocators.CONTAINER_HISTORY_ORDERS, MainPageLocators.EXCEPTION)
        number = self.get_text_from_element(FeedPageLocators.NUMBER_ORDER_HISTORY) # получаем номера заказа из истории
        # переходим в ленту
        self.transition_to_page_exception(MainPageLocators.BUTTON_ORDER_FEED, MainPageLocators.INSCRIPTION_ORDER_FEED,
                                           MainPageLocators.EXCEPTION)
        # форматируем локатор номера заказа
        locator_formatted = self.format_locators(FeedPageLocators.NUMBER_FEED, number)
        # находим заказа в ленте и возвращаем результат
        return self.find_element_with_wait(locator_formatted)
