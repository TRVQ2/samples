# Function decorators, Class decorators
# Typical use cases of decorators:
# Timer Decorator - to calculate the execution time
# Debug Decorator
# Check Decorator - if arguments fullfil the requirements
# Register functions as plugins
# Cache the return values
# Add information or update the state

import functools


def print_decorator(func):
    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        print('Start')
        result = func(*args, **kwargs)
        print('End')
        return result  # returns the result of called function
    return wrapper


@print_decorator  # equivalent of "print_name = print_decorator(print_name)"
def print_name():
    print('Alex')


# print_name = print_decorator(print_name)
print_name()


# Another example works as well when wrapper has *args, and **kwargs
@print_decorator
def add5(x):
    print(x + 5)
    return x + 5


print(add5(10), "<= result of function")
print(add5.__name__)  # without @functools.wraps(func) it returns "wrapper"
print()
print(help(add5))  # without @functools.wraps(func) it returns "wrapper" help
print("======== NEXT EXAMPLE:")


# next example shows another type of decorator
def repeat(num_times):
    def repeat_decorator(func):
        @functools.wraps(func)
        def wrapper(*args, **kwargs):
            for _ in range(num_times):
                result = func(*args, **kwargs)
            return result
        return wrapper
    return repeat_decorator


@repeat(num_times=3)
def print_name(name):
    print(f"Hello {name}!")


print_name("Alex")


print("======== NEXT EXAMPLE:")


# next example shows another type of decorator
def debug(func):
    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        args_repr = [repr(a) for a in args]
        kwargs_repr = [f"{k}={v!r}" for k, v in kwargs]
        signature = ", ".join(args_repr + kwargs_repr)
        print(f"Calling {func.__name__}({signature})")
        result = func(*args, *kwargs)
        print(f"{func.__name__!r} returned {result!r}")
        return result
    return wrapper


@debug
@print_decorator
def say_hello(name):
    string = f"Hello {name}!"
    print(string)
    return string


say_hello("Alex")
print("======== NEXT EXAMPLE IS CLASS DECORATOR:")


# next example shows another type of decorator
class CountCalls:

    def __init__(self, func):
        self.func = func
        self.num_calls = 0

    def __call__(self, *args, **kwargs):
        self.num_calls += 1
        print(f"This is executed {self.num_calls} times")
        return self.func(*args, **kwargs)


@repeat(num_times=3)  # 3 times counted here
@CountCalls
@repeat(num_times=3)  # 1 time counted here
def hi():
    print("Hi!:)")


hi()
