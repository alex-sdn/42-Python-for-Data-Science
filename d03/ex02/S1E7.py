from S1E9 import Character


class Baratheon(Character):
    """Representing the Baratheon family."""

    def __init__(self, first_name, is_alive=True):
        """
        Initializes a new Baratheon. Calls the Character __init__
        and adds new attributes: family_name, eyes, hairs
        """
        super().__init__(first_name, is_alive)
        self.family_name = 'Baratheon'
        self.eyes = 'brown'
        self.hairs = 'dark'

    def __str__(self):
        """Baratheon __str__ method, returns a string of attributes"""
        return f"{self}"

    def __repr__(self):
        """Baratheon __repr__ method, returns a string of attributes"""
        return f"Vector: ('{self.family_name}', '{self.eyes}', '{self.hairs}')"


class Lannister(Character):
    """Representing the Lannister family."""

    def __init__(self, first_name, is_alive=True):
        """
        Initializes a new Lannister. Calls the Character __init__
        and adds new attributes: family_name, eyes, hairs
        """
        super().__init__(first_name, is_alive)
        self.family_name = 'Lannister'
        self.eyes = 'blue'
        self.hairs = 'light'

    def __str__(self):
        """Lannister __str__ method, returns a string of attributes"""
        return f"{self}"

    def __repr__(self):
        """Lannister __repr__ method, returns a string of attributes"""
        return f"Vector: ('{self.family_name}', '{self.eyes}', '{self.hairs}')"

    @staticmethod
    def create_lannister(first_name, is_alive):
        """Returns a new Lannister instance with the argument attributes"""
        return Lannister(first_name, is_alive)
