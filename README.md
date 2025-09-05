## Дипломный проект. Задание 1: Юнит-тесты
<hr>

## Студент: Олег Шипулев

## <h>Когорта: #26</h>
<hr>

## <h>Автотесты для проверки программы, которая помогает заказать бургер в Stellar Burgers</h> 

### Реализованные сценарии

Созданы юнит-тесты, покрывающие класс `Burger`

Процент покрытия класса `Burger` 100% (отчет: `htmlcov/index.html`)

### Структура проекта

- `praktikum` - пакет, содержащий код программы
- `tests` - пакет, содержащий тесты

### Список тестов класса `Burger`

1. test_set_buns_success - проверка возможности выбора булочки
2. test_set_buns_multiple_times_success - проверка замены одной булочки на другую
3. test_add_ingredient_success - есть возможность добавления ингредиента
4. test_add_ingredient_multiple_times_success - можно добавить несколько ингредиентов
5. test_remove_ingredient_success - проверка возможности удалить ингредиент
6. test_move_ingredient_success - можно переместить ингредиент
7. test_get_price_success - проверка получения цены
8. test_get_receipt_success - проверка получения чека

### Запуск автотестов

**Установка зависимостей**

> `$ pip install -r requirements.txt`

**Запуск автотестов и создание HTML-отчета о покрытии**

>  `$ pytest --cov=praktikum --cov-report=html`
