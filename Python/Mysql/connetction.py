# connector to mysql
import mysql.connector

# Starting coonection
db = mysql.connector.connect(
    host = "localhost",
    user = "root",
    password = ""
)

# check connection status
if db.is_connected():
    print("Connection Sucseed")