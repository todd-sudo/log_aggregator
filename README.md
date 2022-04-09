# Агрегатор лог-файлов Apache

Тестовое задание - Агрегатор Логов Apache

[![Built with Cookiecutter Django](https://img.shields.io/badge/built%20with-Cookiecutter%20Django-ff69b4.svg?logo=cookiecutter)](https://github.com/cookiecutter/cookiecutter-django/)
[![Black code style](https://img.shields.io/badge/code%20style-black-000000.svg)](https://github.com/ambv/black)

License: MIT


## Описание

#### Административная панель - http://127.0.0.1:8000/admin/
#### API Документация - http://127.0.0.1:8000/api/docs/
#### Стек:
- Django/Django Rest Framework
- Celery
- Redis
- Docker/Docker-compose
- apachelogs
- Swagger UI

## Настройки

#### В файле настроек `config/settings/base.py` прописать путь до файла с логами
    
```python
PATH_APACHE_LOGS = "access_log.log"
```
#### В корне проекта, есть пример файла с логами


## Запуск

#### 1. Build project:
    
```bash
./scripts/build_local.sh
```

#### 2. Migrate:

```bash
./scripts/migrate_local.sh
```

#### 3. Create superuser:

```bash
./scripts/manage_local.sh createsuperuser
```

#### 4. Up project:

```bash
./scripts/up_local.sh
```

#### 5. Запуск парсинга файла с логами

- Перейти в административную панель/периодичные таски `http://127.0.0.1:8000/admin/django_celery_beat/periodictask/`
- Выбрать таску для парсинга файла
- Выставить ей поле `Enabled` в `True`(нажать на check box):
    - так же можно настроить периодичность выполнения задачи парсинга файла с логами 

Далее раз в день будет парситься файл с логами, распаршенные данные будут добавляться в базу данных.