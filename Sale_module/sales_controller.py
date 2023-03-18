from model_sales import Sales
from view_terminal import get_input

class SalesController:
    def __init__(self, data_file):
        self.model = Sales(data_file)

    def list_transactions(self):
        transactions = self.model.transactions
        if not transactions:
            print("No transactions found.")
        else:
            for transaction in transactions:
                print(f"{transaction['id']} - {transaction['date']} - {transaction['product']} - {transaction['price']}")

    def add_transaction(self):
        id=get_input("ID")
        product = get_input("Product")
        price = float(get_input("Price"))
        date = get_input("Date (YYYY-MM-DD)")
        new_transaction = {"id":id, "date": date, "product": product, "price": price}
        self.model.add_transaction(new_transaction)
        print("Transaction added successfully.")

    def update_transaction(self):
        transaction_id = get_input("Transaction ID")
        transaction = self.model.get_transaction(transaction_id)
        if not transaction:
            print("Transaction not found.")
        else:
            id=get_input(f"ID({transaction['id']})")
            date = get_input(f"Date ({transaction['date']})")
            product = get_input(f"Product ({transaction['product']})")
            price = get_input(f"Price ({transaction['price']})")
            updated_transaction = {"id": transaction_id, "date": date or transaction['date'] , "product": product or transaction['product'], "price": price or transaction['price']}
            self.model.update_transaction(transaction_id, updated_transaction)
            print("Transaction updated successfully.")

    def delete_transaction(self):
        transaction_id = get_input("Transaction ID")
        transaction = self.model.get_transaction(transaction_id)
        if not transaction:
            print("Transaction not found.")
        else:
            self.model.delete_transaction(transaction_id)
            print("Transaction deleted successfully.")

    def get_biggest_revenue_transaction(self):
        transaction = self.model.get_biggest_revenue_transaction()
        if not transaction:
            print("No transactions found.")
        else:
            print(f"Transaction with biggest revenue: {transaction['id']}- {transaction['date']} - {transaction['product']} - {transaction['price']}")

    def get_biggest_revenue_product(self):
        product = self.model.get_biggest_revenue_product()
        if not product:
            print("No transactions found.")
        else:
            print(f"Product with biggest revenue: {product}.")

    def count_transactions_between(self):
        start_date = get_input("Start date (YYYY-MM-DD)")
        end_date = get_input("End date (YYYY-MM-DD)")
        count = self.model.count_transactions_between(start_date, end_date)
        print(f"Number of transactions between {start_date} and {end_date}: {count}.")

    def sum_transactions_between(self):
        start_date = get_input("Start date (YYYY-MM-DD)")
        end_date = get_input("End date (YYYY-MM-DD)")
        total_price = self.model.sum_transactions_between(start_date, end_date)
        print(f"Total price of transactions between {start_date} and {end_date}: {total_price}.")


def main():
    controller = SalesController(data_file="sales.csv")

    while True:
        print("\nSale Module:")
        print("1. List transactions")
        print("2. Add new transaction")
        print("3. Update transaction")
        print("4. Remove transaction")
        print("5. Get the transaction that made the biggest revenue")
        print("6. Get the product that made the biggest revenue altogether")
        print("7. Count number of transactions between")
        print("8. Sum the price of transactions between")
        choice = input("Enter choice (1-8): ")

        if choice == "1":
            controller.list_transactions()
        elif choice == "2":
            controller.add_transaction()
        elif choice == "3":
            controller.update_transaction()
        elif choice == "4":
            controller.delete_transaction()
        elif choice == "5":
            controller.get_biggest_revenue_transaction()
        elif choice == "6":
            controller.get_biggest_revenue_product()
        elif choice == "7":
            controller.count_transactions_between()
        elif choice == "8":
            controller.sum_transactions_between()
        else:
            break

if __name__ == "__main__":
    main()

