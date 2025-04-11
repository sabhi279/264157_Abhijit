import uuid


class Employee:
    def __init__(self, name: str, department: str, designation: str, gross_salary: float, tax: float, bonus: float):
        self.id = str(uuid.uuid4())
        self.name = name
        self.department = department
        self.designation = designation
        self.gross_salary = gross_salary
        self.tax = tax
        self.bonus = bonus
        self.net_salary = self.calculate_net_salary()

    def calculate_net_salary(self):
        return self.gross_salary - self.tax + self.bonus

    def __str__(self):
        return (f"ID: {self.id}, Name: {self.name}, Department: {self.department}, Designation: {self.designation}, "
                f"Gross Salary: {self.gross_salary}, Tax: {self.tax}, Bonus: {self.bonus}, Net Salary: {self.net_salary}")