# Simple Exercise II:
# ---
# 第一題.Write a function called "stars"
# which prints out layers of stars in the following pattern:
# stars(1);
# *
# stars(4);
# *
# **
# ***
# ****
# 答:


def stars(number):
    for star_num in range(number):
        print("*" * (star_num + 1))

# ---
# 第二題.Write a function called "stars2"
# which prints out layers of stars in the following pattern:
# stars2(1)
# *
# stars2(2)
# *
# **
# *
# stars2(4)
# *
# **
# ***
# ****
# ***
# **
# *
# 答:


def stars2(number):
    for star_num in range(number):
        print("*" * (star_num + 1))

    for star_num2 in range(number - 1, 0, -1):
        print("*" * star_num2)


# ---
# 第三題.Write a function called "table"
# which takes an input n,
# and prints out n x 1 to n x 9
# 答:


def table(n):
    for num in range(1, 10):
        print(f"{n} x {num} =", n * num)


# ---
# 第四題.Write a function called "table9to9"
# that prints out the multiplication table:
# table9to9();
# 1 x 1 = 1
# 1 x 2 = 2
# 1 x 3 = 3
# ...
# 1 x 9 = 9
# 2 x 1 = 2
# 2 x 2 = 4
# ...
# 9 x 9 = 81
# 答:
def table9to9():
    for num1 in range(1, 10):
        for num2 in range(1, 10):
            print(f"{num1} x {num2} =", num1 * num2)

# ---
# 第五題.Write a function called "swap" that takes a string as input,
# and returns a new string with lowercase changed to uppercase,
# uppercase changed to lowercase.
# 答:


def swap(word):
    result = ""
    for w in word:
        if w.isupper():
            w = w.lower()
            result = result + w
        else:
            w = w.upper()
            result = result + w
    return result

# ---
# 第六題.Write a function called "findMin"
# which takes an list as input,
# and returns the minimum element in the input list.


def findMin(data):
    if not data:
        return "undefined"

    min_num = data[0]
    for number in data:
        if min_num > number:
            min_num = number
    return min_num
