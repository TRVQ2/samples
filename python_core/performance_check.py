import sys
import timeit
from timeit import default_timer as timer

# List VS Tuple
'''my_list = [0, 1, 2, "hello", True]
my_tuple = 0, 1, 2, "hello", True

print(sys.getsizeof(my_list), "bytes")
print(sys.getsizeof(my_tuple), "bytes")

print(timeit.timeit(stmt="[0, 1, 2, 'hello', True]", number=1000000))
print(timeit.timeit(stmt="(0, 1, 2, 'hello', True)", number=1000000))'''

# Addition to subarrays
# VS unpacking of subarrays
# VS addition using the same array level
list = [['1', '2', '3'], ['1', '2', '3']]
list1 = [x + ['4'] for x in list]
print(list1)
expr = "[x + ['4'] for x in [['1', '2', '3'], ['1', '2', '3']]]"
print(f"timeit={timeit.timeit(stmt=expr, number=1000000)}\texpr={expr}\n")

list2 = [[*x, '4'] for x in list]
print(list2)
expr = "[[*x, '4'] for x in [['1', '2', '3'], ['1', '2', '3']]]"
print(f"timeit={timeit.timeit(stmt=expr, number=1000000)}\texpr={expr}\n")

'''list3 = list + [['4']]
print(list3)
expr = "[['1', '2', '3'], ['1', '2', '3']] + [['4']]"
print(f"timeit={timeit.timeit(stmt=expr, number=1000000)}\texpr={expr}\n")
'''
print(''' ======= str join VS concatentation ====== ''')
my_list = ['0'] * 1000000
# bad
start = timer()
my_str = ''
for i in my_list:
    my_str += i
stop = timer()
print("time=", stop - start)

# good
start = timer()
my_str = ''.join(my_list)
stop = timer()
print("time=", stop - start)
