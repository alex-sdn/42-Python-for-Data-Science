import sys


def building():
    """
    Counts and displays the number of all types of characters in a string.
    String is passed as argument, or taken from user input if none.
    """
    assert len(sys.argv) < 3, "more than one argument is provided"

    if len(sys.argv) == 1 or not sys.argv[1]:
        arg = input("What is the text to count?\n")
    else:
        arg = sys.argv[1]

    upper = 0
    lower = 0
    punctuation = 0
    spaces = 0
    digits = 0

    for char in arg:
        if char.isupper():
            upper += 1
        elif char.islower():
            lower += 1
        elif char in ".,:;!?-_'\"()[]{}/\\":
            punctuation += 1
        elif char.isspace():
            spaces += 1
        elif char.isdigit():
            digits += 1

    print(f"The text contains {len(arg)} characters:")
    print(f"{upper} upper letters")
    print(f"{lower} lower letters")
    print(f"{punctuation} punctuation marks")
    print(f"{spaces} spaces")
    print(f"{digits} digits")


if __name__ == "__main__":
    try:
        building()
    except AssertionError as e:
        print(f"AssertionError: {e}")
    except Exception as e:
        print(f"Error: {str(e)}")
