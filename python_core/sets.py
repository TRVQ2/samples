# Set: unordered, mutable, no duplicates
my_set = {1, 2, 3, 4, 5, 1, 1, 2, 2}
print(my_set)
my_set = set('123451122')
print(my_set)  # as you can see each character is presented at once
my_set = set((1, 2, 3, 4, 5, 1, 1, 2, 2))
print(my_set)

my_set.add(10)
my_set.add(11)
my_set.add(12)
try:
    my_set.remove(100)  # generates exception because set doesn't have such key
except KeyError as e:
    print(f"Exception={e}")
# instead we can use
my_set.discard(100)
my_set.remove(10)
item = my_set.pop()
print(f"{my_set}, after adding/removal. Popped item={item}")
print(
    f"'1' in my_set?={'1' in my_set}, '2' in my_set?={'2' in my_set}" +
    f"1 in my_set?={1 in my_set}, 2 in my_set?={2 in my_set}\n"
)

for i in my_set:
    print(i)

my_set.clear()
print(my_set, '\n')

odds = {1, 3, 5, 7, 9}
evens = {0, 2, 4, 6, 8}
primes = {2, 3, 5, 7}
print(odds, "\t\t<= odds")
print(evens, "\t\t<= evens")
print(primes, "\t\t\t<= primes")
print(f"{odds.intersection(evens)} \t\t\t\t<= odds.intersection(evens)")
print(f"{odds.intersection(primes)} \t\t\t<= odds.intersection(primes)")
print(f"{odds.union(evens)} \t<= odds.union(evens)")
print(f"{odds.difference(primes)} \t\t\t\t<= odds.difference(primes)")
print(f"{primes.difference(odds)} \t\t\t\t<= primes.difference(odds)")
print(
    f"{odds.symmetric_difference(primes)}"
    f"\t\t\t<= odds.symmetric_difference(primes)"
)
odds.intersection_update(primes)
print(f"{odds} \t\t\t<= odds after odds.intersection_update(primes)")
primes.intersection_update(evens)
print(f"{primes} \t\t\t\t<= primes after primes.intersection_update(evens)\n")
print(odds, "\t\t\t<= odds")
print(evens, "\t\t<= evens")
print(primes, "\t\t\t\t<= primes")
print(f"{odds.isdisjoint(primes)} \t\t\t\t<= odds.isdisjoint(primes)???")
print(f"{evens.isdisjoint(primes)} \t\t\t\t<= evens.isdisjoint(primes)???")
print(f"{primes.issubset(evens)} \t\t\t\t<= primes.issubset(evens)???")
print(f"{evens.issubset(primes)} \t\t\t\t<= evens.issubset(primes)???")
print(f"{evens.issuperset(primes)} \t\t\t\t<= evens.issuperset(primes)???")
print(f"{primes.issuperset(evens)} \t\t\t\t<= primes.issuperset(evens)???")

odds.update(primes)
odds.update(evens)
print(f"{odds} \t<= odds after odds.update(primes) and odds.update(evens)")
print(evens, "\t\t<= evens")
odds.symmetric_difference_update(evens)
print(f"{odds} \t\t\t<= odds after odds.symmetric_difference_update(evens)")

# frozenset - immutable, can't be modified after creation
f_set = frozenset((1, 2, 3, 4, 5))
print(f_set)
