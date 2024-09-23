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
                     subtype SET('jeans', 'pants', 'shorts', 'skirt', 'cargos', 'flare') NOT NULL, 
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

item = ['jeans', 'blue', None, 'casual', 'sunny,partly cloudy,cloudy', 17]

# Check if item in table
cursor.execute(f"SELECT * FROM Bottoms WHERE subtype = '{item[0]}' AND colours = '{item[1]}' AND pattern is NULL "
               f"AND occasion ='{item[3]}' AND weather = '{item[4]}' AND temperature = '{item[5]}'")
rows = cursor.fetchall()

if not rows:
    cursor.execute("INSERT INTO Bottoms (subtype, colours, pattern, occasion, weather, temperature) "
                   "VALUES (%s, %s, %s, %s, %s, %s)", item)

cursor.execute("SELECT * FROM Bottoms")
rows = cursor.fetchall()
for row in rows:
    print(row)

# Commit the transaction
conn.commit()

# Close the cursor and connection
cursor.close()
conn.close()
