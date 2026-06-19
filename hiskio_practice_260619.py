# ============================================================
# 題目 2：隨機複習 - compress_string()
# ============================================================
# 請寫一個函式 compress_string(text)
#
# 功能：
# 把連續重複的字元壓縮成「字元 + 次數」。
#
# 範例：
# compress_string("aaabbc")
# 回傳 "a3b2c1"
#
# compress_string("a")
# 回傳 "a1"
#
# compress_string("")
# 回傳 ""
#
# compress_string("wwwwaaadexxxxxx")
# 回傳 "w4a3d1e1x6"
#
# compress_string("AAaa")
# 回傳 "A2a2"
#
# 注意：
# 1. 大小寫視為不同字元。
# 2. 空字串要回傳空字串。
# 3. 不可以使用 Counter。
# 4. 請用 for 迴圈處理。
#
# 提示：
# - 需要記錄目前正在數的字元 current_char
# - 需要記錄目前字元出現幾次 count
# - 遇到不同字元時，把上一組結果加進 result
# - 迴圈結束後，別忘了把最後一組也加進 result


def compress_string(text):
    if text == "":
        return ""

    result = ""
    current_char = text[0]
    count = 0
    for character in text:
        if current_char == character:
            count += 1
        else:
            result = result + current_char + str(count)
            current_char = character
            count = 1
    result = result + current_char + str(count)
    return result


# 測試區
print(compress_string("aaabbc"))             # a3b2c1
print(compress_string("a"))                  # a1
print(compress_string(""))                   #
print(compress_string("wwwwaaadexxxxxx"))    # w4a3d1e1x6
print(compress_string("AAaa"))               # A2a2

# 我是分隔
# ============================================================
# 題目 1：遞迴複習 - nested_len()
# ============================================================
# 請寫一個函式 nested_len(data)
#
# 功能：
# 計算巢狀 list 裡面「所有非 list 元素」的總數量。
#
# 注意：
# 1. data 可能是普通 list，也可能是多層巢狀 list。
# 2. 只要不是 list，就算一個元素。
# 3. 必須使用「遞迴」完成。
# 4. 不可以使用 flatten 後再 len()。
#
# 範例：
# nested_len([1, 2, 3])
# 回傳 3
#
# nested_len([1, [2, 3], [4, [5]]])
# 回傳 5
#
# nested_len([])
# 回傳 0
#
# nested_len([[[]], [1, [2, [3, 4]]]])
# 回傳 4
#
# nested_len(["a", ["b", ["c"]], 10])
# 回傳 4
#
# 提示：
# - 遇到 list：進去裡面繼續數
# - 遇到非 list：代表找到一個元素，數量 + 1
# - 可以用 isinstance(value, list) 判斷是不是 list


def nested_len(data):
    count = 0
    for item in data:
        if isinstance(item, list):
            count += nested_len(item)
        else:
            count += 1
    return count


# 測試區
print(nested_len([1, 2, 3]))                         # 3
print(nested_len([1, [2, 3], [4, [5]]]))             # 5
print(nested_len([]))                                # 0
print(nested_len([[[]], [1, [2, [3, 4]]]]))          # 4
print(nested_len(["a", ["b", ["c"]], 10]))           # 4
