from model import *
from view import *
import main_menu
import time
import os
class HRController():
    def __init__(self, model, view):
        self.model = model
        self.view = view

    def run(self):
        self.model.load_data('employees.csv')

        while True:
            os.system('cls' if os.name == 'nt' else 'clear')
            self.view.display_menu()
            choice = input("Enter choice: ")
            if choice == '1':
                self.list_employees()
                time.sleep(15)
            elif choice == '2':
                self.add_employee()
                time.sleep(15)
            elif choice == '3':
                self.update_employee()
                time.sleep(15)
            elif choice == '4':
                self.delete_employee()
                time.sleep(15)
            elif choice == '5':
                self.show_oldest_and_youngest_employees()
                time.sleep(15)
            elif choice == '6':
                self.show_average_employee_age()
                time.sleep(15)
            elif choice == '7':
                self.show_birthdays_within_two_weeks()
                time.sleep(15)
            elif choice == '8':
                self.show_number_of_employees_with_clearance()
                time.sleep(15)
            elif choice == '9':
                self.show_number_of_employees_per_department()
                time.sleep(15)
            elif choice == '0':
                self.model.save_data('employees.csv')
                break
            elif choice == '10':
                return main_menu.run_main_menu()

    def list_employees(self):
        employees = self.model.employees
        self.view.list_employees(employees)

    def add_employee(self):
        employee = self.view.input_employee_data()
        self.model.employees.append(employee)

    def update_employee(self):
        id = input("Enter employee ID: ")
        employee = next((e for e in self.model.employees if e.id == int(id)), None)
        if employee:
            new_employee = self.view.input_employee_data()
            employee.name = new_employee.name
            employee.department = new_employee.department
            employee.clearance_level = new_employee.clearance_level
            employee.birthdate = new_employee.birthdate
        else:
            print("Employee not found")

    def delete_employee(self):
        id = input("Enter employee ID: ")
        employee =         self.model.employees = [e for e in self.model.employees if e.id != int(id)]

    def show_oldest_and_youngest_employees(self):
        oldest, youngest = self.model.get_oldest_and_youngest_employees()
        self.view.print_oldest_and_youngest_employees(oldest, youngest)

    def show_average_employee_age(self):
        average_age = self.model.get_average_employee_age()
        self.view.print_average_employee_age(average_age)

    def show_birthdays_within_two_weeks(self):
        date = self.view.input_date()
        employee_names = self.model.get_birthdays_within_two_weeks(date)
        self.view.print_birthdays_within_two_weeks(employee_names)

    def show_number_of_employees_with_clearance(self):
        clearance_level = int(input("Enter clearance level: "))
        count = self.model.get_number_of_employees_with_clearance(clearance_level)
        self.view.print_number_of_employees_with_clearance(count)

    def show_number_of_employees_per_department(self):
        department_counts = self.model.get_number_of_employees_per_department()
        self.view.print_number_of_employees_per_department(department_counts)

