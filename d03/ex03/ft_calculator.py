
class calculator:
    """
    Class with an attribute 'vector' as list of floats
    Can perform basic calculations on the vector after instantiating
    """
    def __init__(self, vector: list) -> None:
        """
        Initializes a new Calculator instance
        Takes a list of numbers as argument
        """
        self.vector = vector

    def __add__(self, object) -> None:
        """Adds object to all numbers in vector"""
        self.vector = [x + object for x in self.vector]
        print(self.vector)

    def __mul__(self, object) -> None:
        """Multiplies all numbers in vector by object"""
        self.vector = [x * object for x in self.vector]
        print(self.vector)

    def __sub__(self, object) -> None:
        """Subtracts object to all numbers in vector"""
        self.vector = [x - object for x in self.vector]
        print(self.vector)

    def __truediv__(self, object) -> None:
        """Divides all numbers in vector by object"""
        if object != 0:
            self.vector = [x / object for x in self.vector]
        print(self.vector)
