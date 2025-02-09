
def slice_me(family: list, start: int, end: int) -> list:
    """
    Takes a 2D array, prints its shape, and returns a
    truncated version based on the start and end arguments.
    """
    try:
        assert isinstance(family, list), 'Expected a list'
        for lst in family:
            assert len(lst) == len(family[0]), 'Not a 2D array'

        new = family[start:end]

        print(f"My shape is : ({len(family)}, {len(family[0])})")
        print(f"My new shape is : ({len(new)}, {len(new[0])})")

        return new
    except Exception as e:
        print(f"ERROR: {str(e)}")
        return None
