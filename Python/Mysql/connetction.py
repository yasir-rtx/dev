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

sql = "INSERT INTO members (kode, name, level) VALUES (%s, %s, %s)"
val = ("Ghost", "Yelf", "Spesial")
cursor.execute(sql, val)
db.commit()
print ("{} data ditambahkan".format(cursor.rowcount))
