> Каждый пишет в своей отдельной ветке

> Предлагаю формат : `%NAME%-%DevUnit%-%Dev|Main%`

> EX: `Alan-Ux/Ui-Dev`

### Оформление коммитов
###### [+] Добавление нового функционала
###### [-] Удаление функции
###### [*] Bug fixed
###### [#] TODO
###### [X] Удаление файла
###### [$] Версия кода
### Version Naming System
###### `%v.[0-9].[0-9].[a-e]%`
> `v.0.0.a -> v.0.0.b -> ... -> v.0.0.e -> v.0.1.a -> ... -> v.0.1.e -> v.1.0a -> ... -> v.1.0e`


------------


Отслеживание задач - в [доске трелло](https://trello.com/b/UXrKkLRL/%D0%BC%D0%BE%D0%BD%D0%B8%D1%82%D0%BE%D1%80%D0%B8%D0%BD%D0%B3-%D1%83%D1%81%D0%BF%D0%B5%D0%B2%D0%B0%D0%B5%D0%BC%D0%BE%D1%81%D1%82%D0%B8 "trello board").
 

------------


# API. Руководство для пользователя
## Установка
1. Установите PostgreSQL и создайте сервер.
2. Создайте базу данных.
3. В файле settings.py поменяйте следующие строки:
    ```
    # /students_performance_monitoring/settings.py
    ...
    
    # Database
    # https://docs.djangoproject.com/en/2.2/ref/settings/#databases

    DATABASES = {
        'default': {
            ...
            'NAME': 'students_performance_monitoring', # имя вашей базы данных
            'USER': 'postgres', # ваше имя пользователя базы данных с привелегиями на внесение изменений
            'PASSWORD': 'root', # ваш пароль к базе данных для данного пользователя
            'HOST': 'localhost', # ваш хост базы данных
            'PORT': '5433', # порт на котором находится база данных
        }
    }
    ```
4. Откройте терминал и, находясь в корне проекта, запустите последовательно приведенные команды:
    ```bash
    # /
    
    pipenv shell
    pipenv install
    python manage.py migrate
    python manage.py collectstatic
    python manage.py createsuperuser
    ```
5. Введите любые данные, они потом будут использоваться для доступа к панели создания пользователей и групп пользователей.
6. Для запуска сервера на локальном устройстве, запустите команду:

    ```bash
    # /
    python manage.py runserver
    ```
## Маршруты API
Для получения доступа к списку маршрутов и моделям в текстовом виде, пройдите по ссылке ```/api/v0/swagger/```, или ```/api/v0/redoc/```

___
MPU 2019 - 2020
