from selenium.webdriver.common.by import By


class AccountPageLocators:
    BUTTON_PERSONAL_ACCOUNT = By.XPATH, './/a[@href="/account"]' # кнопка "Личный кабинет"
    TAB_PROFILE = By.XPATH, './/li[contains(@class, "Account_listItem")]//a[text() = "Профиль"]' # вкладка "Профиль"
    NAVIGATION_ACCOUNT = By.XPATH, '.// *[contains( @class , "Account_nav__Lgali")]' # раздел навигации в личном кабинете
    INSCRIPTION_ENTRANCE = By.XPATH, '.// h2[text() = "Вход"]' # надпись "Вход" на странице входа
    FIELD_EMAIL = By.XPATH, ".//*[text()='Email']/following-sibling::input" # поле ввода логина
    FIELD_PASSWORD = By.XPATH, ".//*[text()='Пароль']/following-sibling::input"   # поле ввода пароля
    BUTTON_ENTRANCE = By.XPATH, './/*[contains(@class,"button_button_size_medium")]' # кнопка "Войти" на странице авторизации
    TAB_EXIT = By.XPATH, './/button[text()="Выход"]' # вкладка "Выход"
    HISTORY_ORDERS = By.XPATH, './/*[contains(@class,"OrderHistory_listItem")]' # список заказов пользователя
    HISTORY_ORDERS1 = By.XPATH,  './/*[contains(@class, "OrderHistory_orderHistory")]/ul/li' # список заказов пользователя
    TAB_ORDER_HISTORY = By.XPATH, './/a[text()="История заказов"]' # вкладка "История заказов"
    CONTAINER_HISTORY_ORDERS = By.XPATH, './/div[contains(@class, "Account_contentBox")]' # контейнер истории заказов
    LIST_ORDERS = By.XPATH, './/li[contains(@class, "OrderHistory_listItem")]' # заказ в истории заказов
#    BUTTON_SAVE_PROFILE = By.XPATH, './/button[contains(@class, "button_button_type_primary") and text()="Сохранить"]'
    OVERLAY = By.XPATH, '//*[@class="Modal_modal_overlay__x2ZCr"]' # локатор невидимого модального окна