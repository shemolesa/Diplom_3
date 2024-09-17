from selenium.webdriver.common.by import By

class RecoveryPageLocators:
#    BUTTON_ENTRANCE_IN_ACCOUNT = By.XPATH, './/*[contains(@class,"button_button_size_large")]'  # кнопка "Войти в аккаунт" на главной странице
    BUTTON_RECOVER_PASSWORD = By.XPATH, './/a[@href="/forgot-password"]' #кнопка "Восстановить пароль"
    INSCRIPTION_PASSWORD_RECOVERY = By.XPATH, '.// h2[text() = "Восстановление пароля"]'  # надпись "Восстановление пароля" на странице восстановления пароля
    EMAIL_USER_PASSWORD_RECOVERY = By.XPATH, '.// input[contains( @class , "text_type_main-default")]' #поле ввода электронного адреса на странице восстановления пароля
    BUTTON_RECOVER = By.XPATH, '.// button[text() = "Восстановить"]' #кнопка "Восстановить" на странице восстановления пароля
    BUTTON_SAVE = By.XPATH, '.// button[text() = "Сохранить"]' #кнопка "Сохранить" на странице восстановления пароля
#    FIELD_PASSWORD = (By.XPATH, '//label[text()="Пароль"]//parent::div')   # поле ввода пароля
    INPUT_PASSWORD = (By.XPATH, ".//*[text()='Пароль']/following-sibling::input")   # поле ввода пароля
    BUTTON_SHOW_PASSWORD = (By.XPATH, '//label[text()="Пароль"]//parent::div')   # поле ввода пароля
#    BUTTON_SHOW_PASSWORD = By.XPATH, './/div[contains(@class, "input_type_password")]' #кнопка показать пароль
    BUTTON_HIDE_PASSWORD = By.XPATH, './/div[contains(@class, "input_type_text")]' #кнопка скрыть пароль
    BUTTON = By.XPATH, './/div[contains(@class, "input_type_password")]//*[name()="svg"]'
    # INSCRIPTION_INGREDIENT_DETAILS = By.XPATH, '.// h2[text() = "Детали ингредиента"]' #
    # MENU_BUNS = By.XPATH, '//a[@href="/ingredient/61c0c5a71d1f82001bdaaa6d"]' # булка из меню
    # BUTTON_CLOSE = By.XPATH, './/button[contains(@class, "Modal_modal__close")]//*[name()="svg"]' #кнопка закрытия окна просмотра ингредиента
    # MODAL_WINDOW = By.XPATH, '//section[contains(@class, "Modal_modal__P3_V5")]' # окно просмотра деталей ингредиента
    # BUTTON_CONSTRUCTOR = By.XPATH, './/a[@href="/"]' # кнопка "Конструктор"
    # INSCRIPTION_ASSEMBLE_BURGER = By.XPATH, './/h1[contains(@class, "text")]' # надпись "Соберите бургер"
    INSCRIPTION_ENTRANCE = By.XPATH, '.// h2[text() = "Вход"]'  # надпись "Вход" на странице входа
