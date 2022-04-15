# connector to mysql
import mysql.connector

# Starting coonection
db = mysql.connector.connect(
    host = "localhost",
    user = "root",
    password = "",
    database = "nizari"
)

# Creating 'cursor' as query executioner
cursor = db.cursor()

sql = """CREATE TABLE members (
    id INT AUTO_INCREMENT PRIMARY KEY,
    kode VARCHAR(255),
    name VARCHAR(255),
    level VARCHAR(255)
)
"""

cursor.execute(sql)
print ("Table created")