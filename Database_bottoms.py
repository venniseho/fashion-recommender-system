"""
Creating a database for bottoms and their categories
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

# cursor.execute('''DROP TABLE IF EXISTS Bottoms''')

cursor.execute('''CREATE TABLE IF NOT EXISTS Bottoms (
                     id INT AUTO_INCREMENT PRIMARY KEY,
                     subtype SET('jeans', 'pants', 'shorts', 'skirt', 'cargos') NOT NULL, 
                     colours SET('black', 'white', 'grey', 'beige', 'tan', 'brown', 'blue', 'green', 'turquoise', 
                                  'orange', 'pink', 'red', 'yellow', 'silver', 'gold') NOT NULL, 
                     pattern SET('animal', 'floral', 'checked', 'pinstripe', 'striped'),
                     material SET('denim', 'linen', 'wool', 'twill', 'leather', 'satin'), 
                     occasion SET('beach', 'casual', 'lounge', 'officewear', 'formal', 'semi-formal', 'party') NOT NULL,
                     weather SET('sunny', 'partly cloudy', 'cloudy', 'rainy', 'drizzle', 'thunderstorm', 
                                  'snowy', 'windy') NOT NULL,
                     temperature TINYINT NOT NULL, 
                     feels_like TINYINT
                 )''')

item = ['corset/bustier', 'white', None, 'casual,party', 'sunny', 20]

# Check if item in table
# use 'is NULL' instead of None
cursor.execute(f"SELECT * FROM Tops WHERE subtype = '{item[0]}' AND colours = '{item[1]}' AND pattern is NULL "
               f"AND occasion ='{item[3]}' AND weather = '{item[4]}' AND temperature = '{item[5]}'")
rows = cursor.fetchall()
# print(rows)

if not rows:
    cursor.execute("INSERT INTO Tops (subtype, colours, pattern, occasion, weather, temperature) "
                   "VALUES (%s, %s, %s, %s, %s, %s)", item)

# Commit the transaction
conn.commit()

# Query the database
cursor.execute("SELECT * FROM Tops")
rows = cursor.fetchall()

# Print the result
for row in rows:
    print(row)

# cursor.execute("SELECT * FROM Tops WHERE subtype = 'corset/bustier' AND colours = 'black'")
# rows = cursor.fetchall()
#
# print(type(rows))
# for row in rows:
#     print(row)

# Close the cursor and connection
cursor.close()
conn.close()
