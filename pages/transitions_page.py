import allure
from pages.base_page import BasePage
from locators.transitions_page_locators import TransitionsPageLocators


class TransitionsPage(BasePage):


    @allure.step('Переход в Ленту заказов')
    def go_to_order_feed(self):
        self.click_to_element_exception(TransitionsPageLocators.BUTTON_ORDER_FEED,
                                        TransitionsPageLocators.EXCEPTION_TRANSITIONS)

    @allure.step('Переход в Конструктор')
    def go_to_constructor(self):
        self.click_to_element_exception(TransitionsPageLocators.BUTTON_CONSTRUCTOR,
                                        TransitionsPageLocators.EXCEPTION_TRANSITIONS)

    @allure.step('Переход в личный кабинет с авторизацией')
    def login_to_personal_account(self):
        self.click_to_element_exception(TransitionsPageLocators.BUTTON_PERSONAL_ACCOUNT,
                                        TransitionsPageLocators.EXCEPTION_TRANSITIONS)

    @allure.step('Выход из аккаунта')
    def logout_from_account(self):
        self.click_to_element_exception(TransitionsPageLocators.TAB_EXIT,
                                        TransitionsPageLocators.EXCEPTION_TRANSITIONS)

    @allure.step('Переход в раздел "История заказов"')
    def go_to_order_history(self):
        self.click_to_element_exception(TransitionsPageLocators.TAB_ORDER_HISTORY,
                                        TransitionsPageLocators.EXCEPTION_TRANSITIONS)

    @allure.step('Переход на страницу входа')
    def go_to_login_page(self):
        self.click_to_element(TransitionsPageLocators.BUTTON_ENTRANCE_IN_ACCOUNT)
