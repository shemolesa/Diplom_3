import allure
from data import TEST_EMAIL


class TestRecoveryPage:


    @allure.description('Переходим на страницу авторизации и по нажатию кнопки "Восстановить пароль" '
                        'переходим на страницу восстановления пароля')
    @allure.title('Проверка перехода на страницу восстановления пароля по кнопке "Восстановить пароль"')
    def test_proceed_to_password_recovery(self, transition_page, recovery_page):
        transition_page.go_to_login_page() # нажимаем кнопку входа в аккаунт и переходим на страницу входа
        #переходим на страницу восстановления пароля и проверяем отображение надписи "Восстановление пароля"
        assert recovery_page.getting_page_title_password_recovery() == 'Восстановление пароля'

    @allure.description('Переходим на страницу авторизации и по нажатию кнопки "Восстановить пароль" переходим на '
                        'страницу восстановления пароля. Вводим емэйл в поле ввода')
    @allure.title('Проверка ввода почты для восстановления пароля')
    def test_entering_mail(self, transition_page, recovery_page):
        transition_page.go_to_login_page() # нажимаем кнопку входа в аккаунт и переходим на страницу входа
        # проверяем введенный текст в поле ввода
        assert recovery_page.entering_mail() == TEST_EMAIL

    @allure.description('Переходим на страницу авторизации и по нажатию кнопки "Восстановить пароль" переходим '
                        'на страницу восстановления пароля. Вводим емэйл в поле ввода и нажимаем кнопку "Восстановить"')
    @allure.title('Проверка перехода на страницу ввода нового пароля после восстановления пароля')
    def test_password_recovery(self, transition_page, recovery_page):
        transition_page.go_to_login_page() # нажимаем кнопку входа в аккаунт и переходим на страницу входа
        # проверяем отображение кнопки "Сохранить" в форме ввода нового пароля
        assert recovery_page.getting_button_name_save() == 'Сохранить'

    @allure.description("Переходим на страницу авторизации и по нажатию кнопки 'Восстановить пароль' переходим "
                        "на страницу восстановления пароля. Вводим емэйл в поле ввода и нажимаем кнопку 'Cохранить'. "
                        "Вводим пароль и нажимаем на кнопку просмотра пароля")
    @allure.title('Проверка показа введенного пароля')
    def test_show_password(self, transition_page, recovery_page):
        transition_page.go_to_login_page() # нажимаем кнопку входа в аккаунт и переходим на страницу входа
        # проверяем наличие признака активности в классе поля
        assert 'input_status_active' in recovery_page.show_password()

