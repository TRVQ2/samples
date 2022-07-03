# String: ordered, immutable, text representation
my_str = "a" * 5
print(my_str)
my_str = "Hello World"
print(my_str)
my_str = '''Hello
World'''
print(my_str.lower())
my_str = '''Hello \
World'''
print(my_str.upper())
my_str = "Hello World" + "!"
print(my_str)
print(f"{'wor' in my_str} <= 'wor' in my_str???")
print(f"{'Wor' in my_str} <= 'Wor' in my_str???")
print(f"{my_str.startswith('Hello')} <= my_str.startswith('Hello')???")
print(f"{my_str.upper().endswith('D!')} <= my_str.upper().endswith('D!')???")
print(f"{my_str.find('lo')} <= my_str.find('lo')")
print(f"{my_str.find('XXX')} <= my_str.find('XXX')")
print(f"{my_str.count('l')} <= my_str.count('l')")
print()

print(''.join([i for i in my_str]))
print(','.join([f"{i}={my_str[i]}" for i in range(len(my_str))]))
print(''.join([value for i, value in enumerate(my_str[::2])]))

my_str = "    Hello World!   "
print(f"'{my_str}' \t<= my_str")
print(f"{my_str.strip()} \t\t<= my_str.strip()")
print(f"{my_str.strip().rstrip('!')} \t\t<= my_str.strip().rstrip('!')")
print(f'{my_str.replace("   ", "---")} \t<= my_str.replace("   ", "---")')
print(f"{my_str.split()} \t<= my_str.split()")

print("\nFormatting: %, .format(), f\"{...}\" string")
var_str, var_num, var_float = "Tom", 5, 5.55
print("Name is %s %d %.2f" % (var_str, var_num, var_float))
print("Name is {} {:d} {:.2f}".format(var_str, var_num, var_float))
print(f"Name is {var_str} {var_num} {var_float}")
