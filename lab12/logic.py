# logic.py
"""Логика проекта: проверка, добавление, поиск, статус, удаление, статистика."""


def validate_records(records):
    """Проверяет весь список. Ничего не меняет.
    При нарушении выбрасывает ValueError с пояснением."""
    if not isinstance(records, list):
        raise ValueError("Корень должен быть списком")
    seen = set()
    for i, item in enumerate(records):
        if not isinstance(item, dict):
            raise ValueError(f"Запись {i} должна быть словарём")
        for key in ("id", "title", "category", "amount", "completed"):
            if key not in item:
                raise ValueError(f"Запись {i}: нет поля {key}")
        if type(item["id"]) is not int or item["id"] <= 0:
            raise ValueError(f"Запись {i}: id должен быть положительным целым")
        if item["id"] in seen:
            raise ValueError(f"Запись {i}: повторный id {item['id']}")
        seen.add(item["id"])
        for key in ("title", "category"):
            if not isinstance(item[key], str) or not item[key].strip():
                raise ValueError(f"Запись {i}: {key} должен быть непустой строкой")
        if type(item["amount"]) is not int or item["amount"] < 0:
            raise ValueError(f"Запись {i}: amount должен быть целым не меньше 0")
        if type(item["completed"]) is not bool:
            raise ValueError(f"Запись {i}: completed должен быть bool")


def add_record(records, title, category, amount):
    """Добавляет запись в конец списка (список ИЗМЕНЯЕТСЯ).
    Возвращает новую запись. При неверных данных — ValueError."""
    if not isinstance(title, str) or not title.strip():
        raise ValueError("Название не должно быть пустым")
    if not isinstance(category, str) or not category.strip():
        raise ValueError("Категория не должна быть пустой")
    if type(amount) is not int or amount < 0:
        raise ValueError("Количество должно быть целым не меньше 0")
    new_id = max((r["id"] for r in records), default=0) + 1
    record = {
        "id": new_id,
        "title": title.strip(),
        "category": category.strip(),
        "amount": amount,
        "completed": False,
    }
    records.append(record)
    return record


def find_records(records, query):
    """Ищет по подстроке названия без учёта регистра.
    Список НЕ меняется. Возвращает новый список (по возрастанию id).
    Пустой запрос — ValueError."""
    if not isinstance(query, str) or not query.strip():
        raise ValueError("Поисковый запрос не должен быть пустым")
    q = query.strip().lower()
    found = [r for r in records if q in r["title"].lower()]
    return sorted(found, key=lambda r: r["id"])


def set_completed(records, record_id, completed):
    """Явно ставит статус (список ИЗМЕНЯЕТСЯ).
    True — запись найдена; False — неизвестный id, данные не изменены."""
    for r in records:
        if r["id"] == record_id:
            r["completed"] = completed
            return True
    return False


def delete_record(records, record_id):
    """Удаляет запись по id (список ИЗМЕНЯЕТСЯ), id остальных не меняются.
    True — удалено; False — неизвестный id."""
    for i, r in enumerate(records):
        if r["id"] == record_id:
            del records[i]
            return True
    return False


def statistics(records):
    """Считает статистику. Список НЕ меняется.
    Возвращает словарь: total, done, not_done, total_amount,
    by_category (категории по алфавиту)."""
    done = sum(1 for r in records if r["completed"])
    by_category = {}
    for r in records:
        key = r["category"].strip()
        by_category[key] = by_category.get(key, 0) + r["amount"]
    return {
        "total": len(records),
        "done": done,
        "not_done": len(records) - done,
        "total_amount": sum(r["amount"] for r in records),
        "by_category": dict(sorted(by_category.items())),
    }
