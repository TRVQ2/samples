num_list = [1, 2, 3, 4, 5]
num_list2 = [6, 7, 8, 9, 10]
print(*num_list, *num_list2)


def num_sum(num1, num2, num3, num4, num5):
    print(num1 + num2 + num3 + num4 + num5)
    return


num_sum(num_list[0], num_list[1], num_list[2], num_list[3], num_list[4])


name = 'Michael'
first, *middle, last = name
print(first, middle, last)


# packing operator
*names, = 'Michael', 'John', 'Nancy', 'Schwar' 'zenegger'
print(names, '\n')


# *args and **kwargs
def names_tuple(*args):
    print(args)
    return


names_tuple('Michael', 'John', 'Nancy')
names_tuple('Jennifer', 'Nancy', 'ano' 'maly')


def names_dict(**kwargs):
    print(kwargs)
    return


names_dict(Jane='Doe')
names_dict(Jane='Doe', John='Smith')


# dictionaries
def dict_sum(a, b, c):
    return a + b + c


num_dict = {'a': 1, 'b': 2, 'c': 3}
print(*num_dict)
print(dict_sum(**num_dict))
num_dict2 = {'d': 4, 'e': 5, 'f': 6}
print({**num_dict, **num_dict2})
