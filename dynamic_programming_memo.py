def fib(n=0, memo={}):  # set memo is mutable, common for all calls
    ''' Get Fibonachi number for n using Memoization:
        O(n) time; O(n) space
    which is much better than Brute Force strategy without Memoization:
        O(2 ^ n) time; O(n) space
    '''
    if n in memo:
        return memo[n]
    if n <= 2:
        return 1

    memo[n] = fib(n - 1, memo) + fib(n - 2, memo)
    return memo[n]


def fib_demo():
    print(fib(6))   # 8
    print(fib(7))   # 13
    print(fib(8))   # 21
    print(fib(50))  # 12586269025


def grid_traveler(n, m, memo={}):  # set is mutable, common for all calls
    ''' Say that you are a traveler on a 2D grid. You begin in the top-left
    corner and your goal is to travel to bottom-right corner. You may only move
    down or right. In how many ways can you travel to the goal on a grid with
    dimensions m * n?

    Function represents Memoization strategy:
        O(m * n) time; O(n + m) space
    which is much better than Brute Force strategy without Memoization:
        O(2 ^ (n + m)) time; O(n + m) space
    '''
    key = f"{n},{m}"
    if key in memo:
        return memo[key]
    if m == 1 and n == 1:
        return 1
    if 0 in (m, n):
        return 0

    memo[key] = grid_traveler(m - 1, n, memo) + \
        grid_traveler(m, n - 1, memo)
    return memo[key]


def grid_traveler_demo():
    print(grid_traveler(1, 1))   # 1
    print(grid_traveler(3, 2))   # 3
    print(grid_traveler(3, 3))  # 6
    print(grid_traveler(18, 18))  # 2333606220


def can_sum(target_sum, numbers, memo=None):  # need to use memo=None
    ''' Write a function that takes in a target_sum and array of numbers as
    arguments. This function should return a boolean indicating whether or not
    it is possible to generate the target_sum using numbers from the array.

    Function represents Memoization strategy:
        O(m * n) time; O(m) space
    which is much better than Brute Force strategy without Memoization:
        O(n ^ m)) time; O(m) space

    NOTE: The memo input parameter by default is None due to the necessity to
    have it clear for each initial call of func. Otherwise, since it is mutable
    it will be single instance shared for all calls of function with different
    parameters, as result - broken flow.
    '''
    if memo is None:
        memo = {}  # we need to initialize new here
    elif target_sum in memo:
        return memo[target_sum]  # or check if target_sum is there already
    if target_sum == 0:
        return True
    if target_sum < 0:
        return False

    for num in numbers:
        remained = target_sum - num
        if can_sum(remained, numbers, memo):
            memo[target_sum] = True
            return True
    memo[target_sum] = False
    return False


def how_sum(target_sum, numbers, memo=None):  # need to use memo=None
    ''' Write a function that takes in a target_sum and array of numbers as
    arguments. This function should return an array containing any combination
    of elements that add up to exactly the target sum. If there are no
    combinations that adds up to the target_sum, then return null

    Function represents Memoization strategy:
        O(n * m ^ 2) time; O(m ^ 2) space
    which is much better than Brute Force strategy without Memoization:
        O(n ^ m * m)) time; O(m ^ 2) space

    NOTE: The memo input parameter by default is None due to the necessity to
    have it clear for each initial call of func. Otherwise, since it is mutable
    it will be single instance shared for all calls of function with different
    parameters, as result - broken flow.
    '''
    if memo is None:
        memo = {}  # we need to initialize new here
    elif target_sum in memo:
        return memo[target_sum]  # or check if target_sum is there already
    if target_sum == 0:
        return []
    if target_sum < 0:
        return None

    for num in numbers:
        remained = target_sum - num
        remained_result = how_sum(remained, numbers, memo)
        if remained_result is not None:
            # below is faster than: memo[target_sum] = remained_result + [num]
            memo[target_sum] = [*remained_result, num]
            return memo[target_sum]

    memo[target_sum] = None
    return None


def best_sum(target_sum, numbers, memo=None):  # need to use memo=None
    ''' Write a function that takes in a target_sum and array of numbers as
    arguments. This function should return an array containing the shortest
    combination of elements that add up to exactly the target sum. If there is
    a tie for the shortest combination, you may return any of the shortest.

    Function represents Memoization strategy:
        O(n * m ^ 2) time; O(m ^ 2) space
    which is much better than Brute Force strategy without Memoization:
        O(n ^ m * m) time; O(m ^ 2) space

    NOTE: The memo input parameter by default is None due to the necessity to
    have it clear for each initial call of func. Otherwise, since it is mutable
    it will be single instance shared for all calls of function with different
    parameters, as result - broken flow.
    '''
    if memo is None:
        memo = {}  # we need to initialize new here
    elif target_sum in memo:
        return memo[target_sum]  # or check if target_sum is there already
    if target_sum == 0:
        return []
    if target_sum < 0:
        return None

    shortest_combination = None
    for num in numbers:
        remained = target_sum - num
        remained_result = best_sum(remained, numbers, memo)
        if remained_result is not None:
            # below is faster than: new_combination = remained_result + [num]
            new_combination = [*remained_result, num]
            if (shortest_combination is None or
                    len(new_combination) < len(shortest_combination)):
                shortest_combination = new_combination

    memo[target_sum] = shortest_combination
    return shortest_combination


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


def can_contstruct(target, word_bank, memo=None):
    ''' Write a function that accepts 'target' string and an array of strings.
    The function should return a boolean indicating wheter or not the 'target'
    can be constructed by concatenating elements of the 'worl_bank' array. We
    can reuse elements of 'worl_bank' as many times as needed.

    Function represents Memoization strategy:
        O(n * m ^ 2) time; O(m ^ 2) space
    which is much better than Brute Force strategy without Memoization:
        O(n ^ m * m) time; O(m ^ 2) space
    '''
    if memo is None:
        memo = {}  # we need to initialize new here
    elif target in memo:
        return memo[target]
    if target == '':
        return True

    for word in word_bank:
        if target.startswith(word):
            suffix = target.lstrip(word)
            if can_contstruct(suffix, word_bank, memo):
                memo[target] = True
                return True

    memo[target] = False
    return False


def count_contstruct(target, word_bank, memo=None):
    ''' Write a function that accepts 'target' string and an array of strings.
    The function should return the number of ways that the 'target' can be
    constructed by concatenating elements of the 'word_bank' array. We
    may reuse elements of 'worl_bank' as many times as needed.

    Function represents Memoization strategy:
        O(n * m ^ 2) time; O(m ^ 2) space
    which is much better than Brute Force strategy without Memoization:
        O(n ^ m * m) time; O(m ^ 2) space
    '''
    if memo is None:
        memo = {}  # we need to initialize new here
    elif target in memo:
        return memo[target]
    if target == '':
        return 1

    total_count = 0

    for word in word_bank:
        if target.startswith(word):
            ways_num = count_contstruct(target.lstrip(word), word_bank, memo)
            total_count += ways_num

    memo[target] = total_count
    return total_count


def all_contstruct(target, word_bank, memo=None):
    ''' Write a function that accepts 'target' string and an array of strings.
    The function should return a 2D array containing all of the ways that the
    'target' can be constructed by concatenating elements of the 'word_bank'
    array. Each element of 2D array should represent one combination that
    constructs the target.

    Function represents Memoization strategy, however, since we need to
    calculate all possible ways, the complexity of that algorithm will remain
    the same as for Brute Force variant:
        O(n ^ m) time; O(m) space
    '''
    if memo is None:
        memo = {}  # we need to initialize new here
    elif target in memo:
        return memo[target]
    if target == '':
        return [[]]

    result = []

    for word in word_bank:
        if target.startswith(word):
            suffix_ways = all_contstruct(target.lstrip(word), word_bank, memo)
            ''' In the line below I'm adding a word at the beginning of each
            2nd level array, e..g [[..., 1, 2, 3], [..., 5, 6]]. Then
            concatenate it with the result array
            '''
            # bellow is a bit better than: [[word] + x for x in suffix_ways]
            result += [[word, *x] for x in suffix_ways]

    memo[target] = result
    return result


def construct_demo():
    ''' Can construct '''
    # print(can_contstruct('abcdef', ['ab', 'abc', 'cd', 'def', 'abcd']))# True
    # print(can_contstruct('skateboard', [
    #     'bo', 'rd', 'ate', 't', 'ska', 'sk', 'boar'
    # ]))   # False
    # print(can_contstruct('enterapotentpot', [
    #     'a', 'p', 'ent', 'enter', 'ot', 'o', 't'
    # ]))   # True
    # print(can_contstruct('eeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeef', [
    #     'e', 'ee', 'eee', 'eeee', 'eeeee', 'eeeeee'
    # ]))   # False
    ''' Count constructs '''
    # print(count_contstruct('purple', ['purp', 'p', 'ur', 'le', 'purpl'])) # 2
    # print(count_contstruct('abcdef', ['ab', 'abc', 'cd', 'def', 'abcd'])) # 1
    # print(count_contstruct('skateboard', [
    #     'bo', 'rd', 'ate', 't', 'ska', 'sk', 'boar'
    # ]))   # 0
    # print(count_contstruct('enterapotentpot', [
    #     'a', 'p', 'ent', 'enter', 'ot', 'o', 't'
    # ]))   # 4
    # print(count_contstruct('eeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeef', [
    #     'e', 'ee', 'eee', 'eeee', 'eeeee', 'eeeeee'
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
    '''[
        ['enter', 'a', 'p', 'ot', 'ent', 'p', 'ot'],
        ['enter', 'a', 'p', 'ot', 'ent', 'p', 'o', 't'],
        ['enter', 'a', 'p', 'o', 't', 'ent', 'p', 'ot'],
        ['enter', 'a', 'p', 'o', 't', 'ent', 'p', 'o', 't']
    ]'''
    print(all_contstruct('eeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeef', [
        'e', 'ee', 'eee', 'eeee', 'eeeee', 'eeeeee'
    ]))   # []


def main():
    fib_demo()
    grid_traveler_demo()
    sum_demo()
    construct_demo()


if __name__ == "__main__":
    main()
