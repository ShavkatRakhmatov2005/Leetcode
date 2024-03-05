import mysql.connector
db = mysql.connector.connect(
    host = "localhost",
    user = "root",
    password = "1234",
    auth_plugin='mysql_native_password'
)

if db.is_connected():
    print("Hello")
