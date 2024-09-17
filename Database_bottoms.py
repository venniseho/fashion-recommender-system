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
