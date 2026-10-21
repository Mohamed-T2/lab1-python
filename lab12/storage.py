# storage.py
"""Чтение и запись JSON. Без консольных диалогов."""
import json
import os

from logic import validate_records


def load_records(path):
    """Читает и проверяет файл (UTF-8). Файл НЕ изменяется.
    Возвращает список записей.
    Ошибки: FileNotFoundError — файла нет;
    ValueError (в том числе JSONDecodeError и UnicodeDecodeError) —
    повреждённый файл, неправильная кодировка или структура;
    OSError — ошибка доступа."""
    with open(path, "r", encoding="utf-8") as file:
        records = json.load(file)
    validate_records(records)
    return records


def save_records(path, records):
    """Записывает список в JSON (UTF-8).
    Пишет во временный файл и заменяет им старый, поэтому при
    ошибке прежний файл остаётся целым.
    При успехе возвращает None; при ошибке выбрасывает исключение
    (OSError или ValueError), сообщать об успехе нужно только после
    нормального возврата."""
    validate_records(records)
    temp_path = str(path) + ".tmp"
    try:
        with open(temp_path, "w", encoding="utf-8") as file:
            json.dump(records, file, ensure_ascii=False, indent=2)
        os.replace(temp_path, path)
    except OSError:
        try:
            os.remove(temp_path)
        except OSError:
            pass
        raise
