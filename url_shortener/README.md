# URL Shortener Service (Test Task for Applied AI)

Простой REST API-сервис для сокращения URL, реализованный на Django + Django REST Framework.


## Установка и запуск

1. Клонируй проект:
   ```bash
   git clone <your_repo_url>
   cd url_shortener

2. Установи зависимости:
    ```bach
   pip install -r requirements.txt

3. Создай .env файл в на уровне с файлом migrate.py
    ```env
   DJANGO_SECRET_KEY=...
   
4. Проведи миграцию, добавь суперпользователя и запусти сервер
    ```bash
   make migrate
    make createsuperuser
    make run
