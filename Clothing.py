"""
Clothing class and subclasses
"""
import mysql.connector

# TODO: turn into ADT
class Clothing:
    """
    Class for clothing

    Instance Attributes
    - clothing_type: I.e. Top, bottom, jacket, shoes, accessories, etc. These will become subclasses
    - colours: A list containing two sublists. The first sublist is for main colours, the second for secondary colours.
    - pattern: I.e. gingham, plaid, floral, animal
    - occasion: I.e. formal, casual, business, athletic-wear etc.
    - weather: weather the clothing is appropriate for. I.e. rain, snow, sun
    - temperature: tuple containing the range of temperatures the clothing is appropriate for (in Celsius).
                   Initialised to set temperatures based on weather.
    """
    clothing_type: str
    colours: list[list[str]]
    pattern: str
    occasion: str
    weather: str
    temperature: tuple[int]

    def __init__(self, clothing_type: str, colours: list[list[str]], occasion: str, weather: str,
                 temperature: tuple[int] = None, pattern: str = None) -> None:
        self.clothing_type = clothing_type
        self.colours = colours
        self.pattern = pattern
        self.occasion = occasion
        self.weather = weather
        self.temperature = temperature

    def add_subtype(self) -> None:
        """
        creates an instance of a subtype
        :return:
        """
        if self.clothing_type == "Top":
            subtype = input("Type of top: ")
            length = input("Length: ")
            Top(self.clothing_type, self.colours, self.occasion, self.weather, subtype, length,
                self.temperature, self.pattern)

        elif self.clothing_type == "Bottoms":
            subtype = input("Type of bottoms: ")
            length = input("Length: ")
            Bottoms(self.clothing_type, self.colours, self.occasion, self.weather, subtype, length,
                self.temperature, self.pattern)

    # def add_to_database(self):
    #     # Establish a connection to the MySQL server
    #     conn = mysql.connector.connect(
    #         host="localhost",  # Replace with your host, usually 'localhost'
    #         user="root",  # Replace with your MySQL username
    #         password="root",  # Replace with your MySQL password
    #         database="clothing_database"  # Replace with your database name
    #     )
    #
    #     # Create a cursor object
    #     cursor = conn.cursor()
    #     cursor.execute(f"SELECT * FROM {self.clothing_type} WHERE subtype = '{item[0]}' AND colours = '{item[1]}' AND pattern is NULL "
    #                    f"AND occasion ='{item[3]}' AND weather = '{item[4]}' AND temperature = '{item[5]}'")


class Top(Clothing):
    """
    Class for tops

    Instance Attributes:
    - subtype: Type of top. I.e.t-shirt, blouse, button-down, corset
    - length: Length of top. I.e. bralette, crop, regular, long
    """
    subtype: str
    length: str

    def __init__(self, clothing_type: str, colours: list[list[str]], occasion: str, weather: str,
                 subtype: str, length: str, temperature: tuple[int] = None, pattern: str = None) -> None:
        super().__init__(clothing_type, colours, occasion, weather, temperature, pattern)
        self.subtype = subtype
        self.length = length

    # TODO: fix this function
    def add_to_database(self, item: list[str]) -> None:
        # Establish a connection to the MySQL server
        conn = mysql.connector.connect(
            host="localhost",  # Replace with your host, usually 'localhost'
            user="root",  # Replace with your MySQL username
            password="root",  # Replace with your MySQL password
            database="clothing_database"  # Replace with your database name
        )

        # Create a cursor object
        cursor = conn.cursor()
        cursor.execute(f"SELECT * FROM Tops WHERE subtype = '{item[0]}' AND colours = '{item[1]}' AND pattern is NULL "
                       f"AND material is NULL AND occasion ='{item[4]}' AND weather = '{item[5]}' "
                       f"AND temperature = '{item[6]}'")

        row = cursor.fetchall()
        if not row:
            cursor.execute("INSERT INTO Tops (subtype, colours, pattern, material, occasion, weather, temperature)"
                           "VALUES (%s, %s, %s, %s, %s, %s, %s)", item)

        cursor.close()
        conn.close()


class Bottoms(Clothing):
    """
    Class for tops

    Instance Attributes:
    - subtype: Type of bottoms. I.e. jeans, trousers, skirt
    - length: Length of bottoms. I.e. mini, midi, 3/4, maxi
    """
    subtype: str
    length: str

    def __init__(self, clothing_type: str, colours: list[list[str]], occasion: str, weather: str,
                 subtype: str, length: str, temperature: tuple[int] = None, pattern: str = None) -> None:
        super().__init__(clothing_type, colours, occasion, weather, temperature, pattern)
        self.subtype = subtype
        self.length = length


class Outerwear(Clothing):
    """
    Class for tops

    Instance Attributes:
    - subtype: Type of outerwear. I.e. jacket, puffer, trench
    - length: Length of outerwear. I.e. crop, regular, midi, maxi
    - season: what season the jacket is most meant for. I.e. spring, summer, fall, winter
    """
    subtype: str
    length: str

    def __init__(self, clothing_type: str, colours: list[list[str]], occasion: str, weather: str,
                 subtype: str, length: str, season: str, temperature: tuple[int] = None, pattern: str = None) -> None:
        super().__init__(clothing_type, colours, occasion, weather, temperature, pattern)
        self.subtype = subtype
        self.length = length
        self.season = season
