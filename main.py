from parser.parse import Parser
from database.db import DB
import os

def main():
    days = os.listdir("./test-case-1")
    p = Parser()

    with DB() as db:
        for day in days:
            transactions = p.parse(f"test-case-1/{day}")
            for t in transactions:
                db.add_transaction(t)


if __name__ == "__main__":
    main()
