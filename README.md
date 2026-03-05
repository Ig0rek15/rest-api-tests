# API Tests for JSONPlaceholder

Набор автоматизированных тестов REST API, написанных на Python с использованием pytest и requests.

### Тестируется эндпоинт:

```bash
/posts
```

публичного API JSONPlaceholder.

Проверяются основные операции:

GET — получение поста и списка постов

POST — создание поста

PUT — обновление поста

DELETE — удаление поста

---

## Установка зависимостей
```bash
pip install -r requirements.txt
```

## Запуск тестов
```bash
pytest tests/ -v
```
