from S1E9 import Character


class Baratheon(Character):
    """Representing the Baratheon family"""

    def __init__(self, first_name, is_alive=True):
        """Baratheon init doc"""
        super().__init__(first_name, is_alive)
        self.family_name = 'Baratheon'
        self.eyes = 'brown'
        self.hairs = 'dark'

    def __str__(self):
        """need?"""
        # return super().__str__()
        return f"???"
    
    def __repr__(self):
        # return super().__repr__()
        return f"Vector: ('{self.family_name}', '{self.eyes}', '{self.hairs})'"


class Lannister(Character):
    """Representing the Lannister family"""

    def __init__(self, first_name, is_alive=True):
        """Lannister init doc"""
        super().__init__(first_name, is_alive)
        self.family_name = 'Lannister'
        self.eyes = 'blue'
        self.hairs = 'light'

    def __str__(self):
        """need?"""
        return f"???"

    def __repr__(self):
        """need?"""
        return f"Vector: ('{self.family_name}', '{self.eyes}', '{self.hairs})'"

    @staticmethod
    def create_lannister(first_name, is_alive):
        """create lannister"""
        return Lannister(first_name, is_alive)
