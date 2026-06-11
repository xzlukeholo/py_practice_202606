# ---
# 題目 2：contains_sequence
#
# Write a function called "contains_sequence"
# that takes two lists: data and target.
#
# Return True if target appears as a subsequence of data.
#
# A subsequence does not need to be continuous,
# but the order must be correct.
# ---
#
# contains_sequence([1, 2, 4, 0, 3, 0, 7], [0, 0, 7])
# returns True
#
# contains_sequence([1, 2, 5, 0, 3, 1, 7], [0, 0, 7])
# returns False
#
# contains_sequence(["a", "b", "c", "d"], ["b", "d"])
# returns True
#
# contains_sequence(["a", "b", "c"], ["c", "b"])
# returns False
#
# contains_sequence([1, 2, 3], [])
# returns True
# ---


def contains_sequence(data, target):
    target_index = 0

    if not target:
        return True

    if not data:
        return False

    for value in data:
        if value == target[target_index]:
            target_index += 1
        if target_index == len(target):
            return True

    return False


# ---
# 題目 1：nested_count
#
# Write a function called "nested_count"
# that takes a nested list and a target,
# and returns how many times the target appears inside the nested list.
#
# You should solve this with recursion.
# Do not flatten the list first.
# ---
#
# nested_count([1, [2, 1], [3, [1, 4]], 1], 1)
# returns 4
#
# nested_count([[["a"]], "b", ["a", ["c", "a"]]], "a")
# returns 3
#
# nested_count([], 1)
# returns 0
# ---


def nested_count(lst, target):
    result = 0

    for value in lst:
        if isinstance(value, list):
            result += nested_count(value, target)
        elif value == target:
            result += 1
    return result


# ---
# 題目 3：word_frequency
#
# Write a function called "word_frequency"
# that takes a string,
# and returns a dictionary showing how many times each word appears.
#
# Requirements:
# 1. Ignore uppercase/lowercase differences.
# 2. Ignore these punctuation marks: . , ! ? ; :
# 3. Split words by spaces.
# 4. If the input string is empty, return an empty dictionary.
# ---
#
# word_frequency("Hello hello world!")
# returns {"hello": 2, "world": 1}
#
# word_frequency("Python is fun. Python is useful.")
# returns {"python": 2, "is": 2, "fun": 1, "useful": 1}
# ---


def word_frequency(text):
    if not text:
        return {}
    punctuation = ".,!?;:"

    text = text.lower()
    del_punctuation = str.maketrans("", "", punctuation)
    clean_text = text.translate(del_punctuation)

    words = clean_text.split()

    counter_dict = {}
    for item in words:
        if item in counter_dict:
            counter_dict[item] += 1
        else:
            counter_dict[item] = 1
    return counter_dict
