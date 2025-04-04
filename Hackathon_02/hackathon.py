import json

class Person(object):
    def __init__(self,name,age,gender):
        self.name = name 
        self.age = age 
        self.gender = gender
        
    def get_details(self):
        return f"Name: {self.name}, Age: {self.age}, Gender: {self.gender}"
    
    
    
        
class Employee(Person):
    def __init__(self, name, age, gender, emp_id, department, salary):
        super().__init__(name, age, gender)
        self.emp_id = emp_id
        self.department = department
        self.salary = salary
        
        
    #data of employees
    data_strings = [
    "Alice,30,Female,E101,HR,48000",
    "Bob,28,Male,E102,IT,55000",
    "Charlie,35,Male,E103,HR,60000",
    "Diana,26,Female,E104,IT,47000",
    "Evan,40,Male,E105,Finance,53000"
    ]
        
    def get_details(self):
        return f"{super().get_details()}, Emp ID: {self.emp_id}, Department: {self.department}, Salary: {self.salary}"
       
       
    @staticmethod
    def bonus_policy():
        print("Bomus Policy will be applicable only for less than 50000 earner.") 
    
    def is_eligible_for_bonus(self):
        if self.salary<50000:
            return "You are eligible for bonus !!"
        else:
            return "You are not eligible for bonus !!"
    
    @classmethod
    def from_string(cls,data_string):
        name, age, gender, emp_id, department, salary = data_string.split(',')
        return cls(name, int(age), gender, emp_id, department, float(salary))
        
    
    @staticmethod
    def bonus_policy():
        print("*"*50,"Good News","*"*50)
        print("Bomus Policy will be applicable only for less than 50000 earner.")
        print('.'*100)
        
   
   
class Department:
    def __init__(self, name):
        self.name = name
        self.employees = []  
    
    def add_employee(self, employee):
        self.employees.append(employee)
    
    def get_average_salary(self):
        total_salary = sum(emp.salary for emp in self.employees)
        return total_salary / len(self.employees)
    
    def get_all_employees(self):
        return [emp.get_details() for emp in self.employees]
        
    
    
def save_data(departments, filename="Employees_data.json"):
    data = {}
    for dept in departments:
        employees_data = []
        for emp in dept.employees:
            emp_data = {
                'name': emp.name,
                'age': emp.age,
                'gender': emp.gender,
                'emp_id': emp.emp_id,
                'department': emp.department,
                'salary': emp.salary
            }
            employees_data.append(emp_data)
        data[dept.name] = employees_data
    
    with open(filename, 'w') as file:
        json.dump(data, file, indent=5)

def load_from_json(filename="Employees_data.json"):
    departments = []
    
    with open(filename, 'r') as file:
        data = json.load(file)
    
    for dept_name, employees_data in data.items():
        department = Department(dept_name)
        for emp_data in employees_data:
            emp = Employee(emp_data['name'], emp_data['age'], emp_data['gender'],
                           emp_data['emp_id'], emp_data['department'], emp_data['salary'])
            department.add_employee(emp)
        departments.append(department)
    
    return departments
    
    

    
    
