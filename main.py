from parser.parse import Parser
from database import queries
from database.db import DB
import os


def parse_and_update_db():
    """
    parse files and updates db
    """
    days = os.listdir("./test-case-1")
    p = Parser()

    with DB() as db:
        for day in days:
            transactions = p.parse(f"test-case-1/{day}")
            for t in transactions:
                db.add_transaction(t)

month_dictionary = {
    "01": "January",
    "02": "February",
    "03": "March",
    "04": "April",
    "05": "May",
    "06": "June",
    "07": "July",
    "08": "August",
    "09": "September",
    "10": "October",
    "11": "November",
    "12": "December"
}

def main():
    # run this once
    # parse_and_update_db()

    # answer questions
    with DB() as db:
        # highest sales volume in a day
        res = db.executor.execute(queries.HIGHEST_SALES_VOLUME_IN_A_DAY)
        data = res.fetchone()
        print(f"\nThe highest sales volume in a day is {data[1]} and it happened on {data[0]}\n")

        # highest sales value in a day
        res = db.executor.execute(queries.HIGHEST_SALES_VALUE_IN_A_DAY)
        data = res.fetchone()
        print(f"\nThe highest sales value in a day is {data[1]} and it happened on {data[0]}\n")

        # most product sold ID by volume
        res = db.executor.execute(queries.MOST_SOLD_PRODUCT_ID_BY_VOLUME)
        data = res.fetchone()
        print(f"""\nThe ID of the most sold product is "PRODUCT:{data[0]}" and it sold a total of {data[1]} qts.\n""")

        # highest sale staff id for each month
        for i in range(1, 12):
            if i <= 9:
                i_str = "0" + str(i)
            else:
                i_str = str(i)
            res = db.executor.execute(queries.HIGHEST_STAFF_FOR_EACH_MONTH, [i_str])
            data = res.fetchone()
            print(f"""\n{month_dictionary[i_str]} | "Staff:{data[0]}" | NGN{data[1]}.\n""")
    
        

if __name__ == "__main__":
    main()
