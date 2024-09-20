from selenium.webdriver.common.by import By

class MainPageLocators:
    MENU_BUNS = By.XPATH, '//a[@href="/ingredient/61c0c5a71d1f82001bdaaa6d"]' # булка из меню
    MENU_SOUSES = By.XPATH, '//a[@href="/ingredient/61c0c5a71d1f82001bdaaa72"]' # соус из меню
    MENU_FILLINGS = By.XPATH, '//a[@href="/ingredient/61c0c5a71d1f82001bdaaa6e"]' # начинка из меню
    BUTTON_CLOSE = By.XPATH, './/button[contains(@class, "Modal_modal__close")]//*[name()="svg"]' #кнопка закрытия окна просмотра ингредиента
    MODAL_WINDOW_INGREDIENT = By.XPATH, './/section[contains(@class, "Modal_modal__P3_V5")]' # окно просмотра деталей ингредиента
    INSCRIPTION_ASSEMBLE_BURGER = By.XPATH, './/h1[contains(@class, "text")]' # надпись "Соберите бургер"
    CONSTRUCTOR = By.XPATH, './/ul[contains(@class, "BurgerConstructor_basket__list")]' # конструктор бургера
    BUTTON_CHECKOUT = By.XPATH, '.// button[text() = "Оформить заказ"]' # кнопка "Оформить заказ"
    NUMBER_ORDER = By.XPATH, './/h2[contains(@class, "Modal_modal__title_shadow")]' #номер заказа
    BUTTON_CLOSE_ORDER = By.XPATH, '//button[contains(@class, "Modal_modal__close__TnseK")]' # кнопка закрытия окна заказа