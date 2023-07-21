import unittest
from base import Base
import json
import os

class TestBase(unittest.TestCase):

    def test_create_with_custom_id(self):
        base_obj = Base(id=100)
        self.assertEqual(base_obj.id, 100)

    def test_create_without_custom_id(self):
        base_obj = Base()
        self.assertTrue(hasattr(base_obj, 'id'))

    def test_create_unique_ids(self):
        base_obj1 = Base()
        base_obj2 = Base()
        self.assertNotEqual(base_obj1.id, base_obj2.id)

    def test_to_json_string(self):
        data = [{'id': 1, 'name': 'Object1'}, {'id': 2, 'name': 'Object2'}]
        json_string = Base.to_json_string(data)
        self.assertEqual(json_string, json.dumps(data))

    def test_from_json_string(self):
        json_string = '[{"id": 1, "name": "Object1"}, {"id": 2, "name": "Object2"}]'
        data = Base.from_json_string(json_string)
        self.assertEqual(data, [{'id': 1, 'name': 'Object1'}, {'id': 2, 'name': 'Object2'}])

    def test_save_to_file(self):
        filename = 'test_save_to_file.json'
        data = [{'id': 1, 'name': 'Object1'}, {'id': 2, 'name': 'Object2'}]
        Base.save_to_file(data)
        self.assertTrue(os.path.exists(filename))
        with open(filename, 'r') as file:
            saved_data = json.load(file)
        self.assertEqual(saved_data, data)
        os.remove(filename)

    def test_load_from_file(self):
        filename = 'test_load_from_file.json'
        data = [{'id': 1, 'name': 'Object1'}, {'id': 2, 'name': 'Object2'}]
        with open(filename, 'w') as file:
            json.dump(data, file)
        loaded_data = Base.load_from_file()
        self.assertEqual(loaded_data, [{'id': 1, 'name': 'Object1'}, {'id': 2, 'name': 'Object2'}])
        os.remove(filename)

if __name__ == '__main__':
    unittest.main()
