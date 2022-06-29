def multiply(a, b):
    '''Function Arguments'''
    return a * b


numbers = [3, 5]
print(multiply(*numbers))  # Output: 15

'''Array Literals'''
numbers = [1, 2, 3]
new_numbers = [0, *numbers, 4]
print(new_numbers)  # Output: [0, 1, 2, 3, 4]


'''Object Literals'''
test_obj = {'foo': 'bar'}
print({**test_obj, 'foo2': 'bar2'})  # Output: {'foo': 'bar', 'foo2': 'bar2'}
