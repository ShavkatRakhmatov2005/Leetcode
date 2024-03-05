import mysql.connector

db = mysql.connector.connect(
    host="localhost",
    user="root",
    password="1234",
    database="Cinema"  # Added database parameter
)
cursor = db.cursor()

def createdatabase():
    try:
        cursor.execute("CREATE DATABASE IF NOT EXISTS Cinema;")
        cursor.execute("USE Cinema;")
        print("Database created or exists")
    except mysql.connector.Error as err:
        print("Database creation error:", err)

def createtable():
    try:
        cursor.execute("""
            CREATE TABLE IF NOT EXISTS cinemas(
                id INT AUTO_INCREMENT PRIMARY KEY,
                name VARCHAR(50),
                position VARCHAR(50),
                salary INT,
                bonus INT,
                year FLOAT,
                department VARCHAR(50),
                period BOOLEAN
            );
        """)
        print("Table created or exists")
    except mysql.connector.Error as err:
        print("Table creation error:", err)

def insertDataToCinemasTable(name, position, salary, bonus, year, department, period):
    try:
        cursor.execute("INSERT INTO cinemas (name, position, salary, bonus, year, department, period) VALUES (%s, %s, %s, %s, %s, %s, %s);",
                       (name, position, salary, bonus, year, department, period))
        db.commit()
        print("Data inserted successfully")
    except mysql.connector.Error as err:
        print("Insertion error:", err)
        db.rollback()

def selectCinemas():
    cursor.execute("SELECT * FROM cinemas;")
    cinemas = cursor.fetchall()
    return cinemas

data=[
    ('Akbar', 'Junior', 600, 100, 1, "1-bo'lim", True),
    ('Alice', 'Senior', 1000, 200, 2, "2-bo'lim", False),
    ('Bob', 'Manager', 1500, 300, 3, "3-bo'lim", True),
    ('Eve', 'Director', 2000, 400, 4, "4-bo'lim", False),
    ('Charlie', 'CEO', 2500, 500, 5, "5-bo'lim", True)
]

createdatabase()
createtable()

for i in data:
    insertDataToCinemasTable(*i)

dat = selectCinemas()
for cinem in dat:
    print(cinem)

cursor.close()
db.close()
