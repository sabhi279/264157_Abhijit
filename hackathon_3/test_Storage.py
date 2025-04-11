import unittest
from employee import Employee
import os
import pickle
from storage import Storage

class TestStorage(unittest.TestCase):
    def setUp(self):
        self.test_file = "test_employees.pkl"
        self.original_file = Storage.FILE_NAME
        Storage.FILE_NAME = self.test_file
        self.employees = [Employee("Test", "QA", "Tester", 2000, 600, 1000)]

    def tearDown(self):
        if os.path.exists(self.test_file):
            os.remove(self.test_file)
        Storage.FILE_NAME = self.original_file

    def test_save_and_load(self):
        Storage.save(self.employees)
        loaded = Storage.load()
        self.assertEqual(len(loaded), 1)
        self.assertEqual(loaded[0].name, "Test")


if __name__ == '__main__':
    unittest.main()