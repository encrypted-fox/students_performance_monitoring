# API. Руководство для пользователя - API. User guide
## Установка - Installation
1. Установите PostgreSQL и создайте сервер. - Install PostgreSQL and create server.
2. Создайте базу данных. - Create database.
3. В файле settings.py поменяйте следующие строки: - In file settings.py change the following words.
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
4. Откройте терминал и, находясь в корне проекта, запустите последовательно приведенные команды: - Open terminal  in project root and run following commands:

    ```bash
    # /
    
    pipenv shell
    pipenv install
    python manage.py migrate
    python manage.py collectstatic
    python manage.py createsuperuser
    ```
5. Введите любые данные, они потом будут использоваться для доступа к панели создания пользователей и групп пользователей. - Enter any data - it will be used to get access to users and groups modifying.
6. Для запуска сервера на локальном устройстве, запустите команду: - For local run use the following command:

    ```bash
    # /
    python manage.py runserver
    ```
## Маршруты API - API Map
Для получения доступа к списку маршрутов и моделям в текстовом виде, пройдите по ссылке ```/api/v0/swagger/```, или ```/api/v0/redoc/```

To get access to API map and models in text view, follow the link ```/api/v0/swagger/```, or ```/api/v0/redoc/```

___
MPU 2019 - 2020
