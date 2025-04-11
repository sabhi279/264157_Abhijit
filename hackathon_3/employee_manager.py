from employee import Employee


class EmployeeManager:
    def __init__(self):
        self.employees = []

    def add_employee(self, employee):
        self.employees.append(employee)

    def view_employees(self):
        return self.employees

    def find_employee_by_id(self, emp_id):
        for e in self.employees:
            if e.id == emp_id:
                return e
        return None

    def delete_employee(self, emp_id):
        employee = self.find_employee_by_id(emp_id)
        if employee:
            self.employees.remove(employee)
            return True
        return False