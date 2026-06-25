"""
題目 1:nested_even_sum

請寫一個函式 nested_even_sum(data)

data 是一個可能有多層 list 的巢狀資料，裡面會放整數。
請計算「所有偶數」的總和。

規則：
1. 如果遇到 int:
   - 偶數就加進總和
   - 奇數就忽略

2. 如果遇到 list:
   - 要繼續往裡面找

3. 空 list 不影響結果

4. 不可以使用 flatten() 先攤平後再算，請直接在函式中處理巢狀結構。

範例：
nested_even_sum([1, 2, 3, 4]) 
# 回傳 6

nested_even_sum([1, [2, 3], [4, [5, 6]]])
# 回傳 12

nested_even_sum([[1, 3], [5, [7]]])
# 回傳 0

nested_even_sum([[], [2, [4, []]], 6])
# 回傳 12
"""


def nested_even_sum(data):
    result = 0
    for num in data:
        if isinstance(num, list):
            result += nested_even_sum(num)
        else:
            if num % 2 == 0:
                result += num
            else:
                pass
    return result


print(nested_even_sum([1, 2, 3, 4]))                    # 6
print(nested_even_sum([1, [2, 3], [4, [5, 6]]]))        # 12
print(nested_even_sum([[1, 3], [5, [7]]]))              # 0
print(nested_even_sum([[], [2, [4, []]], 6]))           # 12


"""
題目 2：most_common_char

請寫一個函式 most_common_char(text)

給你一個字串 text，請找出出現次數最多的英文字母。

規則：
1. 不分大小寫：
   "A" 和 "a" 要算同一個字母

2. 只計算英文字母：
   空格、標點符號、數字都忽略

3. 回傳格式是一個 tuple：
   (字母, 次數)

4. 如果有多個字母次數一樣多，回傳最早達到最高次數的那個字母。
   例如：
   "aabb" 裡 a 和 b 都出現 2 次，但 a 比較早出現，所以回傳 ("a", 2)

5. 如果沒有任何英文字母，回傳 None

範例：
most_common_char("Hello World!")
# 回傳 ("l", 3)

most_common_char("Aabb!!!")
# 回傳 ("a", 2)

most_common_char("12345!!!")
# 回傳 None

most_common_char("Python is so cool")
# 回傳 ("o", 4)
"""


def most_common_char(text):
    clean_text = [char.lower() for char in text if char.isalpha()]

    if not clean_text:
        return None

    current_result = {}
    for item in clean_text:
        if item in current_result:
            current_result[item] += 1
        else:
            current_result[item] = 1

    result = max(current_result, key=current_result.get)
    result_time = current_result[result]
    return (result, result_time)


print(most_common_char("Hello World!"))      # ("l", 3)
print(most_common_char("Aabb!!!"))           # ("a", 2)
print(most_common_char("12345!!!"))          # None
print(most_common_char("Python is so cool"))  # ("o", 4)
