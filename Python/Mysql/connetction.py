# connector to mysql
import mysql.connector

# Starting coonection
db = mysql.connector.connect(
    host = "localhost",
    user = "root",
    password = ""
)

# Creating 'cursor' as query executioner
cursor = db.cursor()

# Creating database
cursor.execute("CREATE DATABASE nizari")

print("Database berhasil dibuat")
