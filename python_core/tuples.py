# Tuple: ordered, immutable, allows duplicate elements
print(f'("Ruslan")={("Ruslan")}, f"type(("Ruslan"))={type(("Ruslan"))}')
my_tuple = ("Ruslan",)
print(my_tuple, f"type(my_tuple)={type(my_tuple)}")
my_tuple = ("Ruslan", "Vinnytsia", 40, "Ruslan")
print(my_tuple)

print(
    f"len(my_tuple)={len(my_tuple)}, is 'Ruslan' in?={'Ruslan' in my_tuple}" +
    f", my_tuple[-2]={my_tuple[-2]}\n"
)
for i in my_tuple:
    print(i)

''' functions '''
print(
    f"my_tuple.count('Ruslan')={my_tuple.count('Ruslan')}" +
    # index can generate ValueError: ... x not in my_tuple
    f", my_tuple.index('Vinnytsia')={my_tuple.index('Vinnytsia')}"
)

list = list(my_tuple[:-1:])
print(list)
list.append('Ruslan')
my_tuple = tuple(list)
print(my_tuple)

# unpacking
var1, *var2, var3 = 'TupleItem1', 'TupleItem2', 'TupleItem3', 'TupleItem4'
print(f"var1={var1}, var2={var2}, var3={var3}")
