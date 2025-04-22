# Delivery Service

Сервис доставки посылок с использованием FastAPI, PostgreSQL, Redis и RabbitMQ.

## Структура проекта

```
delivery_service/
├── alembic/                  # Миграции базы данных
├── redis/                    # Конфигурация Redis
├── src/                      # Исходный код
│   ├── app/                  # Основное приложение
│   │   ├── api/              # API эндпоинты
│   │   ├── core/             # Ядро приложения
│   │   │   ├── config/       # Конфигурация
│   │   │   ├── database.py   # Настройки БД
│   │   │   ├── paths.py      # Пути проекта
│   │   │   └── worker.py     # Воркер для фоновых задач
│   │   ├── external/         # Внешние сервисы
│   │   ├── models/           # SQLAlchemy модели
│   │   ├── repository/       # Репозитории для работы с БД
│   │   ├── schemas/          # Pydantic схемы
│   │   ├── services/         # Бизнес-логика
│   │   ├── utils/            # Вспомогательные функции
│   │   ├── asgi.py           # ASGI приложение
│   │   └── main.py           # Точка входа
│   └── initial_seed.py       # Скрипт инициализации данных
├── tests/                    # Тесты
├── .env                      # Переменные окружения
├── .env.example              # Пример .env файла
├── .pre-commit-config.yaml   # Настройки pre-commit
├── .python-version           # Версия Python
├── Dockerfile                # Docker конфигурация
├── alembic.ini               # Конфигурация Alembic
├── docker-compose.yml        # Docker Compose конфигурация
├── pyproject.toml            # Зависимости проекта
└── README.md                 # Документация
```

## Основные компоненты

### Модели данных
- `Parcel` - модель посылки
- `ParcelType` - типы посылок
- `User` - модель пользователя

### API
- CRUD операции для посылок
- Управление типами посылок
- Расчет стоимости доставки

### Сервисы
- Расчет стоимости доставки
- Обновление курса валют
- Обработка фоновых задач

### Инфраструктура
- PostgreSQL для хранения данных
- Redis для кэширования и очередей
- RabbitMQ для асинхронных задач

## Запуск проекта

1. Скопируйте `.env.example` в `.env` и настройте переменные окружения
2. Запустите сервисы:
```bash
docker-compose up -d
```

## Миграции базы данных

```bash
docker-compose run --rm migrator
```

## Тесты

```bash
docker-compose run --rm api pytest
```

## Лицензия

MIT
