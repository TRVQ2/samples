# function determines the summary of all pairs in input list
def number_of_pairs(gloves):
    count = 0
    for value in list(set(gloves)):
        count += gloves.count(value) // 2
    return count


print(number_of_pairs(["red", "green", "red", "green", "red", "red", "red"]))
