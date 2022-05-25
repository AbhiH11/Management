import mysql.connector

mydb = mysql.connector.connect(
    host = "localhost",
    username = "root",
    password = "Goodlooking@92",
    database = "Abhi"
)

my_cursor = mydb.cursor()

my_cursor.execute("show tables")
for x in my_cursor:
    print(x)
# sql = "show tables"

# my_cursor.execute(sql)
# mydb.commit()

