import sqlite3

# Open database
user_file = input("File: ")
db = sqlite3.connect(f"{user_file}")
cursor = db.cursor()

# Ask user if he needs help recalling table and column names
help = input("Do you want to see database structure? ").upper()
if help == "YES" or help == "Y":
    list = cursor.execute("SELECT name FROM sqlite_schema;")
    print(list.fetchall())

# Show original column
table = input("Table: ")
column = input("Column's name: ")
original_names = cursor.execute("SELECT ? FROM ?;", column, table)
print(original_names)

