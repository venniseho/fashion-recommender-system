"""
Experimental SQL database.
Currently experimenting with how SQL works.
Will eventually act as a "virtual closet" for all clothing objects.
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

# Execute an SQL command (for example, create a table)
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

# create a function that can filter by type of subtype if that makes sense:
#     NOVELTY: 't-shirt', 'blouse', 'corset/bustier', 'bodysuit', 'print, 'cut-out',
#     LENGTH: 'bandeau', 'crop',
#     NECKLINE: 'off-shoulder', 'low cut', 'collared', 'halter', turtleneck
#     SLEEVE: 'short sleeve', 'long sleeve', 'puff sleeve', 'sleeveless'


# create computer vision thing that can recognise colour hex codes instead of colours as a dropdown set?

# feels like calculated based on weather + temp

# Insert a new record
# cursor.execute("INSERT INTO users (name, age) VALUES (%s, %s)", ('Alice', 25))
cursor.execute("INSERT INTO Tops (subtype, colours, pattern, occasion, weather, temperature) "
               "VALUES (%s, %s, %s, %s, %s, %s)", ('corset/bustier', 'white', None, 'casual,party', 'sunny', 20))

# Commit the transaction
# conn.commit()
#
# # Query the database
# cursor.execute("SELECT * FROM users")
# rows = cursor.fetchall()
#
# # Print the result
# for row in rows:
#     print(row)

# Close the cursor and connection
cursor.close()
conn.close()
