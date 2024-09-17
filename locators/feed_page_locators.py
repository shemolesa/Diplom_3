from selenium.webdriver.common.by import By

class FeedPageLocators:

    TOTAL_ORDERS = By.XPATH, '//*[contains(@class, "text_type_main-medium") and text()="Выполнено за все время:"]/following-sibling::p'
    TOTAL_ORDERS_TODAY = By.XPATH, '//*[contains(@class, "text_type_main-medium") and text()="Выполнено за сегодня:"]/following-sibling::p'
    LAST_ORDER_CARD = By.XPATH, './/*[contains(@class, "OrderFeed_contentBox")]/ul/li[last()]' # последний заказ в ленте
    MODAL_WINDOW = By.XPATH, '//section[contains(@class, "Modal_modal_opened__3ISw4")]' # окно просмотра деталей заказа
    LIST_ORDER_CARDS = By.XPATH, './/*[contains(@class, "OrderFeed_contentBox")]/ul/li' #
#    M_W = By.XPATH, './/section[contains(@class, "Modal_modal__P3_V5")]' # окно просмотра деталей ингредиента
    ORDER_AT_WORK = By.XPATH, '//ul[contains(@class, "OrderFeed_orderListReady")]//li[text()="{}"]' # элемент списка "В работе"
    ORDERS_READY = By.XPATH, '//ul[contains(@class, "OrderFeed_orderListReady")]//li' # список "В работе"
    NUMBER_ORDER_HISTORY = By.XPATH, './/div[contains(@class, "OrderHistory_textBox")]//p[contains(@class, "text_type_digits-default")]' #номер заказа в истории
    NUMBER_FEED1 = By.XPATH, './/div[contains(@class, "OrderHistory_textBox")]//p[contains(@class, "text_type_digits-default") and text()="{}"]' # номер заказа в ленте
    NUMBER_FEED = By.XPATH, './/p[contains(@class, "text_type_digits-default") and text()="{}"]'  # номер заказа в ленте
    NUMBERS_READY = By.XPATH, '//ul[contains(@class, "OrderFeed_orderList__cBvyi")]//li' # список "В работе"
