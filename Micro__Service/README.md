# Создание микросервиса

## Установка и запуск

Проект разбит на 3 docker-контейнера:
- backend — бэкенд проекта (django+rest_framework)
- db — образ базы данных PostgreSQL
- nginx — web-сервер nginx

1. Склонировать репозиторий: ```git clone https://github.com/Valyaevgeorgiy/Coding_praktikum/tree/main/Micro__Service.git```
2. Установить: [docker](https://docs.docker.com/engine/install/ubuntu/), [docker-compose](https://docs.docker.com/compose/install/)
3. Перейти в директорию с проектом cобрать проект и запустить: ```sudo docker-compose up``` 
4. Собрать базу данных на основе ресурсов: ```sudo docker-compose exec backend python manage.py makemigrations && sudo docker-compose exec backend python manage.py migrate```
5. Создать профиль администратора: ```sudo docker-compose exec web python manage.py createsuperuser```
6. Собрать статику (встроенный frontend админки и rest_framework): ```sudo docker-compose exec web python manage.py collectstatic```

## Эндпоинты API

1. https://localhost/users/info - полная информация о пользователе
2. https://localhost/users/create - создание пользователя
3. https://localhost/users/password - смена пароля
4. https://localhost/users/token - получения bearer-токена для просмотра полной информации и смены пароля

## Работа Микросервиса

- Запуск микросервиса (загрузка и сборка контейнеров)
![img](https://github.com/bitcoineazy/Study_Practice/blob/main/images/microservice_startup.jpg)


- Сборка модели базы данных, статики и создание профиля администратора
![img](https://github.com/bitcoineazy/Study_Practice/blob/main/images/microservice_migrate_static_superuser.jpg) 


- Создание самоподписанного SSL сертификата и ключа OpenSSL ```openssl req -x509 -out localhost.crt -keyout localhost.key -newkey rsa:2048 -nodes -sha256 -subj '/CN=localhost'``` 


- Веб-интерфейс django REST framework'a
![img](https://github.com/bitcoineazy/Study_Practice/blob/main/images/microservice_users_info_web.jpg) 


- Процесс создание нового пользователя, используем Postman для взаимодействия с API
![img](https://github.com/bitcoineazy/Study_Practice/blob/main/images/microservice_users_create.jpg) 
- проверка сложности пароля
![img](https://github.com/bitcoineazy/Study_Practice/blob/main/images/microservice_pass_validate_1.jpg)
![img](https://github.com/bitcoineazy/Study_Practice/blob/main/images/microservice_pass_validate_2.jpg)
- создание пользователя с валидным паролем
![img](https://github.com/bitcoineazy/Study_Practice/blob/main/images/microservice_users_created.jpg)


- Процесс получения токена для работы с эндпоинтами, которые имеют ограничение на доступ (токен - условие для сервера, что пользователь залогинен)
![img](https://github.com/bitcoineazy/Study_Practice/blob/main/images/microservice_users_token.jpg) 
- Получение токена для пользователя (используя логин и пароль, указанный при создании пользователя)
![img](https://github.com/bitcoineazy/Study_Practice/blob/main/images/microservice_users_token_created.jpg) 


- Получение полной информации о пользователе из бд, используя токен
![img](https://github.com/bitcoineazy/Study_Practice/blob/main/images/microservice_users_info_wtoken.jpg) 


- Процесс смены пароля пользователя, используя токен
![img](https://github.com/bitcoineazy/Study_Practice/blob/main/images/microservice_users_password.jpg) 
- Смена пароля, указав новый пароль
![img](https://github.com/bitcoineazy/Study_Practice/blob/main/images/microservice_users_password_set.jpg) 


- Админ-панель django (просмотр и изменения записей в бд)
![img](https://github.com/bitcoineazy/Study_Practice/blob/main/images/microservice_admin_1.jpg) 
![img](https://github.com/bitcoineazy/Study_Practice/blob/main/images/microservice_admin_2.jpg) 


- Логи микросервиса
![img](https://github.com/bitcoineazy/Study_Practice/blob/main/images/microservice_logs.jpg) 


- Процесс подключения к серверной бд (PostgreSQL), используем DataGrip
![img](https://github.com/bitcoineazy/Study_Practice/blob/main/images/microservice_datagrip_prop.jpg) 
- Простейший SQL запрос к серверу
![img](https://github.com/bitcoineazy/Study_Practice/blob/main/images/microservice_datagrip.jpg)
