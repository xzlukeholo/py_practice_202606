# Intermediate Exercise I:
# ---
# 第五題.Write a function called "inversePyramid"
# that draws pyramid upside down.
# ---
# inversePyramid(4);
# *******
#  *****
#   ***
#    *
# ---
# 答:

def inversePyramid(number):
    top_stars = 1 + 2 * (number - 1)
    for row in range(number):
        space = row
        star = top_stars - 2 * row
        for column in range(space):
            print(" ", end="")
        for column in range(star):
            print("*", end="")
        print()


def inversePyramid2(number):
    top_stars = 1 + 2 * (number - 1)
    for row in range(number):
        space = row
        star = top_stars - row * 2
        print(" " * space + "*" * star)


# ---
# 第六題.Given a list of ints,
# return True if the list contains a 3 next to a 3.
# ---
# print(has_33([1, 5, 7, 3, 3])) # True
# print(has_33([])) # False
# print(has_33([4, 3, 2, 1, 0])) # False
# print(has_33([1, 5, 7, 1, 3]))  # True
# ---
# 答:


def has_33(numbers):
    for index, number in enumerate(numbers[:-1]):
        if number == 3:
            if numbers[index + 1] == 3:
                return True
    return False


def has_33_v2(numbers):
    for index in range(len(numbers) - 1):
        if numbers[index] == 3 and numbers[index + 1] == 3:
            return True
    return False


# ---
# 第七題.Write a function that
# check if a list contains a subsequence of 007
# ---
# print(spyGame([1, 2, 4, 0, 3, 0, 7])) # True
# print(spyGame([1, 2, 5, 0, 3, 1, 7])) # False
# ---
# 答:


def spyGame(numbers):
    for index in range(len(numbers) - 2):
        if numbers[index] == 0:
            for index2 in range(index + 1, len(numbers) - 1):
                if numbers[index2] == 0:
                    for index3 in range(index2 + 1, len(numbers)):
                        if numbers[index3] == 7:
                            return True
    return False


def spyGame2(numbers):
    target = [0, 0, 7]
    target_index = 0

    for number in numbers:
        if number == target[target_index]:
            target_index += 1

        if target_index == len(target):
            return True
    return False


print(spyGame2([1, 2, 4, 0, 3, 0, 7]))  # True
print(spyGame2([1, 2, 5, 0, 3, 1, 7]))  # False
print(spyGame2([1, 2, 5, 0, 3, 1, 7, 0, 0]))  # False
