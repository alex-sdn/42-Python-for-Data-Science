
def callLimit(limit: int):
    """
    Wrapper function that takes as argument an int 'limit'
    Functions defined with this wrapper can be called limit times max
    """
    count = 0

    def callLimiter(function):
        def limit_function(*args: any, **kwds: any):
            """Executes the function if limit not reached"""
            nonlocal count

            if count < limit:
                count += 1
                return function()
            else:
                print(f'Error: {function} call too many times')
        return limit_function

    return callLimiter
