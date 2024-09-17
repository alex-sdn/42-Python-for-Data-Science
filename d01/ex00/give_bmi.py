import numpy # ???


def give_bmi(height: list[int | float], weight: list[int | float]) -> list[int | float]:
    if len(height) != len(weight):
        print("Lists need to be of same size")  # AssertError ?
        return None
    # check if both int / float ?

    return [w / (h * h) for h, w in zip(height, weight)]


def apply_limit(bmi: list[int | float], limit: int) -> list[bool]:
    # error check ?

    return [item > limit for item in bmi]
