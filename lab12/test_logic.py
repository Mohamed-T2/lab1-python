# test_logic.py
import unittest

from logic import (
    validate_records, add_record, find_records,
    set_completed, delete_record, statistics,
)


def sample():
    return [
        {"id": 1, "title": "Сумма чисел", "category": "циклы", "amount": 3, "completed": True},
        {"id": 2, "title": "Палиндром", "category": "строки", "amount": 2, "completed": False},
        {"id": 3, "title": "Поиск максимума", "category": "циклы", "amount": 5, "completed": True},
        {"id": 4, "title": "Анаграммы", "category": "строки", "amount": 4, "completed": False},
    ]


class TestValidate(unittest.TestCase):
    def test_valid(self):
        validate_records(sample())

    def test_empty_list(self):
        validate_records([])

    def test_root_not_list(self):
        with self.assertRaises(ValueError):
            validate_records({"id": 1})

    def test_duplicate_id(self):
        data = sample()
        data[1]["id"] = 1
        with self.assertRaises(ValueError):
            validate_records(data)

    def test_missing_key(self):
        data = sample()
        del data[0]["category"]
        with self.assertRaises(ValueError):
            validate_records(data)

    def test_id_bool(self):
        data = sample()
        data[0]["id"] = True
        with self.assertRaises(ValueError):
            validate_records(data)

    def test_amount_bool(self):
        data = sample()
        data[0]["amount"] = True
        with self.assertRaises(ValueError):
            validate_records(data)

    def test_amount_negative(self):
        data = sample()
        data[0]["amount"] = -1
        with self.assertRaises(ValueError):
            validate_records(data)

    def test_completed_string(self):
        data = sample()
        data[0]["completed"] = "false"
        with self.assertRaises(ValueError):
            validate_records(data)

    def test_empty_title(self):
        data = sample()
        data[0]["title"] = "   "
        with self.assertRaises(ValueError):
            validate_records(data)


class TestAdd(unittest.TestCase):
    def test_add_to_empty(self):
        data = []
        record = add_record(data, "Python", "тест", 4)
        self.assertEqual(record["id"], 1)
        self.assertFalse(record["completed"])
        self.assertEqual(len(data), 1)

    def test_strip_spaces(self):
        data = []
        record = add_record(data, "  Python  ", "  тест ", 1)
        self.assertEqual(record["title"], "Python")
        self.assertEqual(record["category"], "тест")

    def test_same_titles_different_ids(self):
        data = []
        a = add_record(data, "Задача", "а", 1)
        b = add_record(data, "Задача", "а", 1)
        self.assertNotEqual(a["id"], b["id"])
        self.assertEqual(len(data), 2)

    def test_id_after_delete(self):
        data = []
        add_record(data, "А", "к", 1)
        add_record(data, "Б", "к", 1)
        delete_record(data, 1)
        self.assertEqual(data[0]["id"], 2)
        new = add_record(data, "В", "к", 1)
        self.assertEqual(new["id"], 3)

    def test_bad_input_adds_nothing(self):
        data = []
        for args in [("", "к", 1), ("А", "", 1), ("А", "к", -1), ("А", "к", "abc"), ("А", "к", True)]:
            with self.assertRaises(ValueError):
                add_record(data, *args)
        self.assertEqual(data, [])


class TestFind(unittest.TestCase):
    def test_case_insensitive(self):
        data = []
        add_record(data, "Python", "к", 1)
        self.assertEqual(len(find_records(data, "PY")), 1)

    def test_not_found(self):
        self.assertEqual(find_records(sample(), "яяя"), [])

    def test_empty_query(self):
        with self.assertRaises(ValueError):
            find_records(sample(), "  ")

    def test_does_not_change_data(self):
        data = sample()
        find_records(data, "а")
        self.assertEqual(data, sample())


class TestStatus(unittest.TestCase):
    def test_set_true(self):
        data = sample()
        self.assertTrue(set_completed(data, 2, True))
        self.assertTrue(data[1]["completed"])

    def test_set_false(self):
        data = sample()
        self.assertTrue(set_completed(data, 1, False))
        self.assertFalse(data[0]["completed"])

    def test_unknown_id(self):
        data = sample()
        self.assertFalse(set_completed(data, 99, True))
        self.assertEqual(data, sample())


class TestDelete(unittest.TestCase):
    def test_delete(self):
        data = sample()
        self.assertTrue(delete_record(data, 2))
        self.assertEqual([r["id"] for r in data], [1, 3, 4])

    def test_unknown_id(self):
        data = sample()
        self.assertFalse(delete_record(data, 99))
        self.assertEqual(data, sample())


class TestStatistics(unittest.TestCase):
    def test_two_categories(self):
        stats = statistics(sample())
        self.assertEqual(stats["total"], 4)
        self.assertEqual(stats["done"], 2)
        self.assertEqual(stats["not_done"], 2)
        self.assertEqual(stats["total_amount"], 14)
        self.assertEqual(stats["by_category"], {"строки": 6, "циклы": 8})
        self.assertEqual(list(stats["by_category"]), ["строки", "циклы"])

    def test_empty(self):
        stats = statistics([])
        self.assertEqual(stats["total"], 0)
        self.assertEqual(stats["done"], 0)
        self.assertEqual(stats["not_done"], 0)
        self.assertEqual(stats["total_amount"], 0)
        self.assertEqual(stats["by_category"], {})

    def test_two_records_example(self):
        data = []
        add_record(data, "А", "к", 4)
        add_record(data, "Б", "к", 2)
        set_completed(data, 2, True)
        stats = statistics(data)
        self.assertEqual((stats["total"], stats["done"], stats["not_done"], stats["total_amount"]), (2, 1, 1, 6))

    def test_does_not_change_data(self):
        data = sample()
        statistics(data)
        self.assertEqual(data, sample())


if _name_ == "_main_":
    unittest.main()
