Auto Mailing

Тестовое задание от Фабрики Решений

Сервис уведомлений - создание автоматических рассылок для пользователей.
Руководство по работе с проектом для разработчиков
Требования

    python=3.8.10

Настройка и установка проекта

    Склонировать репозиторий с помощью команды:

    git clone https://github.com/alinocco/auto-mailing.git

    Перейти в папку с проектом:

    cd auto-mailing

    Установить poetry:

    pip3 install poetry

    Активировать виртуальное окружение:

    poetry shell

    Установить зависимости:

    poetry install

    Установить Docker и docker-compose с официального сайта

    Запустить сервисы в Docker (PostgreSQL, Redis):

    docker-compose -f basic-compose.yml up -d --build --remove-orphans

    Получить креды от внешних сервисов и положить их в папку conf. Для проверки оставляю открытым файл .env.

    Применить миграции:

    python3 src/manage.py migrate

    Запустить сервер приложения:

    python3 src/manage.py runserver

    При необходимости запустить Celery:

    cd src && celery -A automailing worker -B -l INFO