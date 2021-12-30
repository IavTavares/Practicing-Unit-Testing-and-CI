def string_to_float(string):
    num=float(string)
    return num

def string_to_int(string):
    try:
        float(string)
    except ValueError:
        print("Variable is not convertible to a number")
    except TypeError:
        print("Wrong Type")
    else:
        num=float(string)
        num=int(num)
        return num

def string_to_int_2(string):
    try:
        float(string)
    except ValueError:
        raise ValueError("Variable is not convertible to a number")
    except TypeError:
        raise TypeError("Wrong Type")
    else:
        num=float(string)
        num=int(num)
        return num