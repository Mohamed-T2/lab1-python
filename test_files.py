from pathlib import Path
from tempfile import TemporaryDirectory

from files_lab import read_matrix


def check_value_error(path, message):
    try:
        read_matrix(path)
    except ValueError:
        pass
    else:
        assert False, message


def main():
    with TemporaryDirectory() as directory:
        folder = Path(directory)
        path = folder / "matrix.txt"

        # Проверка обычной матрицы
        path.write_text("1 2\n7 -1\n", encoding="utf-8")
        assert read_matrix(path) == [[7, -1]]

        # Проверка матрицы с нулём
        path.write_text("1 1\n0\n", encoding="utf-8")
        assert read_matrix(path) == [[0]]

        # Проверка пустого файла
        path.write_text("", encoding="utf-8")
        check_value_error(path, "Пустой файл не обнаружен")

        # Проверка нулевого размера
        path.write_text("0 3\n", encoding="utf-8")
        check_value_error(path, "Нулевой размер не обнаружен")

        # Проверка неправильного количества чисел
        path.write_text("1 2\n1\n", encoding="utf-8")
        check_value_error(path, "Ошибка количества чисел не обнаружена")

        # Проверка нечисловой ячейки
        path.write_text("1 2\n1 x\n", encoding="utf-8")
        check_value_error(path, "Нечисловая ячейка не обнаружена")

        # Проверка лишней строки
        path.write_text("1 1\n5\n6\n", encoding="utf-8")
        check_value_error(path, "Лишняя строка не обнаружена")

        # Проверка отсутствующего файла
        missing = folder / "missing.txt"
        try:
            read_matrix(missing)
        except FileNotFoundError:
            pass
        else:
            assert False, "Отсутствующий файл не обнаружен"

    print("Все тесты успешно пройдены!")


if _name_ == "_main_":
    main()
