# PIUS 2
## Структура проекта
```
PIUS2/
├── .env - конфигурационные данные
├── .env_template - шаблон конфигурационные данные
├── .gitignore
├── alembic/ - директория миграций
│   ├── env.py
│   ├── README
│   ├── script.py.mako
│   └── versions/
│       └── b8ef8d140649_initial.py
├── alembic.ini - конфиг миграций
├── apis/ - API's
│   ├── __init__.py
│   ├── base.py 
│   └── version1/
│       ├── __init__.py
│       ├── route_addresses.py - Router Address
│       └── route_customers.py - Router Customer
├── cli/ - 
│   ├── __init__.py
│   ├── count_addresses.py - позволяет получить число адресов для покупателя по id покупателя
│   └── seeder.py - заполнение базы данных 100 записями
├── core/
│   ├── __init__.py
│   └── config.py - конфиг, читающий данные из конфигурационного файла
├── db/ - подключение к базе данных, модели и методы получения данных из базы данных
│   ├── __init__.py
│   ├── base.py
│   ├── base_class.py
│   ├── models/ - модели
│   │   ├── __init__.py
│   │   ├── addresses.py
│   │   └── customers.py
│   ├── repository/ - методы для получения данных из бд
│   │   ├── __init__.py
│   │   ├── addresses.py
│   │   └── customers.py
│   └── session.py - создание сессии подключения к базе
├── main.py - запуск сервера
├── README.md
├── requirments.txt - файл зависимостей
├── schemas/ - request response схемы
│   ├── __init__.py
│   ├── addresses.py
│   └── customers.py
├── static/ - статичные файлы
│   └── images/
│       └── logo.png
├── templates/ - html файлы
│   ├── components/
│   │   ├── navbar.html
│   │   ├── table_addresses.html
│   │   └── table_customers.html
│   ├── general_pages/
│   │   ├── customer_detail.html
│   │   ├── customers.html
│   │   ├── homepage.html
│   │   └── not_found_customer.html
│   └── shared/
│       └── base.html
└── webapps/ - рендеринг страницы
    ├── __init__.py
    ├── base.py
    └── customers/
        ├── __init__.py
        └── route_customers.py
 ```
