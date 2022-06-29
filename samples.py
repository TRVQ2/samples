def number_of_pairs_initial_version(gloves):
    '''function determines the summary of all pairs in input list'''
    count = 0
    for value in list(set(gloves)):
        count += gloves.count(value) // 2
    return count


def number_of_pairs(gloves):
    return sum(gloves.count(color) // 2 for color in set(gloves))


# That one below via lambda function is also working
# number_of_pairs_from_codewars = lambda g: sum(g.count(i)//2for i in set(g))
# print(number_of_pairs(["red", "green", "red", "green", "red", "red", "red"]))


def check_initial(seq, elem):
    '''function determines if the array has a value'''
    try:
        str(seq.index(elem))
        return True
    except Exception as e:
        return False


def check_mine(seq, elem):
    for i in seq:
        if i == elem:
            return True
    return False


def check(a, e):
    return e in a


# print("True: " + str(check([101, 45, 75, 105, 99, 107], 107)))
# print("False: " + str(check([78, 117, 110, 99, 104, 117, 107, 115], 8)))

def zero_fuel(distance_to_pump, mpg, fuel_left):
    '''function determines if there is enough fuel'''
    return distance_to_pump <= mpg * fuel_left


# print(f"zero_fuel(50, 25, 2)={zero_fuel(50, 25, 2)}")
# print(f"zero_fuel(150, 25, 2)={zero_fuel(150, 25, 2)}")


def bool_to_word(boolean):
    return "Yes" if boolean else "No"


def open_or_senior_my(data):
    '''function determines if candidate is "Senior" or "Open"'''
    return ["Senior" if x[0] > 54 and x[1] > 7 else "Open" for x in data]


def open_or_senior(d):
    return ["Senior" if age > 54 and hcap > 7 else "Open" for (age, hcap) in d]


'''
input = [[18, 20], [45, 2], [61, 12], [37, 6], [21, 21], [78, 9]]
print(open_or_senior(input))
print(["Open", "Open", "Senior", "Open", "Open", "Senior"])
'''


def sum_two_smallest_numbers_my(numbers):
    '''function returns sum of the lowest two items of integer array'''
    return sum(x for x in sorted(numbers)[slice(2)])


def sum_two_smallest_numbers_best(numbers):
    return sum(sorted(numbers)[:2])


# print(sum_two_smallest_numbers([19, 5, 42, 2, 77]))  # 7
