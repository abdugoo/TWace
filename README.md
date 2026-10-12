# TWace
«TWace: Track your applications. Work on your skills. Ace your interviews.» 

# TWace Backend

Backend приложения для отслеживания откликов на вакансии.

## Текущее состояние

Приложение находится в разработке.
Реализована проверка работоспособности GET /health.

## Подготовка

Активируйте виртуальное окружение.
Все команды ниже выполняются из папки backend.

Установите зависимости:

```bash
python -m pip install -r requirements.txt
```

## Запуск

```bash
python -m uvicorn app.main:app --reload
```

Документация API: http://127.0.0.1:8000/docs

## Тесты

```bash
python -m pytest
```

Тест /health проверяет код ответа 200 и JSON {"status": "ok"}.

## Ближайшие задачи

- Подключить PostgreSQL.
- Настроить миграции Alembic.
- Реализовать регистрацию и вход.