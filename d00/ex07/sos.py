import sys


def check_string(string):
    """
    Checks if all characters in the string passed as argument
    are alphanumerics or spaces. Raises AssertionError if not.
    """
    for char in string:
        if not (char.isalnum() or char == ' '):
            raise AssertionError(
                "argument must be a string of alphanum and spaces only"
            )


def to_morse(string):
    """
    Converts a string into morse code and returns the new string.
    Handles only alphanum characters and spaces.
    """
    NESTED_MORSE = {
        " ": "/",
        "A": ".-",
        "B": "-...",
        "C": "-.-.",
        "D": "-..",
        "E": ".",
        "F": "..-.",
        "G": "--.",
        "H": "....",
        "I": "..",
        "J": ".---",
        "K": "-.-",
        "L": ".-..",
        "M": "--",
        "N": "-.",
        "O": "---",
        "P": ".--.",
        "Q": "--.-",
        "R": ".-.",
        "S": "...",
        "T": "-",
        "U": "..-",
        "V": "...-",
        "W": ".--",
        "X": "-..-",
        "Y": "-.--",
        "Z": "--..",
        "0": "-----",
        "1": ".----",
        "2": "..---",
        "3": "...--",
        "4": "....-",
        "5": ".....",
        "6": "-....",
        "7": "--...",
        "8": "---..",
        "9": "----."
    }

    morse = ""

    for char in string:
        morse += NESTED_MORSE[char.upper()]

    return morse


def main():
    """Prints out the morse translation of a string passed as argument"""
    try:
        assert len(sys.argv) == 2, "One argument required."

        string = sys.argv[1]
        check_string(string)

        print(to_morse(string))
    except AssertionError as e:
        print(f"AssertionError: {e}")
    except Exception as e:
        print(f"Error: {str(e)}")


if __name__ == "__main__":
    main()
