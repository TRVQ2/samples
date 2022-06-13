##########
##########
def make_negative(number):
    return -number if number > 0 else number


def make_negative1(number):
    return -abs(number)

# make_negative_lambda=lambda _:-_ if _>0 else _


# print(make_negative(0))
# print(make_negative(-5))
# print(make_negative(22))

##########
##########
def invert(list):
    return [-x for x in list]


# print(invert([1, 2, 3, 4, 5]))  # [-1,-2,-3,-4,-5]
# print(invert([1, -2, 3, -4, 5]))   # [-1,2,-3,4,-5]
# print(invert([]))  # == []


##########
##########
def is_square(n):
    return n == 0 or (n > 0 and (n**.5) % 1 == 0)


print(is_square(9))  # True
print(is_square(3))  # False
print(is_square(0))  # True
print(is_square(-1))  # False
