from selenium.webdriver.common.by import By


class AccountPageLocators:
    TAB_PROFILE = By.XPATH, './/li[contains(@class, "Account_listItem")]//a[text() = "Профиль"]' # вкладка "Профиль"
    INSCRIPTION_ENTRANCE = By.XPATH, '.// h2[text() = "Вход"]' # надпись "Вход" на странице входа
    FIELD_EMAIL = By.XPATH, ".//*[text()='Email']/following-sibling::input" # поле ввода логина
    FIELD_PASSWORD = By.XPATH, ".//*[text()='Пароль']/following-sibling::input"   # поле ввода пароля
    BUTTON_ENTRANCE = By.XPATH, './/*[contains(@class,"button_button_size_medium")]' # кнопка "Войти" на странице авторизации
    CONTAINER_HISTORY_ORDERS = By.XPATH, './/div[contains(@class, "Account_contentBox")]' # контейнер истории заказов
    NUMBER_ORDER_HISTORY = By.XPATH, './/div[contains(@class, "OrderHistory_textBox")]//p[contains(@class, "text_type_digits-default")]' #номер заказа в истории

