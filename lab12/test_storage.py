# test_storage.py
import json
import os
import tempfile
import unittest

from storage import load_records, save_records

SAMPLE = [
    {"id": 1, "title": "Сумма чисел", "category": "циклы", "amount": 3, "completed": True},
    {"id": 2, "title": "Палиндром", "category": "строки", "amount": 2, "completed": False},
]


class TestStorage(unittest.TestCase):
    def test_save_and_reload(self):
        with tempfile.TemporaryDirectory() as folder:
            path = os.path.join(folder, "data.json")
            save_records(path, SAMPLE)
            self.assertEqual(load_records(path), SAMPLE)

    def test_empty_list(self):
        with tempfile.TemporaryDirectory() as folder:
            path = os.path.join(folder, "data.json")
            save_records(path, [])
            self.assertEqual(load_records(path), [])

    def test_cyrillic_readable_in_file(self):
        with tempfile.TemporaryDirectory() as folder:
            path = os.path.join(folder, "data.json")
            save_records(path, SAMPLE)
            with open(path, "r", encoding="utf-8") as file:
                text = file.read()
            self.assertIn("Палиндром", text)

    def test_missing_file(self):
        with tempfile.TemporaryDirectory() as folder:
            with self.assertRaises(FileNotFoundError):
                load_records(os.path.join(folder, "none.json"))

    def test_broken_json_file_unchanged(self):
        with tempfile.TemporaryDirectory() as folder:
            path = os.path.join(folder, "data.json")
            with open(path, "w", encoding="utf-8") as file:
                file.write("[{broken")
            with self.assertRaises(ValueError):
                load_records(path)
            with open(path, "r", encoding="utf-8") as file:
                self.assertEqual(file.read(), "[{broken")

    def test_duplicate_id(self):
        with tempfile.TemporaryDirectory() as folder:
            path = os.path.join(folder, "data.json")
            data = [dict(SAMPLE[0]), dict(SAMPLE[0])]
            with open(path, "w", encoding="utf-8") as file:
                json.dump(data, file)
            with self.assertRaises(ValueError):
                load_records(path)

    def test_wrong_encoding(self):
        with tempfile.TemporaryDirectory() as folder:
            path = os.path.join(folder, "data.json")
            with open(path, "wb") as file:
                file.write(b"\xff\xfe\x00\x00")
            with self.assertRaises(ValueError):
                load_records(path)

    def test_root_is_object(self):
        with tempfile.TemporaryDirectory() as folder:
            path = os.path.join(folder, "data.json")
            with open(path, "w", encoding="utf-8") as file:
                json.dump({"id": 1}, file)
            with self.assertRaises(ValueError):
                load_records(path)

    def test_save_invalid_keeps_old_file(self):
        with tempfile.TemporaryDirectory() as folder:
            path = os.path.join(folder, "data.json")
            save_records(path, SAMPLE)
            bad = [{"id": 1}]
            with self.assertRaises(ValueError):
                save_records(path, bad)
            self.assertEqual(load_records(path), SAMPLE)

    def test_save_error_raises(self):
        with tempfile.TemporaryDirectory() as folder:
            path = os.path.join(folder, "no_folder", "data.json")
            with self.assertRaises(OSError):
                save_records(path, SAMPLE)

    def test_extra_keys_kept(self):
        with tempfile.TemporaryDirectory() as folder:
            path = os.path.join(folder, "data.json")
            data = [dict(SAMPLE[0], note="x")]
            save_records(path, data)
            self.assertEqual(load_records(path), data)


if _name_ == "_main_":
    unittest.main()
