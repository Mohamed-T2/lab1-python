import unittest

from table import (
    row_sums,
    column_sums,
    diagonal_pattern,
    transform,
)


class TestTable(unittest.TestCase):

    def test_row_and_column_sums(self):
        matrix = [[1, 2, 3], [4, 5, 6]]

        self.assertEqual(row_sums(matrix), [6, 15])
        self.assertEqual(column_sums(matrix), [5, 7, 9])

    def test_single_element(self):
        self.assertEqual(row_sums([[7]]), [7])
        self.assertEqual(column_sums([[7]]), [7])
        self.assertEqual(diagonal_pattern(1), [[0]])

    def test_single_column(self):
        matrix = [[1], [-1], [0]]

        self.assertEqual(row_sums(matrix), [1, -1, 0])
        self.assertEqual(column_sums(matrix), [0])

    def test_empty_matrix(self):
        self.assertEqual(row_sums([]), [])
        self.assertEqual(column_sums([]), [])
        self.assertEqual(transform([]), [])

    def test_diagonal_pattern(self):
        expected = [
            [0, 1, 1],
            [2, 0, 1],
            [2, 2, 0],
        ]

        self.assertEqual(diagonal_pattern(3), expected)

    def test_transform_variant_9(self):
        matrix = [[-2, 0, 3], [4, -5, 6]]
        expected = [[-2, 3, 3], [4, -5, 3]]

        self.assertEqual(transform(matrix), expected)

    def test_other_variants_examples(self):
        matrix = [[-2, 0, 3], [4, -5, 6]]

        self.assertEqual(
            [[0 if value < 0 else value for value in row]
             for row in matrix],
            [[0, 0, 3], [4, -5, 6]],
        )

        self.assertEqual(
            [[1 if value > 0 else value for value in row]
             for row in matrix],
            [[-2, 0, 1], [1, -5, 1]],
        )

        self.assertEqual(
            [[value * 2 if value % 2 == 0 else value
              for value in row] for row in matrix],
            [[-4, 0, 3], [8, -5, 6]],
        )

    def test_transform_does_not_change_original(self):
        matrix = [[-2, 0, 3], [4, -5, 6]]
        original = [row.copy() for row in matrix]

        result = transform(matrix)
        result[0][0] = 100

        self.assertEqual(matrix, original)

    def test_transform_returns_independent_rows(self):
        matrix = [[-2, 0, 3], [4, -5, 6]]
        result = transform(matrix)

        result[0][0] = 100

        self.assertEqual(matrix[0][0], -2)


if _name_ == "_main_":
    unittest.main()
