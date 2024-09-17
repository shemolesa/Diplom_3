import allure
from selenium.common import ElementClickInterceptedException, TimeoutException
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.common.action_chains import ActionChains
from data import PAUSE

class BasePage:

    def __init__(self, driver):
        self.driver = driver

    @allure.step('Поиск элемента с ожиданием')
    def find_element_with_wait(self, locator):
        WebDriverWait(self.driver, PAUSE).until((expected_conditions.visibility_of_element_located(locator)))
        return self.driver.find_element(*locator)

    @allure.step('Ожидание изменения текста')
    def waiting_for_text_to_change(self, locator, text):
        WebDriverWait(self.driver, PAUSE).until_not((expected_conditions.text_to_be_present_in_element(locator, text)))
        return self.driver.find_element(*locator)

    @allure.step('поиск элемента с нажатием на него')
    def click_to_element(self, locator):
        self.find_element_with_wait(locator).click()

    @allure.step('Поиск элемента и ввод текста в поле')
    def add_text_to_element(self, locator, text):
        self.find_element_with_wait(locator).send_keys(text)

    @allure.step("получение текста элемента")
    def get_text_from_element(self, locator):
        return self.find_element_with_wait(locator).text

    @allure.step("форматирование локатора из списка")
    def format_locators(self, locator_original, number):
        method, locator = locator_original # делим исходный локатора на метод и путь
        locator = locator.format(number) # подставляем в путь номер
        return (method, locator)

    @allure.step("скролл до элемента")
    def scroll_to_element(self, locator):
        element = self.find_element_with_wait(locator)
        self.driver.execute_script("arguments[0].scrollIntoView();", element)

    @allure.step('Получение значения поля')
    def getting_element_attribute(self, locator, variable):
        value_field = self.driver.find_element(*locator) #находим поле ввода и сохраняем в переменную
        return value_field.get_attribute(variable) # получаем значение атрибута и передаем

    @allure.step('Клик по элементу с обработкой исключения')
    def click_to_element_exception(self, button, locator_exception):
        while True:
            try:
                self.click_to_element(button)
                break
            except ElementClickInterceptedException:
                try:
                    WebDriverWait(self.driver, PAUSE).until_not(expected_conditions.visibility_of_element_located(locator_exception))
                except ElementClickInterceptedException:
                    continue
                continue

    @allure.step("Закрытие окна с заказом")
    def close_order_window(self, element, locator_exception):
        while True:
            try:
                self.click_to_element(element)
                break
            except ElementClickInterceptedException:
                try:
                    WebDriverWait(self.driver, PAUSE).until_not(
                        expected_conditions.visibility_of_element_located(locator_exception))
                except TimeoutException:
                    continue
                continue

    @allure.step('Переход по кнопке на другую страницу')
    def transition_to_page_exception(self, button, element, locator_exception):
        self.click_to_element_exception(button, locator_exception)
        return self.find_element_with_wait(element)

    @allure.step('Перетаскивание ингредиента')
    def drag_and_drop_ingredient(self, locator_element, locator_target):
        element = self.find_element_with_wait(locator_element)
        target = self.find_element_with_wait(locator_target)
        ActionChains(self.driver).drag_and_drop(element, target).perform()

    @allure.step('Формирование бургера')
    def formation_burger(self, burger):
        self.drag_and_drop_ingredient(burger[0], burger[3])
        self.scroll_to_element(burger[1])
        self.drag_and_drop_ingredient(burger[1], burger[3])
        self.scroll_to_element(burger[2])
        self.drag_and_drop_ingredient(burger[2], burger[3])
        self.click_to_element(burger[4])

