import json


def update_salaries(department):
    expenses = department.get('expenses', 0)
    income = department.get('income', 0)

    if expenses < income:
        for employee in department.get('employees', []):
            salary = employee.get('salary', 0)
            new_salary = salary * 1.1  # increase salary on 10%
            employee['salary'] = round(new_salary, 2)


with open('departments.json', 'r') as file:
    data = json.load(file)

for department in data.get('departments', []):
    update_salaries(department)

with open('new_costs.json', 'w') as new_file:
    json.dump(data, new_file, indent=2)

print("Updated file is new_costs.json")
