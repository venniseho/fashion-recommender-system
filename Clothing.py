"""

"""

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
