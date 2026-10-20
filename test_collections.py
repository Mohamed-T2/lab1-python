import unittest

from collections_lab import (
    word_counts,
    common_topics,
    all_topics,
    totals_by_category,
    titles_in_category,
    sorted_category_totals,
)


class TestCollectionsLab(unittest.TestCase):

    def test_word_counts(self):
        self.assertEqual(
            word_counts("Python, python! SQL"),
            {"python": 2, "sql": 1},
        )

    def test_empty_text(self):
        self.assertEqual(word_counts("!!!"), {})

    def test_common_topics(self):
        self.assertEqual(
            common_topics(
                ["python", "sql", "python"],
                ["sql", "git"],
            ),
            ["sql"],
        )

    def test_all_topics(self):
        self.assertEqual(
            all_topics(
                ["python", "sql", "python"],
                ["sql", "git"],
            ),
            ["git", "python", "sql"],
        )

    def test_empty_topics(self):
        self.assertEqual(common_topics([], ["python"]), [])
        self.assertEqual(all_topics([], ["python"]), ["python"])

    def test_totals_by_category(self):
        records = [
            {"title": "A", "category": "основное", "amount": 4},
            {"title": "B", "category": "дополнительное", "amount": 2},
            {"title": "C", "category": "основное", "amount": 3},
        ]

        self.assertEqual(
            totals_by_category(records),
            {"основное": 7, "дополнительное": 2},
        )

    def test_titles_in_category(self):
        records = [
            {"title": "A", "category": "основное", "amount": 4},
            {"title": "B", "category": "дополнительное", "amount": 2},
            {"title": "C", "category": "основное", "amount": 3},
        ]

        self.assertEqual(
            titles_in_category(records, "основное"),
            ["A", "C"],
        )
        self.assertEqual(titles_in_category(records, "нет"), [])

    def test_empty_records(self):
        self.assertEqual(totals_by_category([]), {})
        self.assertEqual(titles_in_category([], "основное"), [])

    def test_records_not_modified(self):
        records = [
            {"title": "A", "category": "основное", "amount": 4},
            {"title": "B", "category": "дополнительное", "amount": 2},
        ]
        original = [record.copy() for record in records]

        totals_by_category(records)
        titles_in_category(records, "основное")

        self.assertEqual(records, original)

    def test_sorted_category_totals(self):
        records = [
            {"title": "A", "category": "основное", "amount": 4},
            {"title": "B", "category": "дополнительное", "amount": 4},
            {"title": "C", "category": "тестирование", "amount": 2},
        ]

        self.assertEqual(
            sorted_category_totals(records),
            [
                ("дополнительное", 4),
                ("основное", 4),
                ("тестирование", 2),
            ],
        )


if _name_ == "_main_":
    unittest.main()
