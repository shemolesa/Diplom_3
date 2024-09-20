## Дипломный проект. Задание 3: Веб-приложение

### Автотесты для проверки программы, которая помогает заказать бургер в Stellar Burgers

### Реализованные сценарии

Созданы тесты, проверяющие основной функционал, восстановление пароля, личный кабинет, раздел «Лента заказов»

Процент покрытия 100% (отчет: `htmlcov/index.html`)

### Структура проекта

- `locators` - пакет, содержащий локаторы страниц
- - 'account_pages_locators.py' - файл с локаторами страницы 'account_pages'
- - 'feed_pages_locators.py' - файл с локаторами страницы 'feed_page'
- - 'main_pages_locators.py' - файл с локаторами страницы 'main_page'
- - 'recovery_pages_locators.py' - файл с локаторами страницы 'recovery_page'
- - 'transitions_page_locators' - файл с локаторами страницы переходов
- `pages` - пакет, содержащий методы страниц
- - 'account_pages.py' - файл с методами страницы личного кабинета - 'account_pages'
- - - 'login_customer(data_customer)' - Авторизация пользователя
- - - 'search_for_profile_tab()' - Поиск таба Профиль
- - - 'search_inscription_entrance()' - Поиск надписи Вход
- - - 'search_order_history()' - Поиск контейнера истории
- - - 'getting_orders_in_history()' - Получение номера заказа в истории
- - 'base_pages.py' - файл с базовыми методами 
- - - 'find_element_with_wait (locator)' - Поиск элемента с ожиданием
- - - 'waiting_for_text_to_change(locator, text)' - Ожидание изменения текста
- - - 'click_to_element(locator)' - поиск элемента с нажатием на него
- - - 'click_element_with_wait_clickable(locator)' - поиск элемента с ожиданием кликабельности и нажатием на него
- - - 'add_text_to_element(locator, text)' - Поиск элемента и ввод текста в поле
- - - 'get_text_from_element(locator)' - получение текста элемента
- - - 'format_locators(locator_original, number)' - форматирование локатора из списка
- - - 'scroll_to_element(locator)' - скролл до элемента
- - - 'getting_element_attribute(locator, variable)' - Получение значения поля
- - - 'click_to_element_exception(button, locator_exception)' - Клик по элементу с обработкой исключения
- - - 'drag_and_drop_ingredient(locator_element, locator_target)' - Перетаскивание ингредиента
- - 'feed_pages.py' - файл с методами страницы ленты заказов  - 'feed_pages'
- - - 'search_inscription_feed()' - Поиск надписи Лента Заказов
- - - 'view_order_details' - Просмотр деталей заказа
- - - 'search_number_at_work()' - Проверка номера заказа в разделе "В работе"
- - - 'getting_counter_order_total(locator_counter)' - Получение значения счетчика заказов
- - - 'getting_counter_order_total_after(locator_counter, counter_before)' - Получение значения счетчика после создания заказа
- - - 'search_orders_in_feed()' - Поиск в ленте заказов из истории
- - 'main_pages.py' - файл с методами главной страницы - 'main_page'
- - - 'view_ingredient_details' - Просмотр деталей ингредиента
- - - 'close_ingredient_details()' - Закрытие окна просмотра деталей ингредиента
- - - 'adding_ingredient(locators, quantity)' - Добавление ингредиента в конструктор
- - - 'registration_order()' - Оформление заказа
- - - 'order_formation()' - Формирование заказа
- - - 'getting_order_counter()' - Получение номера оформленного заказа
- - - 'close_order_window()' - Закрытие окна заказа
- - - 'registration_order_with_number()' - Оформление заказа с получением номера
- - - 'registration_order()' - Оформление заказа
- - - 'search_inscription_constructor()' - Поиск надписи Соберите бургер
- - 'recovery_pages.py' - файл с методами страницы восстановления пароля - 'recovery_page'
- - - 'proceed_to_password_recovery()' - Переход к странице восстановления пароля
- - - 'getting_page_title_password_recovery()' - Получение заголовка страницы восстановления пароля
- - - 'entering_mail()' - Ввод адреса электронной почты
- - - 'password_recovery()' - Восстановление пароля
- - - 'getting_button_name_save()' - Получение названия кнопки сохранения на странице ввода нового пароля
- - - 'entering_new_password()' - Ввод нового пароля
- - - 'show_password()' - Просмотр введенного пароля
- - 'transitions_page.py' - файл с методами страницы переходов
- - - 'go_to_order_feed' - Переход в Ленту заказов
- - - 'go_to_constructor' - Переход в Конструктор
- - - 'login_to_personal_account' - Переход в личный кабинет с авторизацией
- - - 'logout_from_account' - Выход из аккаунта
- - - 'go_to_order_history' - Переход в раздел "История заказов"
- - - 'go_to_login_page' - Переход на страницу входа
- `tests` - пакет, содержащий тесты страниц
- - 'test_account_pages.py' - файл с тестами страницы 'account_pages'
- - - 'test_login_to_personal_account_authorized()' - проверка перехода в личный кабинет авторизованного пользователя
- - - 'test_login_to_personal_account_unauthorized()' - проверка перехода в личный кабинет без авторизации
- - - 'test_logout_from_account()' - Проверка выхода из аккаунта
- - - 'test_transition_order_history()' - Проверка перехода к разделу  "История заказов" под пользователями: без заказов и с заказами
- - 'test_feed_pages.py' - файл с тестами страницы 'feed_page'
- - - 'test_transition_order_feed(transition_page, feed_page)' - Проверка перехода по кнопке "Лента Заказов"
- - - 'test_view_order_details(feed_page, transition_page)' - Просмотр деталей заказа
- - - 'test_checking_new_order_in_progress(feed_page, transition_page, main_page, response_customer)' - Проверка наличия номера нового заказа в разделе "В работе"
- - - 'test_increasing_order_counter_total(feed_page, transition_page, main_page, response_customer, locator_counter)' - Проверка увеличения счетчика заказов за все время/за день при создании нового заказа
- - - 'test_view_order_in_feed(feed_page, transition_page, account_page, customer_authorized)' - Проверка отображения заказов из истории в ленте
- - 'test_main_pages.py' - файл с тестами страницы 'main_page'
- - - 'test_view_ingredient_details(main_page)' - Проверка просмотра деталей ингредиента
- - - 'test_close_ingredient_details(main_page)' - Проверка закрытия окна просмотра деталей ингредиента
- - - 'test_adding_ingredient(main_page, menu_ingredients, quantity)' - Проверка увеличения каунтера ингредиента при добавлении в заказ
- - - 'test_registration_order(main_page, response_customer)' - Проверка оформление заказа пользователем
- - - 'test_transition_constructor(main_page, transition_page)' - Проверка перехода по кнопке "Конструктор"
- - 'test_recovery_pages.py' - файл с тестами страницы 'recovery_page'
- - - 'test_proceed_to_password_recovery(transition_page, recovery_page)' - Получение заголовка страницы восстановления пароля 
- - - 'test_entering_mail(transition_page, recovery_page)' - Ввод адреса электронной почты
- - - 'test_password_recovery(transition_page, recovery_page)' - Проверка перехода на страницу ввода нового пароля после восстановления пароля
- - - 'test_show_password(transition_page, recovery_page)' - Проверка показа введенного пароля
- 'conftest.py' - файл с фикстурами
- - 'response_customer()' - Регистрация нового тестового покупателя, авторизация и последующее удаление
- - 'driver()' - Инициация драйвера  и последующее удаление
- - 'main_page()' - создание объекта главной страницы
- - 'recovery_page()' - создание объекта страницы личного кабинет
- - 'account_page()' - создание объекта страницы личного кабинета
- - 'feed_page()' - создание объекта страницы ленты заказов
- - 'customer_authorized()' - Регистрация нового тестового покупателя, авторизация, формирование заказов и последующее 
                              удаление
- 'data.py' - файл с тестовыми данными
- 'helpers.py' - 
- - 'generate_string()' - Генерация строкового значения
- - 'generate_email()' - Генерация email
- - 'generate_data_customer()' - Генерация данных покупателя для регистрации
- - 'generate_ingredient()' - Генерация ингредиента
- - 'formation_locators()' - Формирование локатора ингредиента
- - 'formation_ingredient_burger' - Формирование списка локаторов ингредиентов бургера
    

### Запуск автотестов

**Установка зависимостей**

> `$ pip install -r requirements.txt`

**Запуск автотестов и создание HTML-отчета о покрытии**

>  `$ pytest --cov=praktikum --cov-report=html`
 
**Запуск автотестов и генерирация Allure-отчёта**

> `$ pytest --alluredir=allure_results'
> '$ allure serve allure_results'

