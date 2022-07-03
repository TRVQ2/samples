# List: ordered, mutable, allows duplicate elements
my_list = ["bannana", "cherry", "apple"]
print(f"my_list={my_list}")
print(
    f"len(my_list)={len(my_list)}, 'apple' in my_list={'apple' in my_list}" +
    f", my_list[-2]={my_list[-2]}\n"
)

my_list.append("lemmon")
my_list.insert(1, "blueberry")
my_list.extend(("blueberry", "orange"))
print(f"added [lemmon, blueberry, blueberry, orange], list={my_list}")
print(
    f"my_list.count('blueberry')={my_list.count('blueberry')}" +
    f", my_list.index('orange')={my_list.index('orange')}"
)

item = my_list.pop()
print(f"popped item={item}, list={my_list}")

my_list.remove("blueberry")  # can generate ValueError: ... x not in list
print(f"removed item=blueberry, list={my_list}\n")

my_list.reverse()
print(f"after reverse my_list={my_list}")

my_list.sort()
print(f"after sort my_list={my_list}")

my_list_ref = my_list
my_list_copy = my_list.copy()
my_list_sorted = sorted(my_list)
# [<initial index> : <last index not included> : <step>] can be negative values
my_list_reverse_slice = my_list[::-2]
my_list_reverse_slice.append('onion')
my_list_reverse_slice.append('cucumber')
print("Fruits are:")
for i in [x for x in my_list_reverse_slice if x not in ('onion', 'cucumber')]:
    print('\t', i)

my_list.clear()
print(
    f"after clear my_list={my_list} the my_list_ref={my_list_ref} also empty" +
    f" other created copies are still ok: \n"
    f"my_list_copy={my_list_copy} \n" +
    f"my_list_sorted={my_list_sorted} \n" +
    f"my_list_reverse_slice=my_list[::-2], ...={my_list_reverse_slice} \n"
)

my_new_list = [0] * 5
print(f"my_new_list = [0] * 5, my_new_list={my_new_list}")
print(f"my_new_list = [0] * 5, my_new_list={my_new_list}")
my_concatenated_list = my_new_list + my_list_copy
print(f"my_concatenated_list={my_concatenated_list}")
print(
    f"my_new_list + []={my_new_list + []}\n" +
    f"my_new_list + [[]]={my_new_list + [[]]}\n"
)

my_list = [0, 1, 2, 3]
my_list2 = [x*x for x in my_list[::-1]]  # list comprehensions
my_list3 = list(map(lambda x: x*2, my_list))
print(f"my_list={my_list},\nmy_list2={my_list2},\nmy_list3={my_list3}")
my_list3 = list(filter(lambda x: x % 2 == 0, my_list))
print(f"list(filter(lambda x: x % 2 == 0, my_list))={my_list3}")
print()

# to have something like [[[]], [], [], [], [], [], []] ... (or 2D arrays)
# use list comprehensions way that creates separate instances
# because [[]] * target_length part will have single reference
list = [[[]]] + [[] for i in range(6)]
print(f"list = [[[]]] + [[] for i in range(6)]={list}")
list[3] += [['1', '2'], ['3', '4']]
print(f"list[3] + [['1', '2'], ['3', '4']]={list[3]}")
print(f"list={list}\n")

list = [[[]]] + [[]] * 6
print(f"list = [[[]]] + [[]] * 6={list}")
list[3] += [['1', '2'], ['3', '4']]
print(f"list[3] + [['1', '2'], ['3', '4']]={list[3]}")
print(f"list={list}")
