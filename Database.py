"""
Experimental SQL database.
Currently experimenting with how SQL works.
Will eventually act as a "virtual closet" for all clothing objects.
"""
import mysql.connector

# Establish a connection to the MySQL server
conn = mysql.connector.connect(
    host="localhost",               # Replace with your host, usually 'localhost'
    user="Vennise",                 # Replace with your MySQL username
    password="Angelwings4444$",     # Replace with your MySQL password
    # database="yourdatabase"         # Replace with your database name (optional) # problem area, to fix
)

# Create a cursor object
cursor = conn.cursor()

# Execute an SQL command (for example, create a table)
cursor.execute('''CREATE TABLE IF NOT EXISTS users (
                     id INT AUTO_INCREMENT PRIMARY KEY,
                     name VARCHAR(255),
                     age INT
                 )''')

# Insert a new record
cursor.execute("INSERT INTO users (name, age) VALUES (%s, %s)", ('Alice', 25))

# Commit the transaction
conn.commit()

# Query the database
cursor.execute("SELECT * FROM users")
rows = cursor.fetchall()

# Print the result
for row in rows:
    print(row)

# Close the cursor and connection
cursor.close()
conn.close()
