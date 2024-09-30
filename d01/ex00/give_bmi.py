
def give_bmi(height: list[int | float], weight: list[int | float]):
    """
    Takes 2 lists of ints or floats of the same size
    and returns a list of BMI values.
    """
    try:
        if len(height) != len(weight):
            raise AssertionError('Lists need to be of same size')

        return [w / (h * h) for h, w in zip(height, weight)]
    except Exception as e:
        print(f"ERROR: {str(e)}")
        return None


def apply_limit(bmi: list[int | float], limit: int) -> list[bool]:
    """
    Takes a list of BMI values and a limit, returns a list of booleans
    with True if the value is above the limit.
    """
    try:
        return [item > limit for item in bmi]
    except Exception as e:
        print(f"ERROR: {str(e)}")
        return None
