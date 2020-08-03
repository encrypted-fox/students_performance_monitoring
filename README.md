# Правила

## Push

Внимательно проверяйте свои коммиты.
Push делайте только в свои ветки. Назовите их своим ником. НЕ ДЕЛАЙТЕ PUSH в мастер!

## Сообщения в коммитах ///МАСШТАБНОЕ ИЗМЕНЕНИЕ СИСТЕМЫ ВЕРСИОНИРОВАНИЯ///

Начиная с версии v.0.1.h, мы начинаем использовать семантическое версионирование. Следующая версия будет обозначена как v.0.1.0

    ```
    [+] Added <изменение – имя фала, для каждого из файлов> <версия в формате v.0.0.a, где цифры изменяются от 0, а буква в конце от a до z>  – Что-то добавлено
    [-] Removed <изменение – имя фала, для каждого из файлов> <версия в формате v.0.0.a, где цифры изменяются от 0, а буква в конце от a до z> – Что-то удалено
    [*] Updated <изменение – имя фала, для каждого из файлов> <версия в формате v.0.0.a, где цифры изменяются от 0, а буква в конце от a до z> – Что-то изменено
    ```

## Баги и предложения

Предложения и баги направляйте прямиком в Issues.

## Важное из ВК

Предлагаю дизайн – [буп](https://www.figma.com/file/687IPxcFUw0BjZM2txCywU)

Трело – [буп](https://trello.com/b/0AtfdCL7/мониторинг-20)

GitHub – отправил всем доступ, жду почту Марины Владимировны и ответ на доступ ото всех

GitHub + правила –
[буп](https://github.com/encrypted-fox/students_performance_monitoring/wiki/%D0%9F%D1%80%D0%B0%D0%B2%D0%B8%D0%BB%D0%B0-%D0%B8-%D1%83%D1%81%D1%82%D0%B0%D0%BD%D0%BE%D0%B2%D0%BA%D0%B0)

Бэкенд лежит [тут](https://students-monitor.herokuapp.com/)

# API. Руководство для пользователя

## Установка - Installation

1. Установите PostgreSQL и создайте сервер.
2. Создайте базу данных.
3. Добавьте секретные ключи в окружение. Вы можете получить ключи у [тимлида проекта](https://github.com/encrypted-fox).
4. Для пользователей Windows: запустите последовательно файлы `.scripts/install.bat`, `.scripts/createadmin.bat`, выполните шаги номер 7, 9, 10, запустите файл `.scripts/start.bat`. Установка будет завершена.
5. Для пользователей Unix: файлы установки в процессе создания и будут добавлены ближе к следующему релизу.
6. Полльзователи Unnix могут выполнить следующие действия для установки. Откройте терминал и, находясь в корне проекта, запустите последовательно приведенные команды:

    ```bash
    # /

    pipenv shell
    pipenv install
    python manage.py makemigrations
    python manage.py migrate
    python manage.py collectstatic
    python manage.py createsuperuser
    ```

7. Введите любые данные, они потом будут использоваться для доступа к панели создания пользователей и групп пользователей.
8. Для запуска сервера на локальном устройстве, запустите команду:

    ```bash
    # /

    python manage.py runserver
    ```

9. Перейдите на страницу `/api/v0/admin`. Авторизируйтесь.
10. Перейдите на страницу `/api/v0/auth/o/applications`. Создайте там новое приложение oauth2 со следующими данными:

    ```
    Name: swagger,
    Client ID: <Вставьте сюда SP_OAUTH2_CLIENT_ID>,
    Client Secret: Вставьте сюда SP_OAUTH2_CLIENT_SECRET>,
    Client Type: Confidential,
    Authorization Type: resource-owner passeord based
    ```

## Маршруты API

Для получения доступа к списку маршрутов и моделям в текстовом виде, пройдите по ссылке `/api/v0/swagger/`, или `/api/v0/redoc/`

---

MPU 2019 - 2020
