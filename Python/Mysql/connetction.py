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

# SELECT DATA
# fetchall() untuk ambil semua data;
# fetachmany(10) untuk ambil 10 data;
# fetchone() untuk mengambil satu data pertama saja.
sql = "SELECT * FROM members"
cursor.execute(sql)

# Variabel untuk menampung data dari sql
results = cursor.fetchall()

for data in results :
    print(data)