import pymysql

mydb = pymysql.connect(
    host='localhost',
    user='root',
    password='root'
)

mycursor = mydb.cursor()
mycursor.execute("CREATE DATABASE flaskdb")
mycursor.execute("SHOW DATABASES")
for db in mycursor:
    print(db)