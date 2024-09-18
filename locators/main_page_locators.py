from selenium.webdriver.common.by import By

class MainPageLocators:
    PERSONAL_ACCOUNT = By.XPATH, './/p[contains(@class,"AppHeader_header__linkText")]' #Личный Кабинет
    EXCEPTION = By.XPATH, './/*[@class="Modal_modal_overlay__x2ZCr"]' # окно оверлея
    BUTTON_ENTRANCE_IN_ACCOUNT = By.XPATH, './/*[contains(@class,"button_button_size_large")]'  # кнопка "Войти в аккаунт" на главной странице
    BUTTON_RECOVER_PASSWORD = By.XPATH, './/a[@href="/forgot-password"]' #кнопка "Восстановить пароль"
    INSCRIPTION_PASSWORD_RECOVERY = By.XPATH, '.// h2[text() = "Восстановление пароля"]'  # надпись "Восстановление пароля" на странице восстановления пароля
    EMAIL_USER_PASSWORD_RECOVERY = By.XPATH, '.// input[contains( @class , "text_type_main-default")]' #поле ввода электронного адреса на странице восстановления пароля
    BUTTON_RECOVER = By.XPATH, '.// button[text() = "Восстановить"]' #кнопка "Восстановить" на странице восстановления пароля
    BUTTON_SAVE = By.XPATH, '.// button[text() = "Сохранить"]' #кнопка "Сохранить" на странице восстановления пароля
    FIELD_PASSWORD = (By.XPATH, ".//*[text()='Пароль']/following-sibling::input")   # поле ввода пароля
    BUTTON_SHOW_PASSWORD = By.XPATH, './/div[contains(@class, "input_type_password")]' #кнопка показать пароль
    BUTTON_HIDE_PASSWORD = By.XPATH, './/div[contains(@class, "input_type_text")]' #кнопка скрыть пароль
    INSCRIPTION_INGREDIENT_DETAILS = By.XPATH, '.// h2[text() = "Детали ингредиента"]' #
    MENU_BUNS = By.XPATH, '//a[@href="/ingredient/61c0c5a71d1f82001bdaaa6d"]' # булка из меню
    COUNTER_BUN = By.XPATH, '//a[@href="/ingredient/61c0c5a71d1f82001bdaaa6d"]//p[@class="counter_counter__num__3nue1"]' # каунтер булки в меню
    MENU_SOUSES = By.XPATH, '//a[@href="/ingredient/61c0c5a71d1f82001bdaaa72"]' # соус из меню
    COUNTER_SOUSE = By.XPATH, '//a[@href="/ingredient/61c0c5a71d1f82001bdaaa72"]//p[@class="counter_counter__num__3nue1"]' # каунтер соуса в меню
    MENU_FILLINGS = By.XPATH, '//a[@href="/ingredient/61c0c5a71d1f82001bdaaa6e"]' # начинка из меню
    COUNTER_FILLING = By.XPATH, '//a[@href="/ingredient/61c0c5a71d1f82001bdaaa6e"]//p[@class="counter_counter__num__3nue1"]' # каунтер начинки в меню
    BUTTON_CLOSE = By.XPATH, './/button[contains(@class, "Modal_modal__close")]//*[name()="svg"]' #кнопка закрытия окна просмотра ингредиента
    MODAL_WINDOW = By.XPATH, '//section[contains(@class, "Modal_modal_opened__3ISw4")]'
    MODAL_WINDOW_INGREDIENT = By.XPATH, './/section[contains(@class, "Modal_modal__P3_V5")]' # окно просмотра деталей ингредиента
    BUTTON_CONSTRUCTOR = By.XPATH, './/a[@href="/"]' # кнопка "Конструктор"
    INSCRIPTION_ASSEMBLE_BURGER = By.XPATH, './/h1[contains(@class, "text")]' # надпись "Соберите бургер"
    CONSTRUCTOR = By.XPATH, './/ul[contains(@class, "BurgerConstructor_basket__list")]'
    BUTTON_CHECKOUT = By.XPATH, '.// button[text() = "Оформить заказ"]' # кнопка "Оформить заказ"
    NUMBER_ORDER = By.XPATH, './/h2[contains(@class, "Modal_modal__title_shadow")]' #номер заказа
    BUTTON_ORDER_FEED = By.XPATH, './/p[text()="Лента Заказов"]' # кнопка "Лента Заказов"
    INSCRIPTION_ORDER_FEED = By.XPATH, './/div[contains(@class,"OrderFeed_orderFeed__2RO")]//h1[text()="Лента заказов"]' # заголовок в ленте заказов
    BUTTON_CLOSE_ORDER = By.XPATH, '//*[contains(@class, "Modal_modal__close")]'

