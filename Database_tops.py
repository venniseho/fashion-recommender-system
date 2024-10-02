"""
Experimental SQL database.
Currently experimenting with how SQL works.
Will eventually act as a 'virtual closet' for all clothing objects.
"""
"""
Commands to enter into Command Prompt to access the table:
>>> mysql -u root -p 
Enter password: 

>>> SHOW DATABASES;

>>> USE your_database_name;
# enter specific database
>>> SHOW TABLES;
# show tables in that database

>>> SELECT * FROM Tops; 
* is which columns, Tops is the specific table

>>> SELECT * FROM Tops WHERE occasion LIKE 'casual'; 
# filters entries where occasion == casual

>>> SELECT * FROM Tops ORDER BY temperature DESC;
# order the table by descending temperature

>>> DROP TABLE Tops;
# deletes the Tops table

>>> DELETE FROM Tops
# deletes all entries in the table

>>> DELETE FROM Tops WHERE subtype = 'corset/bustier';
# deletes all entries where subtype == 'corset/bustier'
"""

import mysql.connector

# Establish a connection to the MySQL server
conn = mysql.connector.connect(
    host="localhost",  # Replace with your host, usually 'localhost'
    user="root",  # Replace with your MySQL username
    password="root",  # Replace with your MySQL password
    database="clothing_database"  # Replace with your database name
)

# Create a cursor object
cursor = conn.cursor()

cursor.execute('''DROP TABLE IF EXISTS Tops''')

# Execute an SQL command (for example, create a table)
cursor.execute('''CREATE TABLE IF NOT EXISTS Tops (
                     id INT AUTO_INCREMENT PRIMARY KEY,
                     subtype SET('t-shirt', 'blouse', 'corset/bustier', 'bodysuit', 'print', 'cut-out',
                                 'bandeau', 'crop',
                                 'off-shoulder', 'low cut', 'collared', 'halter', 'turtleneck', 
                                 'short sleeve', 'long sleeve', 'puff sleeve', 'sleeveless') NOT NULL, 
                     colours SET('black', 'white', 'grey', 'beige', 'tan', 'brown', 'blue', 'green', 'turquoise', 
                                  'orange', 'pink', 'red', 'yellow', 'silver', 'gold') NOT NULL, 
                     pattern SET('animal', 'floral', 'checked', 'pinstripe', 'striped'),
                     material SET('denim', 'linen', 'wool', 'twill', 'leather', 'satin', 'mesh', 'athletic'), 
                     occasion SET('beach', 'casual', 'lounge', 'officewear', 'formal', 'semi-formal', 'party') NOT NULL,
                     weather SET('sunny', 'partly cloudy', 'cloudy', 'rainy', 'drizzle', 'thunderstorm', 
                                  'snowy', 'windy') NOT NULL,
                     temperature TINYINT NOT NULL, 
                     feels_like TINYINT
                 )''')

# create a function that can filter by type of subtype if that makes sense:
#     NOVELTY: 't-shirt', 'blouse', 'corset/bustier', 'bodysuit', 'print, 'cut-out',
#     LENGTH: 'bandeau', 'crop',
#     NECKLINE: 'off-shoulder', 'low cut', 'collared', 'halter', turtleneck
#     SLEEVE: 'short sleeve', 'long sleeve', 'puff sleeve', 'sleeveless'


# create computer vision thing that can recognise colour hex codes instead of colours as a dropdown set?

# feels like calculated based on weather + temp

# Insert a new record
# cursor.execute("INSERT INTO users (name, age) VALUES (%s, %s)", ('Alice', 25))

item = ['corset/bustier', 'white', None, None, 'casual,party', 'sunny', 20]
item2 = ['turtleneck,bodysuit,long sleeve', 'white', None, None, 'casual', 'snowy,rainy', 15]

items = [item, item2, item]

# Check if item in table. If no, add. else, don't add.
# use 'is NULL' instead of None

# for item in items:
for item in items:
    for i in range(len(item)):
        if item[i] is None:
            item[i] = "NULL"

print(items)

# Create a cursor object
print(f"SELECT * FROM Tops WHERE subtype = '{item[0]}' AND colours = '{item[1]}' "
               f"AND pattern is {item[2]} AND material is {item[3]} AND occasion ='{item[4]}' "
               f"AND weather = '{item[5]}' AND temperature = '{item[6]}'")

cursor.execute(f"SELECT * FROM Tops WHERE subtype = '{item[0]}' AND colours = '{item[1]}' "
               f"AND pattern is {item[2]} AND material is {item[3]} AND occasion ='{item[4]}' "
               f"AND weather = '{item[5]}' AND temperature = '{item[6]}'")

# TODO somehow need to change None to Null when parsing through list...

row = cursor.fetchall()
if not row:
    print(item)
    print("INSERT INTO Tops (subtype, colours, pattern, material, occasion, weather, temperature)"
                   "VALUES (%s, %s, %s, %s, %s, %s, %s)", item)
    cursor.execute("INSERT INTO Tops (subtype, colours, pattern, material, occasion, weather, temperature)"
                   "VALUES (%s, %s, %s, %s, %s, %s, %s)", item)

rows = cursor.fetchall()
for row in rows:
    print(row)

# Close the cursor and connection
cursor.close()
conn.close()
