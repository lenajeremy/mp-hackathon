"""
contains all sql queries
"""
CREATE_TRANSACTIONS_TABLE = """
CREATE TABLE IF NOT EXISTS Transactions (
    date TEXT,
    staff_id INT,
    value INT
);
"""

CREATE_PRODUCTS_TABLE = """
CREATE TABLE IF NOT EXISTS Products (
    id INT PRIMARY KEY,
    total_sold INT DEFAULT 0
);
"""

CREATE_STAFFS_TABLE = """
CREATE TABLE IF NOT EXISTS Staffs (
    id INT PRIMARY KEY
);
"""

ADD_UPDATE_PRODUCT = """
INSERT INTO Products (id, total_sold)
VALUES(?, ?)
ON CONFLICT(id) 
DO 
   UPDATE SET total_sold = total_sold + ? 
   WHERE id = ?;
"""

ADD_TRANSACTION = """
INSERT INTO Transactions (date, staff_id, value)
VALUES (?, ?, ?)
"""


ADD_STAFF = """
INSERT INTO Staffs(id)
VALUES(?)
ON CONFLICT(id) 
DO NOTHING
"""

HIGHEST_SALES_VOLUME_IN_A_DAY = """
SELECT
  STRFTIME('%Y-%m-%d', date) AS date,
  COUNT(*) AS volume
FROM Transactions
GROUP BY
  STRFTIME('%Y-%m-%d', date)
ORDER BY volume DESC
LIMIT 1;
"""

HIGHEST_SALES_VALUE_IN_A_DAY = """
SELECT
  STRFTIME('%Y-%m-%d', date) AS date,
  SUM(value) AS value
FROM Transactions
GROUP BY
  STRFTIME('%Y-%m-%d', date)
ORDER BY value DESC
LIMIT 1;
"""

MOST_SOLD_PRODUCT_ID_BY_VOLUME = """
SELECT id, MAX(total_sold) FROM Products;
"""

HIGHEST_STAFF_FOR_EACH_MONTH = """
SELECT staff_id, SUM(value) as total_sales FROM Transactions
WHERE STRFTIME('%m', date) = ?
GROUP BY staff_id
ORDER BY total_sales DESC
LIMIT 1;
"""

HIGHEST_HOUR_OF_THE_DAY = """
SELECT AVG(value), STRFTIME('%H', date) as average
FROM
    Transactions
GROUP BY
    STRFTIME('%H', date)
ORDER BY average DESC
LIMIT 1;
"""
