def make_negative(number):
    return -number if number > 0 else number


def make_negative1(number):
    return -abs(number)

# make_negative_lambda=lambda _:-_ if _>0 else _


print(make_negative_lambda(0))
print(make_negative_lambda(-5))
print(make_negative_lambda(22))
