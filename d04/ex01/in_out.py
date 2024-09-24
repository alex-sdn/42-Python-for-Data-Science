
def square(x: int | float) -> int | float:
    """Returns the square of argument"""
    return x * x


def pow(x: int | float) -> int | float:
    """Returns the power of argument by itself"""
    return x ** x


def outer(x: int | float, function) -> object:
    """
    Takes a number x and a function()
    Returns an inner function that calls function(x) and updates x with the res
    """
    count = 0

    def inner() -> float:
        nonlocal count, x
        # count += 1  # useless

        x = function(x)

        return x

    return inner
