"""
Required models
"""
from typing import List

class Sale:
    """
    A sale
    """
    product_id: str
    quantity: int

    def __init__(self, product_id: str, quantity: int):
        self.product_id = product_id
        self.quantity = quantity


class Transaction:
    """
    A transaction
    """
    date: str
    sale_amount: str
    staff_id: str
    sale: List[Sale]

    def __init__(self, date: str, sale_amount: float, staff_id: str, sale: List[Sale]):
        self.date = date
        self.sale_amount = sale_amount
        self.staff_id = staff_id
        self.sale = sale

