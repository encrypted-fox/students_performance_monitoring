# Правила

## Push 
Внимательно проверяйте свои коммиты, я вот уже запушил случайно папку .idea, никак её вытравить не могу отсюда.
Push делайте только в свои ветки. Назовите их своим ником. НЕ ДЕЛАЙТЕ PUSH в мастер!

## Сообщения в коммитах

```
[+] Added * v.0.1.e – Что-то добавлено
[-] Removed * v.0.1.e – Что-то удалено
[*] Updated * v.0.1.e – Что-то изменено
```

## Баги и предложения
Предложения и баги направляйте прямиком в Issues.

## Важное из ВК

Предлагаю дизайн – [буп](https://www.figma.com/file/687IPxcFUw0BjZM2txCywU)

Трело – [буп](https://vk.com/away.php?to=https%3A%2F%2Ftrello.com%2Finvite%2Fb%2F0AtfdCL7%2F2def16655bccf8c423c281810dfa2855%2F%25D0%25BC%25D0%25BE%25D0%25BD%25D0%25B8%25D1%2582%25D0%25BE%25D1%2580%25D0%25B8%25D0%25BD%25D0%25B3-20&cc_key=)

GitHub – отправил всем доступ, жду почту Марины Владимировны и ответ на доступ ото всех

GitHub + правила –
[буп](https://github.com/encrypted-fox/students_performance_monitoring/wiki/%D0%9F%D1%80%D0%B0%D0%B2%D0%B8%D0%BB%D0%B0-%D0%B8-%D1%83%D1%81%D1%82%D0%B0%D0%BD%D0%BE%D0%B2%D0%BA%D0%B0)

Бэкенд лежит [тут](https://students-monitor.herokuapp.com/)

# API. Руководство для пользователя - API. User guide

## Установка - Installation
1. Установите PostgreSQL и создайте сервер. – Install PostgreSQL and create server.
2. Создайте базу данных. – Create database.
3. В файле settings.py поменяйте следующие строки: – In file settings.py change the following words.
    ```
    # /students_performance_monitoring/settings.py
    ...
    
    # Database
    # https://docs.djangoproject.com/en/2.2/ref/settings/#databases

    DATABASES = {
        'default': {
            ...
            'NAME': 'students_performance_monitoring', # имя вашей базы данных / name of your database
            'USER': 'postgres', # ваше имя пользователя базы данных с привелегиями на внесение изменений / database username with priveleges
            'PASSWORD': 'root', # ваш пароль к базе данных для данного пользователя / your database password for current user
            'HOST': 'localhost', # ваш хост базы данных / your database host
            'PORT': '5433', # порт на котором находится база данных / your database port
        }
    }
    ```
4. Откройте терминал и, находясь в корне проекта, запустите последовательно приведенные команды: – Open terminal  in project root and run following commands:

    ```bash
    # /
    
    pipenv shell
    pipenv install
    python manage.py migrate
    python manage.py collectstatic
    python manage.py createsuperuser
    ```
5. Введите любые данные, они потом будут использоваться для доступа к панели создания пользователей и групп пользователей. – Enter any data – it will be used to get access to users and groups modifying.
6. Для запуска сервера на локальном устройстве, запустите команду: – For local run use the following command:

    ```bash
    # /
    python manage.py runserver
    ```
7. Перейдите на страницу ```/admin ```. Авторизируйтесь. – Go to page ```/admin ``` and perform authorization.
8. Перейдите на страницу ```/api/v0/o/applications ```. Создайте там новое приложение oauth2 со следующими данными – Go to page ```/api/v0/o/applications ``` and create a new oauth2 application with the follofing data:

```
Name: app, 
Client ID: FFkBdq6jhLkR8E9fZ2yXT1TWqchqfs0KHvA4QpmZ, 
Client Secret: jVUu2AllmRbYdvSGbPCDKzwfVWzViEUpwcilEuy0eI3wteFM2ol8XLwNA3CQb9E0wW9S1aJ14TKeS5X3xaezRnaIazkOD13gZT0iaBdu9ZBWQ5NRLzNMmHp5fpqN6nr7, 
Authorization Type: resource-owner passeord based
```

## Маршруты API - API Map
Для получения доступа к списку маршрутов и моделям в текстовом виде, пройдите по ссылке ```/api/v0/swagger/```, или ```/api/v0/redoc/```

To get access to API map and models in text view, follow the link ```/api/v0/swagger/```, or ```/api/v0/redoc/```

___
MPU 2019 - 2020
