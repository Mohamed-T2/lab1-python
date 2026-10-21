# analysis.py
def validate_todos(data):
    if not isinstance(data, list):
        raise ValueError("Корень должен быть списком")
    seen = set()
    for i, item in enumerate(data):
        if not isinstance(item, dict):
            raise ValueError(f"Запись {i} должна быть словарём")
        for key in ("id", "userId"):
            if key not in item:
                raise ValueError(f"Запись {i}: нет поля {key}")
            if type(item[key]) is not int or item[key] <= 0:
                raise ValueError(f"Запись {i}: {key} должен быть положительным целым")
        title = item.get("title")
        if not isinstance(title, str) or not title.strip():
            raise ValueError(f"Запись {i}: title должен быть непустой строкой")
        if type(item.get("completed")) is not bool:
            raise ValueError(f"Запись {i}: completed должен быть логическим")
        if item["id"] in seen:
            raise ValueError(f"Запись {i}: повторный id {item['id']}")
        seen.add(item["id"])


def completion_counts(todos):
    counts = {}
    for t in todos:
        counts.setdefault(t["userId"], 0)
        if t["completed"]:
            counts[t["userId"]] += 1
    return counts


def top_users(counts):
    if not counts:
        return []
    best = max(counts.values())
    if best == 0:
        return []
    return sorted(u for u, c in counts.items() if c == best)


def select_tasks(todos, user_id, parameter=None):
    # Variante 9 : titre commence par la sous-chaîne
    if parameter is None or not parameter.strip():
        raise ValueError("Нужна непустая строка")
    prefix = parameter.strip().lower()
    return [
        dict(t) for t in todos
        if t["userId"] == user_id and t["title"].lower().startswith(prefix)
    ]
