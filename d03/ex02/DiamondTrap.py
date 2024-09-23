from S1E7 import Baratheon, Lannister


class King(Baratheon, Lannister):
    """King doc"""

    def __init__(self, first_name, is_alive=True):
        """King init doc"""
        Baratheon.__init__(self, first_name, is_alive)

    def get_eyes(self):
        """eyes getter"""
        return self.eyes

    def get_hairs(self):
        """hairs getter"""
        return self.hairs
    
    def set_eyes(self, eyes):
        """eyes setter"""
        self.eyes = eyes
    
    def set_hairs(self, hairs):
        """hairs setter"""
        self.hairs = hairs
