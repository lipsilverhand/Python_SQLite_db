import sqlite3
import pandas as pd

# Connect to SQLite database
connect = sqlite3.connect('INSTRUCTOR.db')

# Create a cursor object
cursor_obj = connect.cursor()

# Drop the table if it already exists
cursor_obj.execute("DROP TABLE IF EXISTS INSTRUCTOR")

# Create the table
table = """ 
CREATE TABLE IF NOT EXISTS INSTRUCTOR(
    ID INTEGER PRIMARY KEY NOT NULL, 
    FNAME VARCHAR(20), 
    LNAME VARCHAR(20), 
    CITY VARCHAR(20), 
    CCODE CHAR(2)
);"""
cursor_obj.execute(table)
print("Table is Ready")

# Insert data into the table using executemany()
data = [
    (1, 'Rav', 'Ahuja', 'TORONTO', 'CA'),
    (2, 'Raul', 'Chong', 'Markham', 'CA'),
    (3, 'Hima', 'Vasudevan', 'Chicago', 'US')
]

cursor_obj.executemany("INSERT INTO INSTRUCTOR VALUES (?, ?, ?, ?, ?)", data)

# Commit the changes
connect.commit()

# Retrieve and print all the data
statement = '''SELECT * FROM INSTRUCTOR'''
cursor_obj.execute(statement)
print("All the data:")
output_all = cursor_obj.fetchall()
for row_all in output_all:
    print(row_all)

# Retrieve data into pandas DataFrame
df = pd.read_sql_query("SELECT * FROM INSTRUCTOR;", connect)
print(df)
print("Total rows and column:", df.shape)

# Close the connection
connect.close()
