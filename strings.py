def string_to_array(s):
    '''that solution returns [''] in case no delimited strings'''
    return s.split() or ['']


def string_to_array1(s):
    '''that solution returns empty array if input string has only spaces'''
    return s.split() if s else ['']


def string_to_array2(s):
    '''that solution splits to empty strings for each space'''
    return s.split(' ')


# print(string_to_array("         "))
# print(string_to_array1("         "))
# print(string_to_array2("         "))


def count_sheep_mine(n=0):
    result = ""
    for i in range(1, n+1):
        result += str(i) + " sheep..."
    return result


def count_sheep_best(n):
    return ''.join(f"{i} sheep..." for i in range(1, n+1))


# print(count_sheep_mine(3))


def greet():
    '''Hello world! :)'''
    return "he%sworld!" % ("llo ")


def remove_exclamation_marks(s):
    '''Remove exclamation marks'''
    return s.replace("!", "")


# print(remove_exclamation_marks('Hi! Hello!'))

def findUniqueWords1(str):
    '''Find unique words'''
    output = []
    for x in str.split():
        if x not in output:
            output.append(x)
    return output


def findUniqueWords(str):
    return sorted(set(str.split()))


# def findUniqueWords?(str): - is it possible to use something like self?
#    return [x for x in str.split() if x not in self]


# print(findUniqueWords("This is a test This is a test"))


def likes_long(names):
    n = len(names)
    if n == 0:
        return "no one likes this"
    elif n == 1:
        return f"{names[0]} likes this"
    elif n == 2:
        return f"{names[0]} and {names[1]} like this"
    elif n == 3:
        return f"{names[0]}, {names[1]} and {names[2]} like this"
    elif n > 3:
        return f"{names[0]}, {names[1]} and {n - 2} others like this"


def likes_initial(names):
    n = len(names)
    out = "no one" if n == 0 else names[0]
    if n > 2:
        out += ", " + names[1]
    if n > 1:
        out += " and " + (f"{n - 2} others" if n > 3 else names[n-1])
        out += " like this"
    else:
        out += " likes this"
    return out


def likes_my(names):
    n = len(names)
    return "%s%s%s this" % (
        "no one" if n == 0 else names[0],
        ", " + names[1] if n > 2 else "",
        " and %s like" % ("%s others" % (n - 2) if n > 3 else names[n-1])
        if n > 1 else " likes"
    )


def likes(names):
    n = len(names)
    return {
        0: 'no one likes this',
        1: '{} likes this',
        2: '{} and {} like this',
        3: '{}, {} and {} like this',
        4: '{}, {} and {others} others like this'
    }[min(4, n)].format(*names[:3], others=n-2)


print(likes([]))
print(likes(["Peter"]))
print(likes(["Jacob", "Alex"]))
print(likes(["Max", "John", "Mark"]))
print(likes(["Alex", "Jacob", "Mark", "Max"]))
