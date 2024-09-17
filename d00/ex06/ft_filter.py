
def ft_filter(function, iterable):
    """
    filter(function or None, iterable) --> filter object
    Return an iterator yielding items of iterable for which function(item)
    is true. If function is None, return the items that are true.
    """
    if function:
        return (x for x in iterable if function(x))
    return (x for x in iterable if x)

# def iseven(num):
#     if num % 2 == 0:
#         return True
#     return False


# if __name__ == "__main__":
#     test = [1, 4, 5, 7, 8, 120]

#     print(list(filter(None, test)))
#     print(list(ft_filter(None, test)))
