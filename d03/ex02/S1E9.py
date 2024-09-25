from abc import ABC, abstractmethod


class Character(ABC):
    """
    Abstract class for a Character
    Attributes: first_name (str), is_alive (bool)
    """
    @abstractmethod
    def __init__(self, first_name, is_alive=True):
        """
        Initializes a new character with the first_name passed as arg
        is_alive is optional and set to True by default
        """
        self.first_name = first_name
        self.is_alive = is_alive

    def die(self):
        """Sets the Character's is_alive status to False"""
        self.is_alive = False


class Stark(Character):
    """Stark class that inherits from Character"""
    def __init__(self, first_name, is_alive=True):
        """Initializes a new Stark by calling the Character __init__"""
        super().__init__(first_name, is_alive)
