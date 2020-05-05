#### Условия запуска
Для проекта необходим Python 3.6-3.7  

_Используется_:  
- f-string (Python3.6+)
- Django 1.11.29 (Python 3.7-)


#### Запуск
**Terminal 1**
- Запуск PostgrSQL, redis, wkhtmltopdf  
`docker-compose up`

**Terminal 2**
- Установка зависимостей  
`pip install -r requirements.txt`

- Создание и применение миграций  
`python manage.py makemigrations`  
`python manage.py migrate`

- Создание администратора  
`python manage.py createsuperuser`

- Применение fixture  
`python manage.py loaddata checkgen/fixtures/initial_data.json`

- Запуск django-rq workers  
`python manage.py rqworker default`

**Terminal 3**
- Запуск сервера  
`python manage.py runserver`