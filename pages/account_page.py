import allure
from pages.base_page import BasePage
from locators.account_page_locators import AccountPageLocators


class AccountPage(BasePage):


    @allure.step('Авторизация пользователя')
    def login_customer(self, data_customer):
        # ввод емэйла
        self.add_text_to_element(AccountPageLocators.FIELD_EMAIL, data_customer['email'])
        # ввод пароля
        self.add_text_to_element(AccountPageLocators.FIELD_PASSWORD, data_customer['password'])
        # нажатие кнопки входа
        self.click_to_element(AccountPageLocators.BUTTON_ENTRANCE)

    @allure.step('Поиск таба Профиль')
    def search_for_profile_tab(self):
        # ищем таб Профиль и передаем результата
        return self.find_element_with_wait(AccountPageLocators.TAB_PROFILE)

    @allure.step('Поиск надписи Вход')
    def search_inscription_entrance(self):
        # ищем надпись Вход и передаем результат
        return self.find_element_with_wait(AccountPageLocators.INSCRIPTION_ENTRANCE)

    @allure.step('Поиск контейнера истории')
    def search_order_history(self):
        # ищем контейнер истории и передаем результат
        return self.find_element_with_wait(AccountPageLocators.CONTAINER_HISTORY_ORDERS)

    @allure.step('Получение номера заказа в истории')
    def getting_orders_in_history(self):
        # получаем номера заказа из истории и передаем
        return self.get_text_from_element(AccountPageLocators.NUMBER_ORDER_HISTORY)

