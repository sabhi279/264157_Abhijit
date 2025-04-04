from hackathon import Employee, Department, save_data, load_from_json
data_strings = [
        "Alice,30,Female,E101,HR,48000",
        "Bob,28,Male,E102,IT,55000",
        "Charlie,35,Male,E103,HR,60000",
        "Diana,26,Female,E104,IT,47000",
        "Evan,40,Male,E105,Finance,53000"
    ]
 
 
employees = [Employee.from_string(s) for s in data_strings]

departments = {}
for emp in employees:
    if emp.department not in departments:
        departments[emp.department] = Department(emp.department)
    departments[emp.department].add_employee(emp)


Employee.bonus_policy()
print("\nEmployee Details:")
for emp in employees:
    print(emp.get_details())
    print(f"Bonus Eligibility: {emp.is_eligible_for_bonus()}")


Employee.bonus_policy()


print("\nAverage Salary by Department:")
for dept_name, dept in departments.items():
    print(f"{dept_name}: ₹{dept.get_average_salary():.2f}")


save_data(departments.values())

loaded_departments = load_from_json()

# Print  data
print("\n Loaded all Employee Data :")
for dept in loaded_departments:
    print(f"\nDepartment: {dept.name}")
    for emp in dept.employees:
        print(emp.get_details())
 