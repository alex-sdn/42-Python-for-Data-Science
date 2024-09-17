# import numpy as np


def slice_me(family: list, start: int, end: int) -> list:
    # check if same size
    for lst in family:
        if len(lst) != len(family[0]):
            print('Not same size')  # raise error?
            return None

    new = family[slice(start, end)]

    print(f"My shape is : ({len(family)}, {len(family[0])})")
    print(f"My new shape is : ({len(new)}, {len(new[0])})")

    return new
