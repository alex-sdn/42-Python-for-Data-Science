import random
import string
from dataclasses import dataclass, field


def generate_id() -> str:
    """Generates a random 15 char long id"""
    return "".join(random.choices(string.ascii_lowercase, k=15))


@dataclass
class Student:
    """
    Dataclass with predefined variables: active, login, id
    Takes a name and surname as argument
    """
    name: str
    surname: str
    active: bool = field(init=False, default=True)
    login: str = field(init=False)
    id: str = field(init=False, default=generate_id())

    def __post_init__(self):
        """Sets login after __init__ was called and name + surname set"""
        self.login = self.name[0] + self.surname
