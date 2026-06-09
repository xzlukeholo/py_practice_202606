# Intermediate Exercises II
# ---
# 第一題.Write a function called "factorPrime"
# that takes an integer as input,
# and returns the prime factorization of the input.
# ---
# factorPrime(120); # returns "2 x 2 x 2 x 3 x 5"
# ---
# 答:

def factorPrime(number):
    if number < 2:
        return ""
    result_list = []
    re_number = number
    while re_number > 1:
        for n in range(2, re_number+1):
            if n != 2 and n % 2 == 0:
                continue
            if re_number % n == 0:
                re_number = re_number // n
                result_list.append(n)
                break
    result = " x ".join(str(n) for n in result_list)
    return result


def factorPrime2(number):
    if number < 2:
        return ""

    factors = []
    divisor = 2
    remaining = number

    while remaining > 1:
        if remaining % divisor == 0:
            factors.append(divisor)
            remaining = remaining // divisor

        else:
            divisor += 1
    return " x ".join(str(n) for n in factors)


# ---
# 第二題.Write a function called "intersection"
# that takes 2 lists,
# and returns an list of elements
# that are in the intersection of 2 list.
# ---
# intersection([1, 3, 4, 6, 10], [5, 11, 4, 3, 100, 144, 0]);
# # returns [3, 4]
# ---
# 答:
def intersection(list1, list2):
    result = []
    list2_set = set(list2)

    for n in list1:
        if n in list2_set and n not in result:
            result.append(n)
    return result


# ---
# 第三題.Write a function called "flatten"
# that flattens an list.
# ---
# flatten([1, [[], 2, [0, [1]], [3]], [1, 3, [3], [4, [1]], [2]]]);
# returns [1, 2, 0, 1, 3, 1, 3, 3, 4, 1, 2]
# ---
# 答:
def flatten(lst):
    result = []
    remaining = lst.copy()

    while remaining:
        item = remaining.pop(0)

        if isinstance(item, list):
            remaining = item + remaining
        else:
            result.append(item)
    return result


a = flatten([1, [2, 3], 4])

print(a)
