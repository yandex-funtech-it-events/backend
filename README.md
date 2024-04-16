# Yandex FunTech IT Meetups API

## Оглавление <a id="contents"></a>

1. [О проекте](#about)
2. [Авторы проекта](#authors)
3. [Документация](#documentation)
4. [Стек технологий](#tools)
5. [Установка зависимостей](#installation)
6. [Запуск](#start)
7. [CI/CD](#cicd)
8. [Frontend](#frontend)


## О проекте <a id="about"></a>

Сервис для участников it мероприятий.

[https://meetup.ddns.net/](https://meetup.ddns.net/)


## Авторы проекта <a id="authors"></a>

Команда:

- Product manager
  - Морозов Алексей (TG) [@alxmorozov](https://t.me/alxmorozov)

- Project manager
  - Петелина Александра (TG) [@Picha_pich](https://t.me/Picha_pich)

- Business analytics
  - Павлова Мария (TG [@MariaPavlova111](https://t.me/MariaPavlova111))

- System analytics
  - Джага Артем (TG [@purple_SU](https://t.me/purple_SU))
  - Титов Владислав (TG [@Vladislav7](https://t.me/Vladislav7))
  - Дунаевский Евгений (TG [@Evgeniy_Dunaevskiy](https://t.me/Evgeniy_Dunaevskiy))

- Designers
  - Суслов Андрей (TG [@s_aandrei](https://t.me/s_aandrei))
  - Черепова Александра (TG [@Cherepova_alex](https://t.me/Cherepova_alex))

- Frontend
  - [Мытников Дмитрий](https://github.com/Dimitry-prog) (TG [@Dmitry_Myt](https://t.me/Dmitry_Myt))
  - [Боднюк Анастасия](https://github.com/Chill-Peppa) (TG [@chill_peppa](https://t.me/chill_peppa))

- Backend
  - [Лашков Павел](https://github.com/hutji) (TG [@hutjinator](https://t.me/hutjinator))
  - [Бобков Константин](https://github.com/deltabobkov) (TG [@Bi_oKey](https://t.me/Bi_oKey))
  - [Сидельцева Мария](https://github.com/mvs51) (TG [@sub_mar](https://t.me/sub_mar))

## Документация <a id="documentation"></a>

Документация сгенерирована при помощи drf-spectacular.

[Swagger](https://meetup.ddns.net/api/v1/schema/swagger/)

[Redoc](https://meetup.ddns.net/api/v1/schema/redoc/)

## Стек технологий <a id="tools"></a>

[![Python](https://img.shields.io/badge/Python-3.11-blue)](https://www.python.org/)
[![Django](https://img.shields.io/badge/Django-4.2-green)](https://www.djangoproject.com/)
[![Django REST Framework](https://img.shields.io/badge/DRF-3.15.1-orange)](https://www.django-rest-framework.org/)
[![PostgreSQL](https://img.shields.io/badge/PostgreSQL-blue)](https://www.postgresql.org/)
[![Docker](https://img.shields.io/badge/Docker-blue)](https://www.docker.com/)
[![Nginx](https://img.shields.io/badge/Nginx-alpine-brightgreen)](https://nginx.org/)
[![drf-spectacular](https://img.shields.io/badge/drf--spectacular-0.27.1-blue)](https://drf-spectacular.readthedocs.io/)
[![simple-jwt](https://img.shields.io/badge/simple–jwt-5.3.1-green)](https://github.com/SimpleJWT/django-rest-framework-simplejwt)
![GitHub](https://img.shields.io/badge/GitHub-100000?style=for-the-badge&logo=github&logoColor=white)

## Установка зависимостей для локального разворачивания проекта<a id="installation"></a>

1. Склонируйте репозиторий:

  ```
    git clone git@github.com:yandex-funtech-it-events/backend.git
    cd backend
  ```

  2. В корневой директории создайте .env файл:
  ```
    cd backend
    touch .env
  ```

3. Заполните по примеру своими значениями:
  [скопируйте этот файл](.env.example)

## Запуск <a id="start"></a>

Запустите контейнеры с проектом следующей командой:
  ```
    docker compose up -d
  ```

Выполните миграции:
  ```
    docker compose exec backend python manage.py makemigrations
    docker compose exec backend python manage.py migrate
  ```

Создайте суперпользователя:
  ```
    docker compose exec backend python manage.py createsuperuser
  ```

Зайти в админ-панель:
[Admin](http://127.0.0.1:8000/admin/)

Посмотреть документацию:
[Swagger](http://127.0.0.1:8000/api/v1/schema/swagger/)

## CI/CD
### Описание и настройка

- при пуше в любую ветку запускаются тесты
- при мёрдже PR в ветки `develop` или `release/` проект запускается на удалённом сервере
- при мёрдже PR в ветку `main` проект запускается на удалённом сервере

Для корректной работы CI/CD необходимо создать секретные переменные репозитория
(Repository secrets):
```text
DOCKER_USERNAME=<docker_username>
DOCKER_PASSWORD=<docker_password>

SERVER_HOST=<server_pub_ip>
SERVER_USER=<username>

SSH_KEY=<--BEGIN OPENSSH PRIVATE KEY--...--END OPENSSH PRIVATE KEY--> # cat ~/.ssh/id_rsa
SSH_PASSPHRASE=<ssh key passphrase>
```

##  Frontend <a id="frontend"></a>

[Ссылка на репозиторий](https://github.com/yandex-funtech-it-events/frontend)


[Оглавление](#contents)
