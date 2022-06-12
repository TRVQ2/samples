##########
# function determines the summary of all pairs in input list
##########
def number_of_pairs_initial_version(gloves):
    count = 0
    for value in list(set(gloves)):
        count += gloves.count(value) // 2
    return count


def number_of_pairs(gloves):
    return sum(gloves.count(color) // 2 for color in set(gloves))


# That one below via lambda function is also working
# number_of_pairs_from_codewars = lambda g: sum(g.count(i)//2for i in set(g))
# print(number_of_pairs(["red", "green", "red", "green", "red", "red", "red"]))


##########
# function determines if the array has a value
##########
def check_initial(seq, elem):
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


print("True: " + str(check([101, 45, 75, 105, 99, 107], 107)))
print("False: " + str(check([78, 117, 110, 99, 104, 117, 107, 115], 8)))
