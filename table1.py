def row_sums(matrix):
    """Вычисляет суммы элементов каждой строки."""
    return [sum(row) for row in matrix]


def column_sums(matrix):
    """Вычисляет суммы элементов каждого столбца."""
    if not matrix:
        return []

    columns = len(matrix[0])

    return [
        sum(row[column] for row in matrix)
        for column in range(columns)
    ]
