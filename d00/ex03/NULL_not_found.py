
def NULL_not_found(object: any) -> int:
    if not object:
        if object == None:
            print(f"Nothing: {type(object)}")
        elif isinstance(object, bool):
            print(f"Fake: {type(object)}")
        elif isinstance(object, int):
            print(f"Zero: {type(object)}")
        elif isinstance(object, str):
            print(f"Empty: {type(object)}")
        return 0
    elif isinstance(object, float) and object != object: #NaN not equal to self
        print(f"Cheese: {object} {type(object)}")
        return 0
    else:
        print("Type not found")
        return 1