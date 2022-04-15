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

# DELETE DATA
sql = "DELETE FROM members WHERE id=%s"
val = (9, )
cursor.execute(sql, val)
db.commit()
print("{} data berhasil dihapus".format(cursor.rowcount))