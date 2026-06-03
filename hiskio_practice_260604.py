# Simple Exercise I:
# ---
# 第五題.Write a function called "findSmallerTotal"
# that takes one list of integers and one integer as input,
# and returns the sum of all elements in the list that are smaller than the input integer.
# 答:

def findSmallerTotal(numbers, target):
    total = 0
    for number in numbers:
        if number < target:
            total += number
    return total


# ---
# 第六題.Write a function called "findAllSmall"
# that takes one list of integers and another integer as input,
# and returns a list of integers that contains all elements
# that are smaller than the input integer.
# 答:

# def findAllSmall(numbers, target):
#     result = []
#     for number in numbers:
#         if number < target:
#             result.append(number)
#     return result
# 進階簡潔寫法:
def findAllSmall(numbers, target):
    return [number for number in numbers if number < target]


# ---
# 第七題.Write a function called "summ" that takes one list of numbers,
# and return the sum of all elements in the input list.
# 答:
def summ(numbers):
    total = 0
    for number in numbers:
        total += number
    return total
