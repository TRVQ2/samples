# initial version with "result" in main function and if clause
def chain_sum0(number):
    result = number

    def wrapper(number2=None):
        nonlocal result
        if number2 is None:
            return result
        result += number2
        return wrapper
    return wrapper


# second version with "result" in wrapper and with try clause
def chain_sum1(number):
    def wrapper(number2=None):
        try:
            wrapper.result += int(number2)
        except TypeError:
            return wrapper.result
        return wrapper
    wrapper.result = number
    return wrapper


# third version with dictionary instead try clause
def chain_sum2(number):
    def wrapper(number2=None):
        def inner():
            wrapper.result += number2
            return wrapper
        logic = {
            type(None): lambda: wrapper.result,
            int: inner
        }
        return logic[type(number2)]()
    wrapper.result = number
    return wrapper


print(chain_sum2(5)())  # 5
print(chain_sum2(5)(2)())  # 7
print(chain_sum2(5)(100)(-10)())  # 95


#########################################
# try to get rid of () squares at the end
#########################################
class chain_sum:
    def __init__(self, number):
        self._number = number

    def __call__(self, value=0):
        return chain_sum(self._number + value)

    def __str__(self):
        return str(self._number)


print(chain_sum(5))  # 5
print(chain_sum(5)(2))  # 7
print(chain_sum(5)(100)(-10))  # 95


#########################################
# try to use result of function as an int
#########################################
class chain_sum_int(int):
    def __call__(self, value=0):
        return chain_sum_int(self + value)


print(1 + chain_sum_int(5))  # 6
print(1 + chain_sum_int(5)(2))  # 8
print(1 + chain_sum_int(5)(100)(-10))  # 96
