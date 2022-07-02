def fib(n=0):
    ''' Get Fibonachi number for n using Tabulation:
        O(n) time; O(n) space
    which is much better than Brute Force strategy without Tabulation:
        O(2 ^ n) time; O(n) space
    '''
    table = [0] * (n + 1)
    table[1] = 1

    end_loop = n - 1
    for i in range(1, end_loop):
        table[i + 1] += table[i]
        table[i + 2] += table[i]
    table[n] += table[end_loop]
    return table[n]


def fib_demo():
    print(fib(6))   # 8
    print(fib(7))   # 13
    print(fib(8))   # 21
    print(fib(50))  # 12586269025


def grid_traveler(n, m):
    ''' Say that you are a traveler on a 2D grid. You begin in the top-left
    corner and your goal is to travel to bottom-right corner. You may only move
    down or right. In how many ways can you travel to the goal on a grid with
    dimensions m * n?

    Function represents Tabulation strategy:
        O(m * n) time; O(n * m) space
    which is much better than Brute Force strategy without Tabulation:
        O(2 ^ (n + m)) time; O(n + m) space
    '''
    if 0 in (m, n):
        return 0
    table = [[0 for i in range(n + 1)] for j in range(m + 1)]
    table[1][1] = 1

    for r in range(1, m + 1):
        for c in range(1, n + 1):
            current = table[r][c]
            if c < n:  # not latest
                table[r][c + 1] += current
            if r < m:  # not latest
                table[r + 1][c] += current
    return table[m][n]


def grid_traveler_demo():
    print(grid_traveler(1, 1))   # 1
    print(grid_traveler(3, 2))   # 3
    print(grid_traveler(3, 3))  # 6
    print(grid_traveler(18, 18))  # 2333606220


def can_sum(target_sum, numbers):
    ''' Write a function that takes in a target_sum and array of numbers as
    arguments. This function should return a boolean indicating whether or not
    it is possible to generate the target_sum using numbers from the array.

    Function represents Tabulation strategy:
        O(m * m * n) time; O(m * m) space
    which is much better than Brute Force strategy without Tabulation:
        O(n ^ m)) time; O(m) space
    '''
    if target_sum < 0:
        return False
    table = [True] + [False] * target_sum

    for i, value in enumerate(table):
        if value:
            for num in [x for x in numbers if i + x <= target_sum]:
                table[i + num] = value
    return table[target_sum]


def how_sum(target_sum, numbers):
    ''' Write a function that takes in a target_sum and array of numbers as
    arguments. This function should return an array containing any combination
    of elements that add up to exactly the target sum. If there are no
    combinations that adds up to the target_sum, then return null

    Function represents Tabulation strategy:
        O(n * m ^ 2) time; O(m ^ 2) space
    which is much better than Brute Force strategy without Tabulation:
        O(n ^ m * m)) time; O(m ^ 2) space
    '''
    if target_sum < 0:
        return None
    table = [[]] + [None] * target_sum

    for i, value in enumerate(table):
        if value is not None:
            for num in [x for x in numbers if i + x <= target_sum]:
                table[i + num] = table[i] + [num]
    return table[target_sum]


def best_sum(target_sum, numbers):
    ''' Write a function that takes in a target_sum and array of numbers as
    arguments. This function should return an array containing the shortest
    combination of elements that add up to exactly the target sum. If there is
    a tie for the shortest combination, you may return any of the shortest.

    Function represents Tabulation strategy:
        O(n * m ^ 2) time; O(m ^ 2) space
    which is much better than Brute Force strategy without Tabulation:
        O(n ^ m * m) time; O(m ^ 2) space
    '''
    if target_sum < 0:
        return None
    table = [[]] + [None] * target_sum

    for i, value in enumerate(table):
        if value is not None:
            for num in [x for x in numbers if i + x <= target_sum]:
                path = table[i] + [num]
                item_to_update = table[i + num]
                if item_to_update is None or len(item_to_update) > len(path):
                    table[i + num] = path
    return table[target_sum]


def sum_demo():
    '''Those three problems below are Dynamic Programming problems'''
    ''' Decision problem::: Can you do it? [yes/no]'''
    print("can_sum=", can_sum(7, [2, 3]))  # True
    print("can_sum=", can_sum(7, [5, 3, 4, 7]))  # True
    print("can_sum=", can_sum(7, [2, 4]))  # False
    print("can_sum=", can_sum(8, [2, 3, 5]))  # True
    print("can_sum=", can_sum(300, [7, 14]))  # False
    ''' Combinatoric problem::: How will you do it? [combinations]'''
    print("how_sum=", how_sum(7, [2, 3]))  # [3, 2, 2]
    print("how_sum=", how_sum(7, [5, 3, 4, 7]))  # [4, 3]
    print("how_sum=", how_sum(7, [2, 4]))  # None
    print("how_sum=", how_sum(8, [2, 3, 5]))  # [2, 2, 2, 2]
    print("how_sum=", how_sum(300, [7, 14]))  # None
    ''' Optimization problem:::
    What is the best way to do it? [the best option]'''
    print("best_sum=", best_sum(7, [2, 3]))  # [3, 2, 2]
    print("best_sum=", best_sum(7, [5, 3, 4, 7]))  # [7]
    print("best_sum=", best_sum(7, [2, 4]))  # None
    print("best_sum=", best_sum(8, [2, 3, 5]))  # [2, 2, 2, 2]
    print("best_sum=", best_sum(300, [7, 14]))  # None


def can_contstruct(target, word_bank):
    ''' Write a function that accepts 'target' string and an array of strings.
    The function should return a boolean indicating wheter or not the 'target'
    can be constructed by concatenating elements of the 'worl_bank' array. We
    can reuse elements of 'worl_bank' as many times as needed.

    Function represents Tabulation strategy:
        O(n * m ^ 2) time; O(m) space
    which is much better than Brute Force strategy without Tabulation:
        O(n ^ m * m) time; O(m ^ 2) space
    '''
    target_length = len(target)
    table = [True] + [False] * target_length

    for i in range(target_length):
        if table[i]:
            for word in word_bank:
                end_matching_part = i + len(word)
                if target[i:end_matching_part] == word:
                    table[end_matching_part] = True

    return table[target_length]


def count_contstruct(target, word_bank):
    ''' Write a function that accepts 'target' string and an array of strings.
    The function should return the number of ways that the 'target' can be
    constructed by concatenating elements of the 'word_bank' array. We
    may reuse elements of 'worl_bank' as many times as needed.

    Function represents Tabulation strategy:
        O(n * m ^ 2) time; O(m) space
    which is much better than Brute Force strategy without Tabulation:
        O(n ^ m * m) time; O(m ^ 2) space
    '''
    target_length = len(target)
    table = [1] + [0] * target_length

    for i in range(target_length):
        for word in word_bank:
            end_matching_part = i + len(word)
            if target[i:end_matching_part] == word:
                table[end_matching_part] += table[i]
        table[i] = None  # to clean up a bit the space usage
    return table[target_length]


def all_contstruct(target, word_bank):
    ''' Write a function that accepts 'target' string and an array of strings.
    The function should return a 2D array containing all of the ways that the
    'target' can be constructed by concatenating elements of the 'word_bank'
    array. Each element of 2D array should represent one combination that
    constructs the target.

    Function represents Tabulation strategy, however, since we need to
    calculate all possible ways, the complexity of that algorithm will remain
    mostly the same as for Brute Force variant:
        ~O(n ^ m) time; ~O(n ^ m) space
    '''
    target_length = len(target)
    # to have something like [[[]], [], [], [], [], [], []]
    table = [[[]]] + [[] for i in range(target_length)]

    for i in range(target_length):
        for word in word_bank:
            end_matching_part = i + len(word)
            if target[i:end_matching_part] == word:
                table[end_matching_part] += [x + [word] for x in table[i]]
        table[i] = None  # to clean up a bit the space usage
    return table[target_length]


def construct_demo():
    ''' Can construct '''
    # print(can_contstruct('abcdef', ['ab', 'abc', 'cd', 'def', 'abcd']))# True
    # print(can_contstruct('skateboard', [
    #  'bo', 'rd', 'ate', 't', 'ska', 'sk', 'boar'
    # ]))   # False
    # print(can_contstruct('enterapotentpot', [
    #  'a', 'p', 'ent', 'enter', 'ot', 'o', 't'
    # ]))   # True
    # print(can_contstruct('eeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeef', [
    #  'e', 'ee', 'eee', 'eeee', 'eeeee', 'eeeeee'
    # ]))   # False
    ''' Count constructs '''
    # print(count_contstruct('purple', ['purp', 'p', 'ur', 'le', 'purpl'])) # 2
    # print(count_contstruct('abcdef', ['ab', 'abc', 'cd', 'def', 'abcd'])) # 1
    # print(count_contstruct('skateboard', [
    #  'bo', 'rd', 'ate', 't', 'ska', 'sk', 'boar'
    # ]))   # 0
    # print(count_contstruct('enterapotentpot', [
    #  'a', 'p', 'ent', 'enter', 'ot', 'o', 't'
    # ]))   # 4
    # print(count_contstruct('eeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeef', [
    #  'e', 'ee', 'eee', 'eeee', 'eeeee', 'eeeeee'
    # ]))   # 0
    ''' All constructs '''
    print(all_contstruct('', ['purp', 'p', 'ur', 'le', 'purpl']))  # [[]]
    print(all_contstruct('purple', ['purp', 'p', 'ur', 'le', 'purpl']))
    # [['purp', 'le'], ['p', 'ur', 'p', 'le']
    print(all_contstruct('abcdef', ['ab', 'abc', 'cd', 'def', 'abcd']))
    # [['abc', 'def']]
    print(all_contstruct('skateboard', [
        'bo', 'rd', 'ate', 't', 'ska', 'sk', 'boar'
    ]))  # []
    print(all_contstruct('enterapotentpot', [
        'a', 'p', 'ent', 'enter', 'ot', 'o', 't'
    ]))
    # '''[
    #  ['enter', 'a', 'p', 'ot', 'ent', 'p', 'ot'],
    #  ['enter', 'a', 'p', 'ot', 'ent', 'p', 'o', 't'],
    #  ['enter', 'a', 'p', 'o', 't', 'ent', 'p', 'ot'],
    #  ['enter', 'a', 'p', 'o', 't', 'ent', 'p', 'o', 't']
    # ]'''
    ''' That one below is commented because there is exponential space usage'''
    # print(all_contstruct('eeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeef', [
    #     'e', 'ee', 'eee', 'eeee', 'eeeee', 'eeeeee'
    # ]))   # []


def main():
    fib_demo()
    grid_traveler_demo()
    sum_demo()
    construct_demo()


if __name__ == "__main__":
    main()
