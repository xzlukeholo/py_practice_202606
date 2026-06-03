# Simple Exercise I:
# ---
# 第一題.Write a function called "printMany" that prints out integers 1, 2, 3, ..., 100.
# 答:
def printMany():
    for number in range(1, 101):
        print(number)

# ---
# 第二題.Write a function called "printEvery3" that prints out integers 1, 4, 7, 10, ..., 88.
# 答:


def printEvery3():
    for number in range(1, 89, 3):
        print(number)


# ---
# 第三題.Write a function called "position" that returns a tuple of the first uppercase letter
# and its index location. If not found, returns - 1.
# 答:
def position(text):
    for index, char in enumerate(text):
        if char.isupper():
            return (char, index)
    return -1

# ---
# 第四題.Write a function called "findSmallCount"
# that takes one list of integers and one integer as input,
# and returns an integer indicating how many elements in the list is smaller than the input integer.
# 答:


def findSmallCount(int_list, target):
    count = 0
    for integer in int_list:
        if integer < target:
            count += 1
    return count
