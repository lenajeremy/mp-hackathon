"""
Handles parsing transaction file for each day.
Takes in a file string, and returns an array of transactions.
"""

from typing import List
from models.main import Transaction, Sale

class Parser:
    """
    The Parser class handles anything about parsing transactions
    """
    def __init__(self):
        pass

    def parse(self, file_name: str) -> List[Transaction]:
        """
        Parses a single file and returns a list of transactions
        """
        all_transactions = []
        with open(file=file_name, mode="r", encoding="utf-8") as file:
            content = file.read()
            transactions = content.split("\n")
            for transaction in transactions:
                if transaction:
                    # this is assuming that the amount are represented without commas
                    staff_id, transaction_time, sale, amount = transaction.split(",")
                    t = Transaction(
                        staff_id=staff_id, 
                        sale_amount=amount, 
                        date=transaction_time, 
                        sale=self.parse_products(sale)
                    )
                    all_transactions.append(t)

        return all_transactions

    def parse_products(self, product_str: str) -> List[Sale]:
        product_str = product_str[1:-1]
        product_sales = product_str.split("|")
        sales = []

        for sale in product_sales:
            product_id, amount = sale.split(":")
            s = Sale(product_id, int(amount))
            sales.append(s)

        return sales
