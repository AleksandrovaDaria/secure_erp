import erp_main
import sales_controller
import os
from model import HRModel
from view import HRView
from controller import HRController

def display_main_menu():
        print("Main menu:")
        print("1. HR module ")
        print("2. CRM module")
        print("3. Sales module")
        print("0. Exit")

def run_main_menu():
        os.system('cls' if os.name == 'nt' else 'clear')
        while True:
                display_main_menu()
                choice = input("Enter choice: ")
                if choice == '1':
                    os.system('cls' if os.name == 'nt' else 'clear')
                    model = HRModel()
                    view = HRView()
                    controller = HRController(model, view)
                    controller.run()
                elif choice == '2':
                    os.system('cls' if os.name == 'nt' else 'clear')
                    erp_main.main()
                elif choice == '3':
                    os.system('cls' if os.name == 'nt' else 'clear')
                    sales_controller.main()
                elif choice == '0':
                    break
                

if __name__ == '__main__':
    run_main_menu()