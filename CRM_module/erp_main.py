import random 

class Customer:
    def __init__(self, name, email, subscription_status):
        self.id = random.randint(1000, 9999)
        self.name = name
        self.email = email
        self.subscription_status = subscription_status

class CustomerModel:
    def __init__(self):
        self.customers = []

    def add_customer(self, name, email, subscription_status):
        customer = Customer(name, email, subscription_status)
        self.customers.append(customer)

    def get_customers(self):
        return self.customers

    def update_customer(self, customer_id, name, email, subscription_status):
        for customer in self.customers:
            if customer.id == customer_id:
                customer.name = name
                customer.email = email
                customer.subscription_status = subscription_status
                break

    def delete_customer(self, customer_id):
        for customer in self.customers:
            if customer.id == customer_id:
                self.customers.remove(customer)
                break

    def get_subscribed_emails(self):
        subscribed_emails = []
        for customer in self.customers:
            if customer.subscription_status == "subscribed":
                subscribed_emails.append(customer.email)
        return subscribed_emails

class CustomerView:
    def display_customers(self, customers):
        print("ID\tName\t\tEmail\t\tSubscription Status")
        for customer in customers:
            print(f"{customer.id}\t{customer.name}\t{customer.email}\t{customer.subscription_status}")

    def input_customer_data(self):
        name = input("Enter customer name: ")
        email = input("Enter customer email: ")
        subscription_status = input("Enter customer subscription status (subscribed/unsubscribed): ")
        return name, email, subscription_status

    def input_customer_id(self):
        customer_id = int(input("Enter customer ID: "))
        return customer_id

    def display_subscribed_emails(self, emails):
        print("Subscribed Emails:")
        for email in emails:
            print(email)

class CustomerController:
    def __init__(self):
        self.model = CustomerModel()
        self.view = CustomerView()

    def add_customer(self):
        name, email, subscription_status = self.view.input_customer_data()
        self.model.add_customer(name, email, subscription_status)

    def get_customers(self):
        customers = self.model.get_customers()
        self.view.display_customers(customers)

    def update_customer(self):
        customer_id = self.view.input_customer_id()
        name, email, subscription_status = self.view.input_customer_data()
        self.model.update_customer(customer_id, name, email, subscription_status)

    def delete_customer(self):
        customer_id = self.view.input_customer_id()
        self.model.delete_customer(customer_id)

    def get_subscribed_emails(self):
        emails = self.model.get_subscribed_emails()
        self.view.display_subscribed_emails(emails)

def main():
    controller = CustomerController()

    while True:
        print("\nCRM Module:")
        print("1. Add Customer")
        print("2. View Customers")
        print("3. Update Customer")
        print("4. Delete Customer")
        print("5. Get Subscribed Emails")
        choice = input("Enter choice (1-5): ")

        if choice == "1":
            controller.add_customer()
        elif choice == "2":
            controller.get_customers()
        elif choice == "3":
            controller.update_customer()
        elif choice == "4":
            controller.delete_customer()
        elif choice == "5":
            controller.get_subscribed_emails()
        else:
            break

if __name__ == "__main__":
    main()
