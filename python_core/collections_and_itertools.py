# collections: Counter, namedtuple, defaultdict, deque
# itertools: product, permutations, combinations, accumulate, groupby
# ... and infinite iterators
from collections import Counter, namedtuple, defaultdict, deque
from itertools import product, permutations, combinations, accumulate
from itertools import combinations_with_replacement, groupby
from itertools import count, cycle, repeat
# import orepator ???

''' Counter '''
a = "aaaaabbbbbbccccccccddd"
my_counter = Counter(a)
print(
    f'my_counter={my_counter}\nmy_counter.items()={my_counter.items()}\n' +
    f'my_counter.keys()={my_counter.keys()}\n' +
    f'my_counter.values()={my_counter.values()}\n' +
    f'list(my_counter.elements())={list(my_counter.elements())}\n' +
    f'my_counter.most_common(1)={my_counter.most_common(1)}\n' +
    f'my_counter.most_common(1)[0][0]={my_counter.most_common(1)[0][0]}\n' +
    f'my_counter.most_common(1)[0][1]={my_counter.most_common(1)[0][1]}\n'
)

''' namedtuple '''
Point = namedtuple('Point', 'x,y')  # will create a class with x and y fields
pt = Point(5, -4)
print(pt, pt.x, pt.y)
print()

''' defaultdict '''
d = defaultdict(list)
d['a'] = 1
d['b'] = 2
print(d, d['a'], d['b'], d['c'])  # for the normal dict there will be KeyError

''' deque '''
d = deque()
d.append(1)
d.append(2)
d.appendleft(3)
print(d)
d.popleft()
print(d)
d.remove(2)
print(d)
d.extend((2, 3, 4, 5))
print(d)
d.extendleft((0, -1, 6))
print(d)
d.rotate(-1)
print(d)
print()

''' itertools.product '''
print('itertools')
a = [1, 2]
b = [3, 4]
print(f'a = [1, 2], b = [3, 4], list(product(a, b))={list(product(a, b))}')
a = [1, 2]
b = [3]
listp = list(product(a, b, repeat=2))
print(f'a={a}, b={b}, list(product(a, b, repeat=2))={listp}')
print()

''' intertools.permutations '''
a = [1, 2, 3]
perm = permutations(a)
print(list(perm))
print(f'list(permutations(a, 2))={list(permutations(a, 2))}')
print()

''' intertools.combinations '''
a = [1, 2, 3]
comb = combinations(a, 2)
comb_wr = combinations_with_replacement(a, 2)
print(list(comb))
print(list(comb_wr))
print()

''' intertools.accumulate '''
a = [1, 2, 3, 4]
print(a)
print(f'list(accumulate(a))={list(accumulate(a))} by default it sums elements')
# acc = accumulate(a, func=operator.mul)
# print(f'list(accumulate(a))={list(acc)} by default it sums elements')
print()

''' intertools.groupby '''
a = "aaaaabbbbbbccccccccddd"
print(a)
groups = groupby(a)
for i, g in groups:
    print(f'i={i}, list(g)={list(g)}')

for i, g in groupby(a, lambda x: x in ('a', 'd')):
    print(f'i={i}, list(g)={list(g)}')
print()
a = [
    {'name': 'Tim', 'age': 25}, {'name': 'Dan', 'age': 25},
    {'name': 'Lisa', 'age': 27}, {'name': 'Claire', 'age': 28},
]
print(a)
for i, g in groupby(a, lambda x: x['age']):
    print(f'i={i}, list(g)={list(g)}')
print()

''' infinite loops: count, cycle, repeat '''
for i in count(10):
    print(i)
    if i == 12:
        break
print()

a = [1, 2, 3]
repeats = 0
for i in cycle(a):
    print(i)
    if i == 3:
        repeats += 1
    if repeats == 2:
        break
print()

for i in repeat(a, 2):
    print(i)

print()
