from selenium.webdriver.common.by import By

class RecoveryPageLocators:
    BUTTON_RECOVER_PASSWORD = By.XPATH, './/a[@href="/forgot-password"]' #кнопка "Восстановить пароль"
    INSCRIPTION_PASSWORD_RECOVERY = By.XPATH, '.// h2[text() = "Восстановление пароля"]'  # надпись "Восстановление пароля" на странице восстановления пароля
    EMAIL_USER_PASSWORD_RECOVERY = By.XPATH, '.// input[contains( @class , "text_type_main-default")]' #поле ввода электронного адреса на странице восстановления пароля
    BUTTON_RECOVER = By.XPATH, '.// button[text() = "Восстановить"]' #кнопка "Восстановить" на странице восстановления пароля
    BUTTON_SAVE = By.XPATH, '.// button[text() = "Сохранить"]' #кнопка "Сохранить" на странице восстановления пароля
    INPUT_PASSWORD = (By.XPATH, ".//*[text()='Пароль']/following-sibling::input")   # поле ввода пароля
    BUTTON_SHOW_PASSWORD = (By.XPATH, '//label[text()="Пароль"]//parent::div')   # поле ввода пароля
    BUTTON_HIDE_PASSWORD = By.XPATH, './/div[contains(@class, "input_type_text")]' #кнопка скрыть пароль
    BUTTON = By.XPATH, './/div[contains(@class, "input_type_password")]//*[name()="svg"]'
    INSCRIPTION_ENTRANCE = By.XPATH, '.// h2[text() = "Вход"]'  # надпись "Вход" на странице входа
