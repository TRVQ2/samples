# that solution returns [''] in case no delimited strings
def string_to_array(s):
    return s.split() or ['']


# that solution returns empty array if input string has only spaces
def string_to_array1(s):
    return s.split() if s else ['']


# that solution splits to empty strings for each space
def string_to_array2(s):
    return s.split(' ')


# print(string_to_array("         "))
# print(string_to_array1("         "))
# print(string_to_array2("         "))


###########################################################
def count_sheep_mine(n=0):
    result = ""
    for i in range(1, n+1):
        result += str(i) + " sheep..."
    return result


def count_sheep_best(n):
    return ''.join(f"{i} sheep..." for i in range(1, n+1))


print(count_sheep_mine(3))
