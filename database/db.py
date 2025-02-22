import sqlite3
from models.main import Transaction
from . import queries as q

class DB:
    def __init__(self):
        db = "main.db"
        self.conn = sqlite3.connect(db)
        self.executor = self.conn.cursor()

        for query in [q.CREATE_STAFFS_TABLE, q.CREATE_PRODUCTS_TABLE, q.CREATE_TRANSACTIONS_TABLE]:
            self.executor.execute(query)

    def __exit__(self, exc_type, exc_val, traceback):
        """
        Runs when exiting `with` block
        """
        print("closing database connection")
        self.conn.close()

    def __enter__(self):
        """
        Runs when entering `with` block
        """
        print("initializing db")
        return self

    def add_transaction(self, t: Transaction):
        """
        adds transaction to database
        """
        # volume = 0
        # for sale in t.sale:
        #     volume += sale.quantity

        print(t.staff_id, t.sale_amount)
        self.executor.execute(q.ADD_TRANSACTION, (t.date, t.staff_id, t.sale_amount))

        for sale in t.sale:
            self.executor.execute(q.ADD_UPDATE_PRODUCT, (sale.product_id, sale.quantity, sale.quantity, sale.product_id))

        self.executor.execute(q.ADD_STAFF, (t.staff_id))

        self.conn.commit()
