print("multiplication, 5*2=", 5 * 2)
print("power operation, (2*2*2)=", 2 ** 3)
print("create list, [0]*10=", [0]*10)
print("create tuple, (0, 1)*2=", (0, 1)*2)
print("create string, 'AB'*3=", 'AB'*3)


# def foo(a, b, *, **kwargs):  # is just the same as below with unnamed *args
def foo(a, b, *args, **kwargs):
    print("==> foo()")
    print(a, b)
    if len(args) > 0:
        print(*args)
    if len(kwargs) > 0:
        print(str(kwargs))
        print(*kwargs.items())
        print(*kwargs.keys())
        print(*kwargs.values())
        print([f"{key}={kwargs[key]}" for key in kwargs])


foo(1, 2, 3, 4, 5, six=6, seven=7)
tuple = (1, 2, *(3, 4, 5))
dict = {"k1": "v1", "k2": "v2"}
foo(*tuple, **dict)
foo(**{"b": 2, "a": 1, "c": 3})
print("==========")

numbers = (1, 2, 3, 4, 5, 6)
beginning, *middle, last = numbers
print(beginning, middle, last)

dict1 = {"a": 1, "b": 2}
dict2 = {"c": [3, 4, 5], "d": [6, 7, 8]}
dict3 = {**dict1, **dict2}
print(dict3)
