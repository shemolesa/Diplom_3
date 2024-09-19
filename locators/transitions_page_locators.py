from selenium.webdriver.common.by import By

class TransitionsPageLocators:
    BUTTON_PERSONAL_ACCOUNT = By.XPATH, './/a[@href="/account"]' # кнопка "Личный кабинет"
    EXCEPTION_TRANSITIONS = By.XPATH, './/*[@class="Modal_modal_overlay__x2ZCr"]' # окно оверлея
    BUTTON_CONSTRUCTOR = By.XPATH, './/a[@href="/"]' # кнопка "Конструктор"
    BUTTON_ORDER_FEED = By.XPATH, './/p[text()="Лента Заказов"]' # кнопка "Лента Заказов"
    TAB_EXIT = By.XPATH, './/button[text()="Выход"]' # вкладка "Выход"
    TAB_ORDER_HISTORY = By.XPATH, './/a[text()="История заказов"]' # вкладка "История заказов"
    BUTTON_ENTRANCE_IN_ACCOUNT = By.XPATH, './/*[contains(@class,"button_button_size_large")]'  # кнопка "Войти в аккаунт" на главной странице
