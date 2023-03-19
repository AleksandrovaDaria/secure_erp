import csv
from datetime import datetime, timedelta

class Employee:
    def __init__(self, id, name, department, clearance_level, birthdate):
        self.id = id
        self.name = name
        self.department = department
        self.clearance_level = clearance_level
        self.birthdate = birthdate

class HRModel:
    def __init__(self):
        self.employees = []

    def load_data(self, filename):
        with open(filename, 'r') as file:
            reader = csv.reader(file)
            next(reader) # skip header row
            for row in reader:
                id, name, department, clearance_level, birthdate_str = row
                birthdate = datetime.strptime(birthdate_str, '%Y-%m-%d').date()
                self.employees.append(Employee(int(id), name, department, int(clearance_level), birthdate))

    def save_data(self, filename):
        with open(filename, 'w', newline='') as file:
            writer = csv.writer(file)
            writer.writerow(['id', 'name', 'department', 'clearance_level', 'birthdate'])
            for employee in self.employees:
                writer.writerow([employee.id, employee.name, employee.department, employee.clearance_level, employee.birthdate.strftime('%Y-%m-%d')])

    def get_oldest_and_youngest_employees(self):
        oldest = min(self.employees, key=lambda e: e.birthdate)
        youngest = max(self.employees, key=lambda e: e.birthdate)
        return (oldest.name, youngest.name)

    def get_average_employee_age(self):
        now = datetime.now().date()
        total_age = sum((now - e.birthdate).days / 365 for e in self.employees)
        return total_age / len(self.employees)

    def get_birthdays_within_two_weeks(self, input_date):
        start_date = input_date.date()
        end_date = (input_date + timedelta(days=14)).date()
        return [e.name for e in self.employees if start_date <= e.birthdate <= end_date]

    def get_number_of_employees_with_clearance(self, clearance_level):
        return sum(1 for e in self.employees if e.clearance_level >= clearance_level)

    def get_number_of_employees_per_department(self):
        department_counts = {}
        for e in self.employees:
            if e.department in department_counts:
                department_counts[e.department] += 1
            else:
                department_counts[e.department] = 1
        return department_counts
