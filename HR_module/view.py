from model import*

class HRView:
    def __init__(self):
        pass

    def display_menu(self):
        print("HR Module Options:")
        print("1. List all employees")
        print("2. Add an employee")
        print("3. Update an employee")
        print("4. Delete an employee")
        print("5. Show oldest and youngest employees")
        print("6. Show average employee age")
        print("7. Show employees with birthdays within two weeks of a date")
        print("8. Show number of employees with at least a certain clearance level")
        print("9. Show number of employees per department")
        print("0. Exit")

    def input_employee_data(self):
        id = input("Enter employee ID: ")
        name = input("Enter employee name: ")
        department = input("Enter employee department: ")
        clearance_level = input("Enter employee clearance level: ")
        birthdate_str = input("Enter employee birthdate (YYYY-MM-DD): ")
        birthdate = datetime.strptime(birthdate_str, '%Y-%m-%d').date()
        return Employee(int(id), name, department, int(clearance_level), birthdate)

    def input_date(self):
        date_str = input("Enter date (YYYY-MM-DD): ")
        return datetime.strptime(date_str, '%Y-%m-%d')

    def list_employees(self, employees):
        print("{:<5} {:<20} {:<10} {:<10} {:<10}".format("ID", "Name", "Department", "Clearance", "Birthdate"))
        for e in employees:
            print("{:<5} {:<20} {:<10} {:<10} {:<10}".format(e.id, e.name, e.department, e.clearance_level, e.birthdate.strftime('%Y-%m-%d')))

    def print_oldest_and_youngest_employees(self, oldest_name, youngest_name):
        print("Oldest employee: {}".format(oldest_name))
        print("Youngest employee: {}".format(youngest_name))

    def print_average_employee_age(self, average_age):
        print("Average employee age: {:.1f} years".format(average_age))

    def print_birthdays_within_two_weeks(self, employee_names):
        print("Employees with birthdays within two weeks:")
        for name in employee_names:
            print("- {}".format(name))

    def print_number_of_employees_with_clearance(self, count):
        print("Number of employees with at least this clearance level: {}".format(count))

    def print_number_of_employees_per_department(self, department_counts):
        print("Number of employees per department:")
        for department, count in department_counts.items():
            print("- {}: {}".format(department, count))
