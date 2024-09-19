import time

import allure
import data
from pages.base_page import BasePage
from locators.recovery_page_locators import RecoveryPageLocators


class RecoveryPage(BasePage):


    @allure.step('Переход к странице восстановления пароля')
    def proceed_to_password_recovery(self):
        # скролим до ссылки на восстановление пароля
        self.scroll_to_element(RecoveryPageLocators.BUTTON_RECOVER_PASSWORD)
        # нажимаем кнопку восстановления пароля
        self.click_to_element(RecoveryPageLocators.BUTTON_RECOVER_PASSWORD)

    @allure.step('Получение заголовка страницы восстановления пароля')
    def getting_page_title_password_recovery(self):
        self.proceed_to_password_recovery() # переходим к странице восстановления пароля
        # ищем надпись 'Восстановление пароля' и возвращаем текст надписи
        return self.get_text_from_element(RecoveryPageLocators.INSCRIPTION_PASSWORD_RECOVERY)

    @allure.step('Ввод адреса электронной почты')
    def entering_mail(self):
        self.proceed_to_password_recovery() # переходим к странице восстановления пароля
        # находим поле ввода и вводим емайл
        self.add_text_to_element(RecoveryPageLocators.EMAIL_USER_PASSWORD_RECOVERY, data.TEST_EMAIL)
        # получаем значение поля ввода и передаем
        return self.getting_element_attribute(RecoveryPageLocators.EMAIL_USER_PASSWORD_RECOVERY, 'value')

    @allure.step('Восстановление пароля')
    def password_recovery(self):
        self.proceed_to_password_recovery() # переходим к странице восстановления пароля
        # находим поле ввода и вводим емайл
        self.add_text_to_element(RecoveryPageLocators.EMAIL_USER_PASSWORD_RECOVERY, data.TEST_EMAIL)
        # находим кнопку "Восстановить" и нажимаем
        self.click_to_element(RecoveryPageLocators.BUTTON_RECOVER)

    @allure.step('Получение названия кнопки сохранения на странице ввода нового пароля')
    def getting_button_name_save(self):
        self.password_recovery() # выполняем восстановление пароля
        # ищем кнопку 'Сохранить' и возвращаем текст кнопки
        return self.get_text_from_element(RecoveryPageLocators.BUTTON_SAVE)

    @allure.step('Ввод нового пароля')
    def entering_new_password(self):
        self.password_recovery() # выполняем восстановление пароля
        self.add_text_to_element(RecoveryPageLocators.INPUT_PASSWORD, data.TEST_PASSWORD) # вводим пароль

    @allure.step('Просмотр введенного пароля')
    def show_password(self):
        self.entering_new_password()  # вводим пароль
        # нажимаем кнопку просмотра пароля
        self.click_element_with_wait_clickable(RecoveryPageLocators.BUTTON_EYE)
        # получаем значение атрибута 'class' и передаем
        return self.getting_element_attribute(RecoveryPageLocators.BUTTON_SHOW_PASSWORD, 'class')
