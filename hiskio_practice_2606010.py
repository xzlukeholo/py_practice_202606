# Intermediate Exercises II
# ---
# 第三題.Write a function called "flatten"
# that flattens an list.
# ---
# flatten([1, [[], 2, [0, [1]], [3]], [1, 3, [3], [4, [1]], [2]]]);
# returns [1, 2, 0, 1, 3, 1, 3, 3, 4, 1, 2]
# ---
# 答:
def flatten(lst):
    result = []

    for item in lst:
        if isinstance(item, list):
            result.extend(flatten(item))
        else:
            result.append(item)
    return result


'''
# 題目 1：nested_sum

# 寫一個函式 nested_sum(lst)，計算巢狀 list 裡所有數字的總和。

nested_sum([1, [2, [3]], 4])
# returns 10

nested_sum([1, [[], 2, [0, [1]], [3]], [1, 3, [3], [4, [1]], [2]]])
# returns 21

nested_sum([])
# returns 0

要求

只能用遞迴，不要先 flatten 再 sum()。
'''


def nested_sum(lst):
    total = 0

    for item in lst:
        if isinstance(item, list):
            total += nested_sum(item)
        else:
            total += item
    return total


'''
題目 2：count_items

寫一個函式 count_items(lst)，計算巢狀 list 裡「真正的元素」有幾個。
空 list 不算元素。

count_items([1, [2, [3]], 4])
# returns 4

count_items([1, [[], 2, [0, [1]], [3]], [1, 3, [3], [4, [1]], [2]]])
# returns 11

count_items([[], [[]], [[[]]]])
# returns 0

'''


def count_items(lst):
    total = 0
    for item in lst:
        if not item:
            continue
        elif isinstance(item, list):
            total += count_items(item)
        else:
            total += 1
    return total


# Intermediate Exercises II
# ---
# 題目：Write a function called "max_depth"
# that calculates the maximum depth of a nested list.
#
# 寫一個函式 max_depth(lst)，計算 list 最深有幾層。
#
# 規則：
# 1. 輸入一定是一個 list。
# 2. list 本身算 1 層。
# 3. 如果裡面還有 list，就要往裡面繼續算。
# 4. 空 list [] 的深度是 1。
# 5. 不需要處理非 list 的輸入。
# ---


def max_depth(lst):
    max_depth_found = 1
    for item in lst:
        if isinstance(item, list):
            branch_depth = 1 + max_depth(item)
            if branch_depth > max_depth_found:
                max_depth_found = branch_depth
    return max_depth_found


# ---
# 題目：Write a function called "nested_contains"
# that checks whether a nested list contains a target value.
#
# 寫一個函式 nested_contains(lst, target)
# 檢查巢狀 list 裡面是否包含 target。
#
# 規則：
# 1. 輸入 lst 一定是 list。
# 2. lst 裡面可能有普通元素，也可能有 list。
# 3. 只要任何一層找到 target，就回傳 True。
# 4. 全部找完都沒有，才回傳 False。
# 5. 不能先 flatten 再判斷。
# ---

def nested_contains(lst, target):
    for item in lst:
        if isinstance(item, list):
            result = nested_contains(item, target)
            if result == True:
                return result
        elif item == target:
            return True
    return False


# 測試資料
print(nested_contains([1, [2, [3]], 4], 3))
# expected: True

print(nested_contains([1, [2, [3]], 4], 5))
# expected: False

print(nested_contains([], 1))
# expected: False

print(nested_contains([[], [[], 1], [[[]]]], 1))
# expected: True

print(nested_contains(
    [1, [[], 2, [0, [1]], [3]], [1, 3, [3], [4, [1]], [2]]], 4))
# expected: True

print(nested_contains(
    [1, [[], 2, [0, [1]], [3]], [1, 3, [3], [4, [1]], [999]]], 999))
# expected: False
