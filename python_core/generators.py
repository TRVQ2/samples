# Generators are very memory efficient instrument
import sys  # to compare generator VS normal function
# Generator expressions
mygenerator = (i for i in range(10) if i % 2 == 0)
for i in mygenerator:
    print(i)
mygenerator = (i for i in range(10) if i % 2 == 0)
print(f"list(mygenerator)={list(mygenerator)}")


def countdown(num):
    print('Starting...')
    while num > 0:
        yield num
        num -= 1


def my_generator():
    yield 3
    yield 2
    yield 1


g = my_generator()
print(sum(g), '\n')
g = my_generator()
print(next(g))
print(next(g))
print(next(g), '\n')

print(f"sorted(my_generator())={sorted(my_generator())}\n")

cd = countdown(4)
for i in cd:
    print(i)


# ====================
def firstn(n):
    nums = []
    num = 0
    while num < n:
        nums.append(num)
        num += 1
    return nums


# equivalent of the function above is a generator
def firstn_gen(n):
    num = 0
    while num < n:
        yield num
        num += 1


print(sum(firstn(10)))
print(sum(firstn_gen(10)))
# print(sys.getsizeof(firstn(1000000)))
# print(sys.getsizeof(firstn_gen(1000000)), '\n')


def fibonnaci(limit):
    a, b = 0, 1
    print(f"a={a}, b={b}")
    while a < limit:
        yield a
        a, b = b, (a + b)


fib = fibonnaci(30)
for i in fib:
    print(i)
