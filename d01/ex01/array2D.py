# import numpy as np


def slice_me(family: list, start: int, end: int) -> list:
    # check if same size
    for lst in family:
        if len(lst) != len(family[0]):
            print('Not same size')  # raise error?
            return None

    return family[slice(start, end)]
