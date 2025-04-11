import unittest
from employee import Employee
from employee_manager import EmployeeManager

class TestEmployeeManager(unittest.TestCase):
    def setUp(self):
        self.manager = EmployeeManager()
        self.emp1 = Employee("Abhijit", "IT", "Tester", 16000, 200, 1400)
        self.emp2 = Employee("Sabhi", "HR", "Analyst", 4500, 550, 350)
        self.manager.add_employee(self.emp1)
        self.manager.add_employee(self.emp2)

    def test_add_employee(self):
        self.assertEqual(len(self.manager.view_employees()), 2)

    def test_find_employee_by_id(self):
        found = self.manager.find_employee_by_id(self.emp1.id)
        self.assertIsNotNone(found)
        self.assertEqual(found.name, "Abhijit")

    def test_delete_employee(self):
        result = self.manager.delete_employee(self.emp1.id)
        self.assertTrue(result)
        self.assertEqual(len(self.manager.view_employees()), 1)

if __name__ == '__main__':
    unittest.main()