## Дипломный проект. Задание 3: Веб-приложение

### Автотесты для проверки программы, которая помогает заказать бургер в Stellar Burgers

### Реализованные сценарии

Созданы тесты, проверяющие основной функционал, восстановление пароля, личный кабинет, раздел «Лента заказов»

Процент покрытия 100% (отчет: `htmlcov/index.html`)

### Структура проекта

- `locators` - пакет, содержащий локаторы страниц
- - 'account_pages_locators.py' - файл с тестами страницы 'account_pages'
- - 'feed_pages_locators.py' - файл с тестами страницы 'feed_page'
- - 'main_pages_locators.py' - файл с тестами страницы 'main_page'
- - 'recovery_pages_locators.py' - файл с тестами страницы 'recovery_page'
- `pages` - пакет, содержащий методы страниц
- - 'account_pages.py' - файл с методами страницы личного кабинета - 'account_pages'
- - - 'login_customer()' - Авторизация пользователя
- - - 'login_to_personal_account_authorized()' - Переход в личный кабинет с авторизацией
- - - 'login_to_personal_account_unauthorized()' - Переход в личный кабинет без авторизации
- - - 'logout_from_account()' - Выход из аккаунта
- - - 'transition_order_history()' - Переход в раздел "История заказов"
- - 'base_pages.py' - файл с базовыми методами 
- - - 'find_element_with_wait ()' - Поиск элемента с ожиданием
- - - 'close_order_window()' - Закрытие окна с заказом
- - - 'waiting_for_text_to_change()' - Ожидание изменения текста
- - - 'click_to_element()' - поиск элемента с нажатием на него
- - - 'add_text_to_element()' - Поиск элемента и ввод текста в поле
- - - 'get_text_from_element()' - получение текста элемента
- - - 'format_locators()' - форматирование локатора из списка
- - - 'scroll_to_element()' - скролл до элемента
- - - 'getting_element_attribute()' - Получение значения поля
- - - 'transition_to_page_exception()' - Переход по кнопке на другую страницу'
- - - 'drag_and_drop_ingredient()' - Перетаскивание ингредиента
- - - 'click_to_element_exception' - Клик по элементу с обработкой исключения
- - - 'formation_burger()' - Формирование бургера
- - 'feed_pages.py' - файл с методами страницы ленты заказов - 'feed_page'
- - - 'view_order_details' - Просмотр деталей заказа
- - - 'search_number_at_work()' - Получение номера заказа и проверка его в разделе "В работе"
- - - 'getting_counter_order_total()' - Получение значения счетчика заказов
- - - 'comparison_counters()' - Сравнение значения счетчика до создания заказа и после
- - - 'search_orders_in_feed()' - Заказы из истории отображаются в ленте
- - 'main_pages.py' - файл с методами главной страницы  - 'main_page'
- - - 'view_ingredient_details' - Просмотр деталей ингредиента
- - - 'close_ingredient_details()' - Закрытие окна просмотра деталей ингредиента
- - - 'adding_ingredient()' - Добавление ингредиента в конструктор
- - - 'registration_order()' - Оформление заказа
- - - 'order_formation()' - Формирование заказа
- - - 'getting_order_counter' - Получение номера оформленного заказа
- - - 'transition_order_feed()' - Переход по кнопке "Лента Заказов"
- - - 'transition_constructor()' - Переход по кнопке "Конструктор"
- - 'recovery_pages.py' - файл с методами страницы восстановлени пароля 'recovery_page'
- - - 'proceed_to_password_recovery()' - Переход к странице восстановления пароля
- - - 'getting_page_title_password_recovery()' - Получение заголовка страницы восстановления пароля
- - - 'entering_mail()' - Ввод адреса электронной почты
- - - 'password_recovery()' - Восстановление пароля
- - - 'getting_button_name_save()' - Получение названия кнопки сохранения на странице ввода нового пароля
- - - 'entering_new_password()' - Ввод нового пароля
- - - 'show_password()' - Просмотр введенного пароля
- `tests` - пакет, содержащий тесты страниц
- - 'test_account_pages.py' - файл с тестами страницы 'account_pages'
- - - 'test_login_to_personal_account_authorized()' - проверка перехода в личный кабинет авторизованного пользователя
- - - 'test_login_to_personal_account_unauthorized()' - проверка перехода в личный кабинет без авторизации
- - - 'test_logout_from_account()' - Проверка выхода из аккаунта
- - - 'test_transition_order_history()' - Проверка перехода к разделу  "История заказов" под пользователями: без заказов и с заказами
- - 'test_feed_pages.py' - файл с тестами страницы 'feed_page'
- - - 'test_view_order_details()' - Просмотр деталей заказа
- - - 'test_checking_new_order_in_progress()' - Проверка наличия номера нового заказа в разделе "В работе"
- - - 'test_increasing_order_counter_total()' - Проверка увеличения счетчика заказов за все время/за день при создании нового заказа
- - - 'test_view_order_in_feed()' - Проверка отображения заказов из истории в ленте
- - 'test_main_pages.py' - файл с тестами страницы 'main_page'
- - - 'test_view_ingredient_details()' - Проверка просмотра деталей ингредиента
- - - 'test_close_ingredient_details()' - Проверка закрытия окна просмотра деталей ингредиента
- - - 'test_adding_ingredient()' - Проверка увеличения каунтера ингредиента при добавлении в заказ
- - - 'test_registration_order()' - Проверка оформление заказа пользователем
- - - 'test_transition_order_feed()' - Проверка перехода по кнопке "Лента Заказов"
- - - 'test_transition_constructor()' - Проверка перехода по кнопке "Конструктор"
- - 'test_recovery_pages.py' - файл с тестами страницы 'recovery_page'
- - - 'test_proceed_to_password_recovery()' - Получение заголовка страницы восстановления пароля 
- - - 'test_entering_mail()' - Ввод адреса электронной почты
- - - 'test_password_recovery()' - Проверка перехода на страницу ввода нового пароля после восстановления пароля
- - - 'test_show_password()' - Проверка показа введенного пароля
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

