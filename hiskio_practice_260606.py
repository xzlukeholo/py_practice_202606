# Intermediate Exercise I:
# ---
# 第三題.Write a function called "palindrome"
# that checks if the input string is a palindrome.
# (Search on google if you don't know what a palindrome is.)
# ---
# palindrome("bearaeb"); # true
# palindrome("Whatever revetahW"); # true
# palindrome("Aloha, how are you today?"); # false
# ---
# 答:
def palindrome(text):
    new_word = ""
    for word in text:
        new_word = word + new_word

    if new_word == text:
        return True
    else:
        return False


def palindrome2(text):
    return text[::-1] == text


'''
補充提:寫一個函式 palindrome_life,「生活中常見版 palindrome」。

這版跟剛剛不同：要忽略大小寫、空格、標點符號，只看真正的英文字母和數字。

請寫一個 function：
def palindrome_life(text):
    ...

要求：
忽略大小寫:"A" 和 "a" 要視為一樣
忽略空格:"nurses run" 要視為 "nursesrun"
忽略標點符號:"," "." "!" "?" ":" 這些都不算
只保留：
1.英文字母
2.數字
最後.回傳 True 或 False
print(palindrome_life("A man, a plan, a canal: Panama"))
# True

print(palindrome_life("No lemon, no melon"))
# True

print(palindrome_life("Was it a car or a cat I saw?"))
# True

print(palindrome_life("race a car"))
# False

print(palindrome_life("12321"))
# True

print(palindrome_life("1231"))
# False
'''


def palindrome_life(text):
    new_text = ""
    for character in text:
        if character.isalnum():
            new_text = new_text + character

    new_text = new_text.lower()
    return new_text == new_text[::-1]

# ---
# 第四題.Write a function called "pyramid"
# that takes an integer as input,
# and prints a pyramid in the following pattern:
# ---
# pyramid(1);
# *
# pyramid(2);
#  *
# ***
# pyramid(4);
#    *
#   ***
#  *****
# *******
# ---
# 答:


def pyramid(number):
    bottom_stars = 1 + 2 * (number - 1)

    for i in range(number):
        stars_count = 1 + i * 2
        space_count = bottom_stars - stars_count
        one_side = int(space_count / 2)
        print(" " * one_side + "*" * stars_count + " " * one_side)
