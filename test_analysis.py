# test_analysis.py
import json
import unittest

from analysis import (
    validate_todos, completion_counts, top_users, select_tasks,
)

TODOS = [
    {"id": 1, "userId": 5, "title": "Ввод", "completed": True},
    {"id": 2, "userId": 5, "title": "Циклы", "completed": False},
    {"id": 3, "userId": 10, "title": "Строки", "completed": True},
    {"id": 4, "userId": 10, "title": "Файлы", "completed": True},
    {"id": 5, "userId": 5, "title": "Списки", "completed": True},
]


def leader_tasks(todos):
    leaders = top_users(completion_counts(todos))
    return [t for t in todos if t["completed"] and t["userId"] in leaders]


class TestLeaders(unittest.TestCase):
    def test_training_set(self):
        counts = completion_counts(TODOS)
        self.assertEqual(counts, {5: 2, 10: 2})
        self.assertEqual(top_users(counts), [5, 10])
        ids = [t["id"] for t in leader_tasks(TODOS)]
        self.assertEqual(ids, [1, 3, 4, 5])

    def test_empty_list(self):
        self.assertEqual(top_users(completion_counts([])), [])
        self.assertEqual(leader_tasks([]), [])

    def test_only_false(self):
        data = [{"id": 1, "userId": 5, "title": "А", "completed": False}]
        self.assertEqual(completion_counts(data), {5: 0})
        self.assertEqual(top_users({5: 0}), [])
        self.assertEqual(leader_tasks(data), [])

    def test_single_leader(self):
        self.assertEqual(top_users({5: 3, 10: 1}), [5])

    def test_several_leaders(self):
        self.assertEqual(top_users({10: 2, 5: 2, 7: 1}), [5, 10])


class TestSelect(unittest.TestCase):
    def ids(self, user_id, param):
        return [t["id"] for t in select_tasks(TODOS, user_id, param)]

    def test_example(self):
        self.assertEqual(self.ids(5, "с"), [5])

    def test_mixed_case(self):
        self.assertEqual(self.ids(5, "СпИ"), [5])

    def test_no_match(self):
        self.assertEqual(self.ids(5, "яяя"), [])

    def test_unknown_user(self):
        self.assertEqual(self.ids(99, "с"), [])

    def test_spaces_stripped(self):
        self.assertEqual(self.ids(5, "  с  "), [5])

    def test_empty_parameter(self):
        with self.assertRaises(ValueError):
            select_tasks(TODOS, 5, "   ")

    def test_original_not_changed(self):
        copy = json.loads(json.dumps(TODOS))
        select_tasks(TODOS, 5, "с")
        self.assertEqual(TODOS, copy)


class TestValidate(unittest.TestCase):
    def test_valid(self):
        validate_todos(TODOS)

    def test_object_instead_of_list(self):
        with self.assertRaises(ValueError):
            validate_todos({"id": 1})

    def test_duplicate_id(self):
        data = [dict(TODOS[0]), dict(TODOS[0])]
        with self.assertRaises(ValueError):
            validate_todos(data)

    def test_missing_user_id(self):
        data = [{"id": 1, "title": "А", "completed": True}]
        with self.assertRaises(ValueError):
            validate_todos(data)

    def test_completed_string(self):
        data = [{"id": 1, "userId": 5, "title": "А", "completed": "false"}]
        with self.assertRaises(ValueError):
            validate_todos(data)

    def test_id_true(self):
        data = [{"id": True, "userId": 5, "title": "А", "completed": True}]
        with self.assertRaises(ValueError):
            validate_todos(data)


class TestRoundTrip(unittest.TestCase):
    def test_write_and_read(self):
        selected = select_tasks(TODOS, 5, "с")
        text = json.dumps(selected, ensure_ascii=False, indent=2)
        self.assertEqual(json.loads(text), selected)


if _name_ == "_main_":
    unittest.main()
