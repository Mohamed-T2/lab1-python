# main.py
import json
from pathlib import Path

from analysis import (
    validate_todos, completion_counts, top_users, select_tasks,
)

BASE = Path(_file_).resolve().parent


def ask_user_id():
    while True:
        text = input("user_id (положительное целое): ").strip()
        try:
            value = int(text)
        except ValueError:
            print("Введите целое число")
            continue
        if value <= 0:
            print("Число должно быть положительным")
            continue
        return value


def ask_prefix():
    while True:
        text = input("Начало названия: ").strip()
        if text:
            return text
        print("Строка не должна быть пустой")


def save_json(name, data):
    with open(BASE / name, "w", encoding="utf-8") as file:
        json.dump(data, file, ensure_ascii=False, indent=2)


def main():
    try:
        with open(BASE / "todos.json", "r", encoding="utf-8") as file:
            todos = json.load(file)
        validate_todos(todos)

        counts = completion_counts(todos)
        leaders = top_users(counts)
        leader_tasks = [
            t for t in todos
            if t["completed"] and t["userId"] in leaders
        ]

        print("Количество выполненных:", counts)
        print("Лидеры:", ", ".join(str(u) for u in leaders) or "нет")

        user_id = ask_user_id()
        prefix = ask_prefix()
        selected = select_tasks(todos, user_id, prefix)

        save_json("leaders.json", leader_tasks)
        save_json("selected.json", selected)
        print("Результаты сохранены")
    except FileNotFoundError:
        print("Файл todos.json не найден")
    except UnicodeDecodeError:
        print("Неправильная кодировка файла")
    except json.JSONDecodeError as error:
        print(f"Неправильный JSON: {error}")
    except ValueError as error:
        print(f"Ошибка структуры данных: {error}")
    except OSError as error:
        print(f"Ошибка доступа к файлу: {error}")


if _name_ == "_main_":
    main()
