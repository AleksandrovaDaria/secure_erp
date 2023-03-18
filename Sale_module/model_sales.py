import csv
import os


class Sales:
    def __init__(self, data_file):
        self.data_file = data_file
        self.transactions = []
        self.load_data()

    def load_data(self):
        if os.path.exists(self.data_file):
            with open(self.data_file, 'r', newline='') as f:
                reader = csv.DictReader(f)
                self.transactions = [row for row in reader]

    def save_data(self):
        with open(self.data_file, 'w', newline='') as f:
            fieldnames = ['id', 'date', 'product', 'price']
            writer = csv.DictWriter(f, fieldnames=fieldnames)
            writer.writeheader()
            writer.writerows(self.transactions)

    def add_transaction(self, transaction):
        self.transactions.append(transaction)
        self.save_data()

    def get_transaction(self, transaction_id):
        for transaction in self.transactions:
            if transaction['id'] == transaction_id:
                return transaction
        return None

    def update_transaction(self, transaction_id, new_transaction):
        for i, transaction in enumerate(self.transactions):
            if transaction['id'] == transaction_id:
                self.transactions[i] = new_transaction
                self.save_data()
                return True
        return False

    def delete_transaction(self, transaction_id):
        for i, transaction in enumerate(self.transactions):
            if transaction['id'] == transaction_id:
                del self.transactions[i]
                self.save_data()
                return True
        return False

    def get_biggest_revenue_transaction(self):
        if not self.transactions:
            return None
        return max(self.transactions, key=lambda t: float(t['price']))

    def get_biggest_revenue_product(self):
        if not self.transactions:
            return None
        products_revenue = {}
        for transaction in self.transactions:
            product = transaction['product']
            if product in products_revenue:
                products_revenue[product] += float(transaction['price'])
            else:
                products_revenue[product] = float(transaction['price'])
        return max(products_revenue, key=products_revenue.get)

    def count_transactions_between(self, start_date, end_date):
        count = 0
        for transaction in self.transactions:
            if start_date <= transaction['date'] <= end_date:
                count += 1
        return count

    def sum_transactions_between(self, start_date, end_date):
        total_price = 0
        for transaction in self.transactions:
            if start_date <= transaction['date'] <= end_date:
                total_price += float(transaction['price'])
        return total_price
