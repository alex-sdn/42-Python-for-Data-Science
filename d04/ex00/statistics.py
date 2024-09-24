
def get_mean(args):
    """Takes a list of numbers as argument and returns the mean"""
    if args:
        return sum(args) / len(args)
    else:
        return None


def get_median(args):
    """Takes a list of numbers as argument and returns the median"""
    if args:
        sorted_args = sorted(args)
        size = len(args)

        if size % 2 == 0:
            median = (sorted_args[size // 2 - 1] + sorted_args[size // 2]) / 2
        else:
            median = sorted_args[size // 2]
        return median
    else:
        return None


def get_quartile(args):
    """Takes a list of numbers as arg and returns the quartiles in a list"""
    if args:
        sorted_args = sorted(args)
        size = len(args)
        quartiles = []

        if size % 2 == 0:
            lower_half = sorted_args[:size // 2]
            upper_half = sorted_args[size // 2:]
        else:
            lower_half = sorted_args[:size // 2 + 1]
            upper_half = sorted_args[size // 2:]

        quartiles.append(float(get_median(lower_half)))
        quartiles.append(float(get_median(upper_half)))

        return quartiles
    else:
        return None


def get_variance(args):
    """Takes a list of numbers as argument and returns the variance"""
    if args:
        mean = get_mean(args)
        variance = sum((x - mean) ** 2 for x in args) / len(args)

        return variance
    else:
        return None


def get_std(args):
    """Takes a list of numbers as argument and returns the std deviation"""
    if args:
        variance = get_variance(args)
        std = variance ** 0.5

        return std
    else:
        return None


def ft_statistics(*args: any, **kwargs: any) -> None:
    """
    Takes a list of nums as args and the requested calculations as kwargs
    Prints the result or ERROR if no numbers
    """
    for arg in args:
        if not isinstance(arg, (int, float)):
            print('ERROR: Expected numbers in *args')
            exit()

    for value in kwargs.values():
        res = None
        if value == 'mean':
            res = get_mean(args)
        elif value == 'median':
            res = get_median(args)
        elif value == 'quartile':
            res = get_quartile(args)
        elif value == 'std':
            res = get_std(args)
        elif value == 'var':
            res = get_variance(args)
        else:
            continue

        if res:
            print(f"{value} : {res}")
        else:
            print('ERROR')
