#Importing dependencies for the exercise (sqlite3)
import sqlite3
#Setting the file used for the database to a variable
DATABASE_PATH = "school.db"
#Creating a connection to a database and assigning that connection to a variable
connection = sqlite3.connect(DATABASE_PATH)
#Creating the cursor to interact with the database
cursor = connection.cursor()
#Creating the companies table with an id and name
sql = (
    '''
        CREATE TABLE IF NOT EXISTS companies (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            name TEXT NOT NULL
        )
    '''
)
#Executing the creation of the table
cursor.execute(sql)
#Creating the courses table with an id, name, category, and company id
sql = (
    '''
        CREATE TABLE IF NOT EXISTS courses (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            name TEXT NOT NULL,
            category TEXT NOT NULL,
            company_id INTEGER
        )
    '''
)
#Executing the creation of the table
cursor.execute(sql)
#Inserting a name into the companies table
sql = "INSERT INTO companies (name) VALUES (?)"
#Executing the sql code and providing the values for the database
cursor.execute(sql, ("Mammoth Interactive",))
#Saving the changes to the database
connection.commit()
#Refer to line 35
cursor.execute(sql, ("She Was Lion",))
#Refer to line 37
connection.commit()
#Inserting a name, category, and company id into the courses table
sql = "INSERT INTO courses (name, category, company_id) VALUES (?, ?, ?)"
#Refer to line 35
cursor.execute(sql, ("Hello Coding", "Programming", 1))
#Refer to line 37
connection.commit()
#Checking the number of entries in the companies table
companies = connection.execute("SELECT count(id) FROM companies").fetchone()
#Showing the results in the terminal
print(*companies)
#Checking the number of entries in the courses table
courses = connection.execute("SELECT count(id) FROM courses").fetchone()
#Showing the results in the terminal
print(*courses)
#Selecting the number of id's that match the query based on name
cursor.execute("SELECT id FROM courses WHERE name=? ", ("Hello Coding"))
#Showing the results in the terminal
print(cursor.fetchone())