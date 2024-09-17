import allure
import data
from locators.account_page_locators import AccountPageLocators
from pages.base_page import BasePage
from locators.main_page_locators import MainPageLocators
from helpers import formation_locators


class MainPage(BasePage):


    @allure.step('Просмотр деталей ингредиента')
    def view_ingredient_details(self):
        self.click_to_element(MainPageLocators.MENU_BUNS) # кликаем на карточку ингредиента
        # получаем атрибут 'class' модального окна и передаем
        return self.getting_element_attribute(MainPageLocators.MODAL_WINDOW_INGREDIENT, 'class')

    @allure.step('Закрытие окна просмотра деталей ингредиента')
    def close_ingredient_details(self):
        self.click_to_element(MainPageLocators.MENU_BUNS) # кликаем на карточку ингредиент
        self.click_to_element(MainPageLocators.BUTTON_CLOSE) # кликаем на кнопку закрытия окна
        # получаем атрибут 'class' модального окна и передаем
        return self.getting_element_attribute(MainPageLocators.MODAL_WINDOW_INGREDIENT, 'class')

    @allure.step('Добавление ингредиента в конструктор')
    def adding_ingredient(self, locators, quantity):
        if quantity == '1': # если это соус или начинка
            self.scroll_to_element(locators[0]) # скролим до элемента
        # перетаскиваем элемент в конструктор
        self.drag_and_drop_ingredient(locators[0], MainPageLocators.CONSTRUCTOR)
        return self.get_text_from_element(locators[1]) # получаем значение каунтера и передаем

    # @allure.step('Оформление заказа')
    # def registration_order(self):
    #     self.order_formation() # формируем бургер
    #     self.click_to_element(MainPageLocators.BUTTON_CHECKOUT) # нажимаем кнопку оформления заказа
    #     self.waiting_for_text_to_change(MainPageLocators.NUMBER_ORDER, '9999') # ждем получения номера заказа
    #     return self.get_text_from_element(MainPageLocators.NUMBER_ORDER) # получаем номер заказа и передаем

    @allure.step('Формирование заказа')
    def order_formation(self):
        locator = formation_locators(data.MENU_BUNS) # формирование локатора булки
        self.adding_ingredient(locator, '2') # добавление булки в конструктор
        locator = formation_locators(data.MENU_SAUCES) # формирование локатора соуса
        self.adding_ingredient(locator, '1') # добавление соуса в конструктор
        locator = formation_locators(data.MENU_FILLINGS) # формирование локатора начинки
        self.adding_ingredient(locator, '1') # добавление начинки в конструктор
        self.click_to_element(MainPageLocators.BUTTON_CHECKOUT) # нажимаем кнопку оформления заказа
        number = self.get_text_from_element(MainPageLocators.NUMBER_ORDER)  # считываем отображаемый номер заказа
        # ждем получения номера заказа и передаем
        self.waiting_for_text_to_change(MainPageLocators.NUMBER_ORDER, number)


    @allure.step('Получение номера оформленного заказа')
    def getting_order_counter(self):
        self.order_formation()
        return self.get_text_from_element(MainPageLocators.NUMBER_ORDER)

    @allure.step('Оформление заказа')
    def registration_order(self):
        self.order_formation()
        #self.click_to_element(MainPageLocators.BUTTON_CLOSE)
        self.close_order_window(MainPageLocators.BUTTON_CLOSE_ORDER, MainPageLocators.EXCEPTION)

    @allure.step('Переход по кнопке "Лента Заказов"')
    def transition_order_feed(self):
        # переходим в ленту
        return self.transition_to_page_exception(MainPageLocators.BUTTON_ORDER_FEED,
                                                  MainPageLocators.INSCRIPTION_ORDER_FEED, MainPageLocators.EXCEPTION)


    @allure.step('Переход по кнопке "Конструктор"')
    def transition_constructor(self):
        # переходим в профиль
        self.transition_to_page_exception(AccountPageLocators.BUTTON_PERSONAL_ACCOUNT,
                                          AccountPageLocators.TAB_PROFILE, MainPageLocators.EXCEPTION)
        # переходим в конструктор
        return self.transition_to_page_exception(MainPageLocators.BUTTON_CONSTRUCTOR,
                                                 MainPageLocators.INSCRIPTION_ASSEMBLE_BURGER,
                                                 MainPageLocators.EXCEPTION)
