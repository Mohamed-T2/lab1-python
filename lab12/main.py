# main.py
"""Консольное меню: план задач по программированию (вариант 9)."""
from pathlib import Path

from logic import (
    add_record, find_records, set_completed, delete_record, statistics,
)
from storage import load_records, save_records

DATA_PATH = Path(_file_).resolve().parent / "data.json"
UNIT = "баллов"

MENU = """
1. Показать записи
2. Добавить запись
3. Найти записи
4. Изменить статус
5. Удалить запись
6. Показать статистику
7. Сохранить данные
8. Выйти"""


def ask_text(prompt):
    while True:
        text = input(prompt).strip()
        if text:
            return text
        print("Строка не должна быть пустой")


def ask_int(prompt, minimum):
    while True:
        text = input(prompt).strip()
        try:
            value = int(text)
        except ValueError:
            print("Введите целое число")
            continue
        if value < minimum:
            print(f"Число должно быть не меньше {minimum}")
            continue
        return value


def status_text(record):
    return "решена" if record["completed"] else "не решена"


def print_record(record):
    print(
        f"ID {record['id']} | {record['title']} | {record['category']} | "
        f"{record['amount']} {UNIT} | {status_text(record)}"
    )


def show_records(records):
    if not records:
        print("Нет записей")
        return
    for record in sorted(records, key=lambda r: r["id"]):
        print_record(record)


def add_menu(records):
    title = ask_text("Название: ")
    category = ask_text("Категория: ")
    amount = ask_int("Количество баллов: ", 0)
    record = add_record(records, title, category, amount)
    print(f"Запись добавлена, ID {record['id']}")


def find_menu(records):
    query = ask_text("Что искать в названии: ")
    found = find_records(records, query)
    if not found:
        print("Ничего не найдено")
        return
    for record in found:
        print_record(record)


def status_menu(records):
    record_id = ask_int("ID записи: ", 1)
    while True:
        answer = input("1 — решена, 2 — не решена: ").strip()
        if answer == "1":
            completed = True
            break
        if answer == "2":
            completed = False
            break
        print("Введите 1 или 2")
    if set_completed(records, record_id, completed):
        print("Статус изменён")
    else:
        print("Запись с таким ID не найдена")


def delete_menu(records):
    record_id = ask_int("ID записи: ", 1)
    if not any(r["id"] == record_id for r in records):
        print("Запись с таким ID не найдена")
        return
    answer = input("Удалить? Введите да для подтверждения: ").strip().lower()
    if answer == "да":
        delete_record(records, record_id)
        print("Запись удалена")
    else:
        print("Удаление отменено")


def stats_menu(records):
    stats = statistics(records)
    print(f"Всего записей: {stats['total']}")
    print(f"Решено: {stats['done']}")
    print(f"Не решено: {stats['not_done']}")
    print(f"Сумма: {stats['total_amount']} {UNIT}")
    for category, total in stats["by_category"].items():
        print(f"  {category}: {total} {UNIT}")


def save_menu(records):
    """Возвращает True, только если сохранение удалось."""
    try:
        save_records(DATA_PATH, records)
    except (OSError, ValueError) as error:
        print(f"Ошибка сохранения: {error}")
        return False
    print("Данные сохранены")
    return True


def exit_menu(records):
    """Возвращает True, если можно завершать программу."""
    while True:
        answer = input("Сохранить данные перед выходом? (да/нет): ").strip().lower()
        if answer == "да":
            return save_menu(records)
        if answer == "нет":
            return True
        print("Ответьте да или нет")


def load_start():
    """Возвращает список записей или None, если запуск нужно прекратить."""
    try:
        return load_records(DATA_PATH)
    except FileNotFoundError:
        print("Файл data.json не найден, начинаем с пустого списка")
        return []
    except ValueError as error:
        print(f"Файл data.json повреждён или имеет неправильную структуру: {error}")
        return None
    except OSError as error:
        print(f"Ошибка доступа к файлу: {error}")
        return None


def main():
    records = load_start()
    if records is None:
        print("Запуск прекращён, файл не изменён")
        return
    actions = {
        "1": show_records,
        "2": add_menu,
        "3": find_menu,
        "4": status_menu,
        "5": delete_menu,
        "6": stats_menu,
        "7": save_menu,
    }
    while True:
        print(MENU)
        command = input("Команда: ").strip()
        if command == "8":
            if exit_menu(records):
                break
        elif command in actions:
            actions[command](records)
        else:
            print("Неизвестная команда")


if _name_ == "_main_":
    main()
