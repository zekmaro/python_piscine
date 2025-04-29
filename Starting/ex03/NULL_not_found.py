def NULL_not_found(obj: any) -> int:
    if obj is None:
        print(f"Nothing: {obj} {type(obj)}")
        return 0
    elif type(obj) == float and obj != obj:  # NaN: NaN != NaN is True
        print(f"Cheese: {obj} {type(obj)}")
        return 0
    elif type(obj) == int and obj == 0:
        print(f"Zero: {obj} {type(obj)}")
        return 0
    elif type(obj) == str and obj == '':
        print(f"Empty: {type(obj)}")
        return 0
    elif obj is False:
        print(f"Fake: {obj} {type(obj)}")
        return 0
    else:
        print("Type not Found")
        return 1
