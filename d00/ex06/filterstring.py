import sys


def check_string(string):
    """
    Checks if all characters in the string passed as argument
    are alphanumerics or spaces. Raises AssertionError if not.
    """
    for char in string:
        if not (char.isalnum() or char == ' '):
            raise AssertionError(
                "1st argument must be a string of alphanum and spaces only"
            )


def get_word_list(string, num):
    """
    Returns a list of words from the string with len > num.
    """
    return [word for word in string.split() if (lambda x: len(x) > num)(word)]


def main():
    """
    Takes a string and int passed as argument and prints out
    the list of words longer than the int.
    """
    try:
        assert len(sys.argv) == 3, "Two arguments required."

        string = sys.argv[1]
        check_string(string)
        try:
            num = int(sys.argv[2])
        except ValueError:
            raise AssertionError("2nd argument must be an integer.")

        print(get_word_list(string, num))
    except AssertionError as e:
        print(f"AssertionError: {e}")
    except Exception as e:
        print(f"Error: {str(e)}")


if __name__ == "__main__":
    main()
