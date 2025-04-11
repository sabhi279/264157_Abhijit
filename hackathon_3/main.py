from employee import Employee
from employee_manager import EmployeeManager
from storage import Storage

def main():
    manager = EmployeeManager()
    manager.employees = Storage.load()

    while True:
        print("\nEmployee Management System")
        print("1. Add Employee")
        print("2. View All Employees")
        print("3. Search Employee by ID")
        print("4. Delete Employee")
        print("5. Save & Exit")
        
        choice = input("Enter your choice: ")

        if choice == '1':
            name = input("Enter name: ")
            dept = input("Enter department: ")
            desg = input("Enter designation: ")
            gross = float(input("Enter gross salary: "))
            tax = float(input("Enter tax amount: "))
            bonus = float(input("Enter bonus: "))
            emp = Employee(name, dept, desg, gross, tax, bonus)
            manager.add_employee(emp)
            print("Employee added.")

        elif choice == '2':
            for emp in manager.view_employees():
                print(emp)

        elif choice == '3':
            emp_id = input("Enter employee ID to search: ")
            emp = manager.find_employee_by_id(emp_id)
            if emp:
                print(emp)
            else:
                print("Employee not found.")

        elif choice == '4':
            emp_id = input("Enter employee ID to delete: ")
            if manager.delete_employee(emp_id):
                print("Employee deleted.")
            else:
                print("Employee not found.")

        elif choice == '5':
            Storage.save(manager.employees)
            print("Data saved. Exiting.")
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()