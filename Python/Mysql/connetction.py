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

# %s == placeholder
sql = "INSERT INTO members (kode, name, level) VALUES (%s, %s, %s)"
values = [
    ("Smirking Death", "Zacht", "Master"),
    ("Oni", "Rvier", "Second"),
    ("Dove", "Nicholas", "Second"),
    ("Xenomorph", "Aeins", "Second")
]

for val in values:
    cursor.execute(sql, val)
    db.commit() # SAVE DATA
print ("{} data ditambahkan".format(len(values)))