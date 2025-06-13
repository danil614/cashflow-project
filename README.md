# Cash Flow Tracker

Веб-приложение для учёта движения денежных средств.  
Backend — Python 3.12 + Django 5.2 (SQLite), Frontend — Django-admin и собственные шаблоны (Bootstrap).

---

## Быстрый старт

```bash
# 1. Клон репозитория
git clone https://github.com/danil614/cashflow-project.git
cd cashflow-project

# 2. Виртуальное окружение
python -m venv venv
source venv/bin/activate        # Windows: venv\Scripts\activate

# 3. Зависимости
pip install -r requirements.txt

# 4. Миграции
python manage.py migrate

# 5. (Опц.) демо-данные
python manage.py loaddata demo

# 6. Суперпользователь
python manage.py createsuperuser

# 7. Запуск
python manage.py runserver
```

## HTML-интерфейс

| Путь             | Метод(ы)  | Назначение                    |
|------------------|-----------|-------------------------------|
| `/`              | GET       | Таблица записей ДДС + фильтры |
| `/new/`          | GET, POST | Создание записи               |
| `/<id>/edit/`    | GET, POST | Редактирование записи         |
| `/<id>/delete/`  | POST      | Удаление записи               |
| `/dictionaries/` | GET, POST | Список справочников           |
| `/admin/`        | GET       | Django-admin                  |

## REST API

| Путь                  | Метод(ы)         | Описание                                   |
|-----------------------|------------------|--------------------------------------------|
| `/api/statuses/`      | GET, POST        | Справочник статусов                        |
| `/api/types/`         | GET, POST        | Справочник типов                           |
| `/api/categories/`    | GET, POST        | Категории; фильтр `?type=<id>`             |
| `/api/subcategories/` | GET, POST        | Подкатегории; фильтр `?category=<id>`      |
| `/api/records/`       | GET, POST        | Список записей / создание                  |
| `/api/records/<id>/`  | GET, PUT, DELETE | Детализировать / обновить / удалить запись |

## Скриншоты

![screen (1).png](docs/screen%20%281%29.png)
![screen (2).png](docs/screen%20%282%29.png)
![screen (3).png](docs/screen%20%283%29.png)
![screen (4).png](docs/screen%20%284%29.png)
![screen (5).png](docs/screen%20%285%29.png)