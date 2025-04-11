import unittest
from employee import Employee

class TestEmployee(unittest.TestCase):
    def setUp(self):
        self.emp = Employee("Abhijit Mandal", "IT", "test Engineer", 24000, 500, 1000)

    def test_net_salary_calculation(self):
        self.assertEqual(self.emp.net_salary, 24500)

    def test_employee_attributes(self):
        self.assertEqual(self.emp.name, "Abhijit Mandal")
        self.assertEqual(self.emp.department, "IT")
        self.assertEqual(self.emp.designation, "test Engineer")
        
        

if __name__ == '__main__':
    unittest.main()