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

cursor.execute('''CREATE TABLE IF NOT EXISTS Tops (
                     id INT AUTO_INCREMENT PRIMARY KEY,
                     subtype SET('t-shirt', 'blouse', 'corset/bustier', 'bodysuit', 'print', 'cut-out',
                                 'bandeau', 'crop',
                                 'off-shoulder', 'low cut', 'collared', 'halter', 
                                 'short sleeve', 'long sleeve', 'puff sleeve', 'sleeveless') NOT NULL, 
                     colours SET('black', 'white', 'grey', 'beige', 'tan', 'brown', 'blue', 'green', 'turquoise', 
                                  'orange', 'pink', 'red', 'yellow', 'silver', 'gold') NOT NULL, 
                     pattern SET('animal', 'floral', 'checked', 'pinstripe', 'striped'),
                     occasion SET('beach', 'casual', 'lounge', 'officewear', 'formal', 'semi-formal', 'party') NOT NULL,
                     weather SET('sunny', 'partly cloudy', 'cloudy', 'rainy', 'drizzle', 'thunderstorm', 
                                  'snowy', 'windy') NOT NULL,
                     temperature TINYINT NOT NULL, 
                     feels_like TINYINT
                 )''')
