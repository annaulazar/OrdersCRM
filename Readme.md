![Python](https://img.shields.io/badge/python-3670A0?style=for-the-badge&logo=python&logoColor=ffdd54)
![Django](https://img.shields.io/badge/django-%23092E20.svg?style=for-the-badge&logo=django&logoColor=white)
![Postgres](https://img.shields.io/badge/postgres-%23316192.svg?style=for-the-badge&logo=postgresql&logoColor=white)
![Bootstrap](https://img.shields.io/badge/bootstrap-%238511FA.svg?style=for-the-badge&logo=bootstrap&logoColor=white)
# Модуль распределения и мониторинга исполнения заявок клиентов
Веб-приложение для создания заявок клиентов, их распределения по исполнителям и мониторинга исполнения

## Бизнес-требования:
1) Фиксация в едином формате и в едином справочнике всю информацию по процессам работы с заявками
2) Ведение реестра клиентов и сотрудников
3) Отслеживание сроков исполнения задач
4) Разграничение прав доступа конечных пользователей:
  - Диспетчер:
    - отслеживание задач и управление ими
    - назначение исполнителя
  - Исполнитель:
    - Просмотр нарядов;
    - Ведение отчетности и заполнение документации.
  - Администратор:
    - Конфигурирование и настройка структуры персонала.
  - Клиент:
    - Создание заявки и подтверждение исполнения


## Реализация

- Приложение реализовано с помощью фреймворка Django.
- Отображение веб-страниц реализовано с помощью шаблонизатора Django и фреймворка Bootstrap
- База данных - PostgreSQL.


## Стек

- Django
- Django ORM
- PosgreSQL
- Bootstrap

## Зависимости
В файле requirements.txt

## Запуск
На сервере Postgres создать базу данных. Прописать в файле .env (переименовать .env_example) параметры подключения,
в директории проекта выполнить последовательно команды:

`python manage.py migrate`

`python manage.py runserver`