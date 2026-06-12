# ---
# 練習題：word_frequency 完整版
# ---
# Write a function called "word_frequency"
# that takes a string as input,
# and returns a dictionary showing how many times each word appears.
#
# Rules:
# 1. Words with different capitalization should be treated as the same word.
#    Example:
#    "Python", "python", "PYTHON" are all "python"
#
# 2. Punctuation should not affect the result.
#    Example:
#    "apple, apple!" should be counted as:
#    {"apple": 2}
#
# 3. Use split() to separate words.
#
# 4. Do not use collections.Counter.
#
# 5. Return an empty dictionary if the input is an empty string.
#
# Examples:
# word_frequency("apple banana apple")
# returns {"apple": 2, "banana": 1}
#
# word_frequency("Python python PYTHON")
# returns {"python": 3}
#
# word_frequency("apple, apple! banana.")
# returns {"apple": 2, "banana": 1}
#
# word_frequency("Hello, world! Hello?")
# returns {"hello": 2, "world": 1}
#
# word_frequency("")
# returns {}
# ---

import string


def word_frequency(text):
    if text == "":
        return {}

    result = {}

    text = text.lower()

    punctuations = string.punctuation
    del_punctuations = str.maketrans("", "", punctuations)
    clean_text = text.translate(del_punctuations)
    words = clean_text.split()
    for word in words:
        if word in result:
            result[word] += 1
        else:
            result[word] = 1
    return result


print(word_frequency("apple banana apple"))
# {"apple": 2, "banana": 1}

print(word_frequency("Python python PYTHON"))
# {"python": 3}

print(word_frequency("apple, apple! banana."))
# {"apple": 2, "banana": 1}

print(word_frequency("Hello, world! Hello?"))
# {"hello": 2, "world": 1}

print(word_frequency(""))
# {}


# ---
# 題目 2：compress_string
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
    result = {}
    text = text.lower()

    split_text = text.split()
    for word in split_text:
        if word in result:
            result[word] += 1
        else:
            result[word] = 1
    return result

# ---
# 題目 4：stock_summary
#
# Write a function called "stock_summary"
# that takes a list of stock records.
#
# Each record is a dictionary with:
# "ticker": stock symbol
# "buy": buy price
# "sell": sell price
# "shares": number of shares
#
# Return a dictionary with:
# 1. "total_profit": total profit of all records
# 2. "profitable_count": how many records made money
# 3. "loss_count": how many records lost money
# 4. "best_ticker": ticker with the highest profit
#
# Profit formula:
# (sell - buy) * shares
# ---
#
# stock_summary([
#     {"ticker": "AAPL", "buy": 100, "sell": 120, "shares": 10},
#     {"ticker": "TSLA", "buy": 200, "sell": 180, "shares": 5},
#     {"ticker": "NVDA", "buy": 300, "sell": 330, "shares": 2}
# ])
#
# returns:
# {
#     "total_profit": 160,
#     "profitable_count": 2,
#     "loss_count": 1,
#     "best_ticker": "AAPL"
# }
# ---


def stock_summary(records):
    pass


# Test cases
records1 = [
    {"ticker": "AAPL", "buy": 100, "sell": 120, "shares": 10},  # profit 200
    {"ticker": "TSLA", "buy": 200, "sell": 180, "shares": 5},   # profit -100
    {"ticker": "NVDA", "buy": 300, "sell": 330, "shares": 2}    # profit 60
]

print(stock_summary(records1))
# {
#     "total_profit": 160,
#     "profitable_count": 2,
#     "loss_count": 1,
#     "best_ticker": "AAPL"
# }

records2 = [
    {"ticker": "AMD", "buy": 80, "sell": 70, "shares": 10},     # profit -100
    {"ticker": "GOOG", "buy": 100, "sell": 100, "shares": 3},   # profit 0
    {"ticker": "MSFT", "buy": 50, "sell": 60, "shares": 4}      # profit 40
]

print(stock_summary(records2))
# {
#     "total_profit": -60,
#     "profitable_count": 1,
#     "loss_count": 1,
#     "best_ticker": "MSFT"
# }

print(stock_summary([]))
# {
#     "total_profit": 0,
#     "profitable_count": 0,
#     "loss_count": 0,
#     "best_ticker": None
# }
