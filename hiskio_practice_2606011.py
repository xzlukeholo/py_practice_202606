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


# Practice Notes

# 這次練習完成了三種不同類型的 Python 題目：

# 1. `contains_sequence`
#    - 練習 list 掃描與狀態追蹤。
#    - 重點是使用 `target_index` 追蹤目前要找的目標位置。
#    - 注意空的 `target` 應該回傳 `True`。

# 2. `nested_count`
#    - 練習遞迴處理巢狀 list。
#    - 重點是遇到 list 時，把同一個任務交給函式自己處理，並把結果加總回來。
#    - 這題加強了對「遞迴回傳值」的理解。

# 3. `word_frequency`
#    - 練習字串清洗與 dictionary 統計。
#    - 重點是先轉小寫、移除標點符號，再用 dictionary 統計每個單字出現次數。
#    - 使用 `split()` 而不是 `split(" ")`，可以更好處理多個空白或空字串。

# 整體收穫：
# 這次練習不只是寫出能執行的程式，而是分別練到三種重要問題模型：狀態追蹤、遞迴累加、資料統計。這些能力對後續學習資料分析與更複雜的 Python 題目都有幫助。
