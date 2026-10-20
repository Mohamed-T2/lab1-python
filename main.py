from table import row_sums, column_sums, diagonal_pattern, transform


def read_matrix():
    rows = int(input("Количество строк: "))
    columns = int(input("Количество столбцов: "))

    while rows <= 0 or columns <= 0:
        print("Размеры должны быть положительными.")
        rows = int(input("Количество строк: "))
        columns = int(input("Количество столбцов: "))

    matrix = []

    for i in range(rows):
        while True:
            row = [
                int(part)
                for part in input(
                    f"Введите строку {i + 1}: "
                ).split()
            ]

            if len(row) == columns:
                matrix.append(row)
                break

            print(f"Нужно ровно {columns} чисел.")

    return matrix


def print_matrix(matrix):
    for row in matrix:
        print(*row)


def main():
    matrix = read_matrix()

    print("\nИсходная матрица:")
    print_matrix(matrix)

    print("\nСуммы строк:", row_sums(matrix))
    print("Суммы столбцов:", column_sums(matrix))

    new_matrix = transform(matrix)

    print("\nПреобразованная матрица (вариант 9):")
    print_matrix(new_matrix)

    size = int(input("\nВведите положительный размер узора: "))

    while size <= 0:
        print("Размер должен быть положительным.")
        size = int(input("Введите положительный размер узора: "))

    print("\nДиагональный узор:")
    print_matrix(diagonal_pattern(size))


if __name__ == "__main__":
    main()
