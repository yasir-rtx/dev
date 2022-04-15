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

# UPDATE DATA 
sql = "UPDATE members SET name=%s, kode=%s, level=%s WHERE id=%s"
val = ("Ian", "Arjuna", "First", 7)
cursor.execute(sql, val)
db.commit()
print("{} data diubah".format(cursor.rowcount))