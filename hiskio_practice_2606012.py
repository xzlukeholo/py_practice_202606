# ---
# 題目 1：compress_string
#
# Write a function called "compress_string"
# that takes a string and compresses consecutive repeated characters.
#
# Each group should become:
# character + count
#
# ---
# compress_string("aaabbc")
# returns "a3b2c1"
#
# compress_string("abcd")
# returns "a1b1c1d1"
#
# compress_string("aabbbaa")
# returns "a2b3a2"
#
# compress_string("")
# returns ""
# ---


def compress_string(text):
    if not text:
        return ""

    result = ""
    current_char = text[0]
    counter = 1
    for character in text[1:]:
        if character == current_char:
            counter += 1
        else:
            result = result + current_char + str(counter)
            current_char = character
            counter = 1
    result = result + current_char + str(counter)
    return result


# ---
# 練習題：word_frequency
# ---
# Write a function called "word_frequency"
# that takes a string as input,
# and returns a dictionary showing how many times each word appears.
#
# Rules:
# 1. Words with different capitalization should be treated as the same word.
#    Example: "Python", "python", "PYTHON" are all "python"
# 2. Use split() to separate words.
# 3. Do not use collections.Counter.
# 4. For now, you do not need to handle punctuation.
#
# Examples:
# word_frequency("apple banana apple")
# returns {"apple": 2, "banana": 1}
#
# word_frequency("Python python PYTHON")
# returns {"python": 3}
#
# word_frequency("")
# returns {}
# ---


def word_frequency(text):
    text = text.lower()

    split_text = text.split()
    print(split_text)


print(word_frequency("apple banana apple"))
# {"apple": 2, "banana": 1}

print(word_frequency("Python python PYTHON"))
# {"python": 3}

print(word_frequency(""))
# {}
