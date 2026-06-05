# Makefile для pip + Django + Ruff

PYTHON=python3
PIP=$(PYTHON) -m pip
VENV=.venv
VENV_PYTHON=$(VENV)/bin/python
VENV_PIP=$(VENV_PYTHON) -m pip

# Создание виртуального окружения
venv:
	$(PYTHON) -m venv $(VENV)

# Установка всех зависимостей проекта
deps: venv
	$(VENV_PIP) install --upgrade pip
	$(VENV_PIP) install -r requirements.txt

# Запуск Django сервера
run:
	$(VENV_PYTHON) manage.py runserver

# Линтинг проекта
lint:
	$(VENV_PYTHON) -m ruff check .

# Авто-форматирование кода
format:
	$(VENV_PYTHON) -m ruff format .

# Полный workflow для разработки
dev: deps lint run

