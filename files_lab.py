def read_matrix(path):
    """Читает матрицу из файла и проверяет формат данных."""
    with open(path, "r", encoding="utf-8") as file:
        content = file.read()

    lines = content.splitlines()

    if not lines:
        raise ValueError("Строка 1: пустой файл")

    header = lines[0].split()

    if len(header) != 2:
        raise ValueError("Строка 1: ожидалось 2 числа")

    try:
        rows, cols = map(int, header)
    except ValueError:
        raise ValueError("Строка 1: размеры должны быть целыми числами")

    if rows <= 0 or cols <= 0:
        raise ValueError("Строка 1: размеры должны быть больше нуля")

    if len(lines) != rows + 1:
        raise ValueError(
            f"Ожидалось {rows} строк данных, получено {len(lines) - 1}"
        )

    matrix = []

    for line_number, line in enumerate(lines[1:], start=2):
        values = line.split()

        if len(values) != cols:
            raise ValueError(
                f"Строка {line_number}: ожидалось {cols} чисел"
            )

        try:
            row = [int(value) for value in values]
        except ValueError:
            raise ValueError(
                f"Строка {line_number}: обнаружено нецелое число"
            )

        matrix.append(row)

    return matrix
