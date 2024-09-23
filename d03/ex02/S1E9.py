from abc import ABC, abstractmethod


class Character(ABC):
    """Character class doc"""
    @abstractmethod
    def __init__(self, first_name, is_alive=True):
        """__init__ doc"""
        self.first_name = first_name
        self.is_alive = is_alive

    # @abstractmethod
    def die(self):
        """die method doc"""
        self.is_alive = False  #check if True ?

class Stark(Character):
    """Stark class doc"""
    def __init__(self, first_name, is_alive=True):
        """Stark init doc"""
        super().__init__(first_name, is_alive)
