# Dictionary: Key-value pairs, Unordered, Mutable
my_dict = {"name": "Ruslan", "age": 40, "city": "Vinnytsia"}
print(my_dict)

my_dict2 = dict(name="Ruslan", age=40, email="trvq2@xyz.com")
print(f"my_dict2={my_dict2}")
my_dict2.update(my_dict)
print(f"my_dict2.update(my_dict) => my_dict2={my_dict2}")
my_tuple = (2, 3)
my_dict2.update({my_tuple: f"{my_tuple[0] * my_tuple[1]}"})
print(my_dict2)


print(
    f"len(my_dict)={len(my_dict)}, is 'name' in?={'name' in my_dict}" +
    f", my_dict['name']={my_dict['name']}" +
    f", is 'Ruslan' in values?={'Ruslan' in my_dict.values()}\n"
)

for k, v in my_dict.items():
    print(k, type(k), '=', v, type(v))

value = my_dict['name']  # my_dict('email') will raise KeyError exception
print(value)
my_dict['email'] = 'trv@trv.com'
print(my_dict)
my_dict['email'] = 'trv@xyz.com'
print(my_dict)

# removal of items
del my_dict["age"]
my_dict.pop("city")
item = my_dict.popitem()
print(f"{my_dict}, popped item={item}")
