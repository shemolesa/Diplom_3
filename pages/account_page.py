import allure
from pages.base_page import BasePage
from locators.account_page_locators import AccountPageLocators
from locators.main_page_locators import MainPageLocators


class AccountPage(BasePage):


    @allure.step('Авторизация пользователя')
    def login_customer(self, data_customer):
        # переход на страницу авторизации
        self.click_to_element(AccountPageLocators.BUTTON_PERSONAL_ACCOUNT)
        # ввод емэйла
        self.add_text_to_element(AccountPageLocators.FIELD_EMAIL, data_customer['email'])
        # ввод пароля
        self.add_text_to_element(AccountPageLocators.FIELD_PASSWORD, data_customer['password'])
        # нажатие кнопки входа
        self.click_to_element(AccountPageLocators.BUTTON_ENTRANCE)

    @allure.step('Переход в личный кабинет с авторизацией')
    def login_to_personal_account_authorized(self, data_customer):
        # переход в личный кабинет под авторизованным пользователем и передача результата
        return self.transition_to_page_exception(AccountPageLocators.BUTTON_PERSONAL_ACCOUNT,
                                          AccountPageLocators.TAB_PROFILE, MainPageLocators.EXCEPTION)

    @allure.step('Переход в личный кабинет без авторизации')
    def login_to_personal_account_unauthorized(self):
        # переход в личный кабинет без авторизации и передача результата
        return self.transition_to_page_exception(AccountPageLocators.BUTTON_PERSONAL_ACCOUNT,
                                                 AccountPageLocators.INSCRIPTION_ENTRANCE, MainPageLocators.EXCEPTION)

    @allure.step('Выход из аккаунта')
    def logout_from_account(self, data_customer):
        # переход в личный кабинет под авторизованным пользователем
        self.transition_to_page_exception(AccountPageLocators.BUTTON_PERSONAL_ACCOUNT,
                                          AccountPageLocators.TAB_PROFILE, MainPageLocators.EXCEPTION)
        # выход из ЛК и передача результата
        return self.transition_to_page_exception(AccountPageLocators.TAB_EXIT,
                                                 AccountPageLocators.INSCRIPTION_ENTRANCE, MainPageLocators.EXCEPTION)

    @allure.step('Переход в раздел "История заказов"')
    def transition_order_history(self):
        # переход в личный кабинет под авторизованным пользователем
        self.transition_to_page_exception(AccountPageLocators.BUTTON_PERSONAL_ACCOUNT,
                                          AccountPageLocators.TAB_PROFILE, MainPageLocators.EXCEPTION)
        # переход в Историю и передача результата
        return self.transition_to_page_exception(AccountPageLocators.TAB_ORDER_HISTORY,
                                                 AccountPageLocators.CONTAINER_HISTORY_ORDERS,
                                                 MainPageLocators.EXCEPTION)
