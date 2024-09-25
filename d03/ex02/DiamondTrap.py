from S1E7 import Baratheon, Lannister


class King(Baratheon, Lannister):
    """King class that inherits from Baratheon and Lannister"""

    def __init__(self, first_name, is_alive=True):
        """Initializes a new King with the Baratheon __init__"""
        Baratheon.__init__(self, first_name, is_alive)

    def get_eyes(self):
        """Getter for eyes attribute"""
        return self.eyes

    def get_hairs(self):
        """Getter for hairs attribute"""
        return self.hairs

    def set_eyes(self, eyes):
        """Setter for eyes attribute"""
        self.eyes = eyes

    def set_hairs(self, hairs):
        """Setter for hairs attribute"""
        self.hairs = hairs
