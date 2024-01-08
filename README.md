# YaCut
[![Python](https://img.shields.io/badge/-Python-464646?style=flat&logo=Python&logoColor=ffffff&color=bc8429)](https://www.python.org/)
[![Flask](https://img.shields.io/badge/-Flask-464646?style=flat&logo=Flask&logoColor=ffffff&color=1d31c9)](https://www.djangoproject.com/)
[![REST](https://img.shields.io/badge/-REST-464646?style=flat&logo=REST&logoColor=ffffff&color=bc2929)](https://www.django-rest-framework.org/)
[![SQLAlchemy](https://img.shields.io/badge/-SQLAlchemy-464646?style=flat&logo=SQLAlchemy&logoColor=ffffff&color=043A6B)](https://www.postgresql.org/)
[![Code style: black](https://img.shields.io/badge/code%20style-black-000000.svg)](https://github.com/psf/black)
[![Jinja2](https://img.shields.io/badge/-Jinja2-464646?style=flat&logo=Jinja&logoColor=ffffff&color=ddcc08)](https://www.postgresql.org/)

Платформа для сокращения URL с возможностью использования как через веб-интерфейс, так и через REST API. Этот инструмент предназначен для сопоставления длинной URL, заданной пользователем, с более короткой версией, которую может выбрать сам пользователь или которую сгенерирует система.

## Основные функции платформы
- Создание сокращенных URL-адресов, соединенных с их полными версиями
- Перенаправление пользователей на первоначальный URL при переходе по сокращенной ссылке
- /api/id/ — отправка POST-запроса для регистрации нового сокращенного URL
- /api/id/<short_id>/ — отправка GET-запроса для извлечения полной версии URL по его сокращенному идентификатору
- Предоставляется функционал для работы как через графический веб-интерфейс, так и через программный API.

## Технологии
- Python 3.10
- Flask 2.0
- Jinja2 3.0
- SQLAlchemy 1.4

## Использование
Клонировать репозиторий и перейти в него в командной строке:

```
git clone git@github.com:Ozxar69/yacut.git
cd yacut
```

Cоздать и активировать виртуальное окружение:

```
python -m venv venv
```

* Если у вас Linux/macOS

    ```
    source venv/bin/activate
    ```

* Если у вас windows

    ```
    . venv/scripts/activate
    ```

Установить зависимости из файла requirements.txt:

```
python -m pip install --upgrade pip
pip install -r requirements.txt
```

## Env
На основе файла envexample создайте файл .env и заполните его

## Миграции
Создать и выполнить миграции:

```commandline
flask db init
```
```commandline
flask db migrate
```
```commandline
flask db upgrade
```

Запуск проекта:

```commandline
flask run
```

Автор: [Ozxar69](https://github.com/Ozxar69)