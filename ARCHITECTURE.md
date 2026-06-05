# Архитектура проекта `backend`
## 1) Назначение
Проект — Django/DRF backend для landing-сервиса с административной панелью, API-префиксом `api/landing/` и auto-документацией Swagger/ReDoc.

## 2) Технологический стек
- Python 3.11+
- Django 4.2
- Django REST Framework
- drf-yasg (Swagger/ReDoc)
- django-jazzmin (тема админки)
- django-cors-headers
- django-modeltranslation
- WhiteNoise
- PostgreSQL (production-конфигурация) / SQLite (development-конфигурация)

## 3) Структура модулей
```text
.
├── manage.py
├── core/
│   ├── asgi.py
│   ├── wsgi.py
│   ├── urls.py
│   ├── yasg.py
│   └── settings/
│       ├── base.py
│       ├── development.py
│       ├── production.py
│       └── jazzmin.py
├── requirements.txt
├── Makefile
└── .env
```

## 4) Точки входа и жизненный цикл
- `manage.py`:
  - загружает переменные из `.env`;
  - выставляет `DJANGO_SETTINGS_MODULE=core.settings.base`;
  - запускает команды Django.
- `core/wsgi.py` и `core/asgi.py`:
  - точки входа для WSGI/ASGI-хостинга;
  - используют тот же модуль настроек `core.settings.base`.

## 5) Конфигурация окружений
Логика выбора окружения находится в `core/settings/base.py`:
- если `PRODUCTION` задан как непустое значение → импортируются настройки из `production.py`;
- если `PRODUCTION` пустой/не задан → импортируются настройки из `development.py`.

### Development (`core/settings/development.py`)
- `DEBUG=True`
- База данных: SQLite (`db.sqlite3`)
- `CORS_ALLOW_ALL_ORIGINS=True`

### Production (`core/settings/production.py`)
- База данных: PostgreSQL (через `POSTGRES_*` переменные)
- security-настройки (`SESSION_COOKIE_SECURE`, HSTS, CSRF secure и т.д.)
- `STATICFILES_STORAGE = whitenoise.storage.CompressedStaticFilesStorage`

## 6) URL-архитектура
Корневой URL (`core/urls.py`) монтирует всё под префиксом:
- `api/landing/`

Внутри этого префикса:
- `admin/` → Django admin
- `v1/` → бизнес-API (`include("apps.settings.urls")`)
- `swagger/`, `redoc/`, `swagger.json|yaml` → документация из `core/yasg.py`
- `back_media/...` и static-раздача для медиа/статики

## 7) Поток HTTP-запроса
1. Клиент отправляет запрос на `api/landing/...`
2. Запрос проходит middleware-цепочку (`CORS`, `WhiteNoise`, security/session/locale и др.)
3. `ROOT_URLCONF` (`core.urls`) маршрутизирует запрос:
   - в admin,
   - в API-приложение `apps.settings`,
   - или в swagger/redoc.
4. View вызывает ORM/сервисы, работает с БД
5. Django формирует ответ и возвращает его через middleware обратно клиенту

## 8) Слои системы
- **Transport/Web layer**: Django URL routing + middleware
- **API layer**: DRF endpoints (ожидаются в `apps.settings`)
- **Data layer**: Django ORM + PostgreSQL/SQLite
- **Ops layer**: `.env`-конфигурация, `Makefile`, WSGI/ASGI entrypoints

## 9) Конфигурация и секреты
Используются переменные окружения из `.env`:
- общие: `SECRET_KEY`, `PRODUCTION`, `DEBUG`, `ALLOWED_HOSTS`
- PostgreSQL: `POSTGRES_DB`, `POSTGRES_USER`, `POSTGRES_PASSWORD`, `POSTGRES_HOST`, `POSTGRES_PORT`
- CORS/CSRF: `CORS_ALLOWED_ORIGINS`, `CSRF_TRUSTED_ORIGINS`

Рекомендация: не хранить рабочие секреты в репозитории, использовать секрет-хранилище на окружениях деплоя.

## 10) Сборка и запуск
- Установка зависимостей: `make deps`
- Локальный запуск: `make run`
- Линтинг: `make lint`
- Форматирование: `make format`

Проект использует `pip` + `requirements.txt`; `pyproject.toml` применяется для конфигурации `ruff`.

## 11) Текущее архитектурное ограничение
В `core/urls.py` подключается модуль `apps.settings.urls`, но директория `apps/` в текущем состоянии репозитория отсутствует.

Следствие:
- команды с полной проверкой URL-конфига (например, `manage.py check`) падают до восстановления `apps.settings`.
- миграции/запуск можно выполнять с `--skip-checks`, но это обход, а не окончательное решение.

## 12) Что восстановить в первую очередь
Минимум для целостной архитектуры:
- `apps/settings/__init__.py`
- `apps/settings/urls.py`
- далее: `views.py`, `serializers.py`, `models.py` по бизнес-требованиям API.
