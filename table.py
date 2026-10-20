def row_sums(matrix):
    """Return the sum of each row."""
    return [sum(row) for row in matrix]


def column_sums(matrix):
    """Return the sum of each column."""
    if not matrix:
        return []

    columns = len(matrix[0])
    return [
        sum(matrix[row][column] for row in range(len(matrix)))
        for column in range(columns)
    ]


def diagonal_pattern(size):
    """Create a square matrix with a diagonal pattern."""
    matrix = []

    for row in range(size):
        current_row = []

        for column in range(size):
            if row == column:
                current_row.append(0)
            elif row < column:
                current_row.append(1)
            else:
                current_row.append(2)

        matrix.append(current_row)

    return matrix


def transform(matrix):
    """Replace multiples of 3 with 3 (variant 9)."""
    return [
        [3 if value % 3 == 0 else value for value in row]
        for row in matrix
    ]
