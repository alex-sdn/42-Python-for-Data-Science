import sys

try:
    assert len(sys.argv) < 3, "more than one argument is provided"

    if (len(sys.argv) == 1): exit()

    try:
        num = int(sys.argv[1])
    except:
        raise AssertionError("argument is not an integer")

    if num % 2 == 0:
        print("I'm Even.")
    else:
        print("I'm Odd.")

except AssertionError as e:
    print(f"AssertionError: {e}")
