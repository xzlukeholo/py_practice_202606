"# py_practice_202606"

## 這個月練習的小題目會集中在這裡,今天的題目是第一部份的:

'''

# A. 函式與 return 基礎

1. 取得股票代號

請寫一個函式：

要求：回傳股票的 `"ticker"`。

print(get_ticker(stocks[0]))
預期輸出：
NVDA

---

2. 判斷股票是否上漲

請寫一個函式：
def is_positive(stock):
...

要求：如果 `return_pct` 大於 0，回傳 `True`，否則回傳 `False`。

print(is_positive(stocks[0]))
print(is_positive(stocks[1]))
預期輸出：
True
False

---

3. 找出第一檔上漲的股票

請寫一個函式：
def find_first_positive(stocks):
...

要求：
從清單中找出第一檔 `return_pct > 0` 的股票。
找到後回傳那一整個 dictionary。
如果全部都沒有上漲，回傳 `None`。

print(find_first_positive(stocks))
預期結果：
{'ticker': 'NVDA', 'price': 1200, 'return_pct': 3.2, 'volume': 35}

---

4. 找出所有上漲股票

請寫一個函式：
def find_all_positive(stocks):

要求：回傳所有 `return_pct > 0` 的股票。回傳型態要是 list。

測試：
print(find_all_positive(stocks))

預期會包含：
NVDA
MU
PLTR

---

'''

## 第二天的練習題目:

'''
B. 參數、預設參數、命名規則

## 用最低漲跌幅篩選股票

情境：
投資人想設定一個「最低漲跌幅門檻」，只看表現達到門檻以上的股票。
要求：請寫一個函式

- 函式要根據 `min_return` 篩選股票。
- 回傳符合條件的股票資料。
- 回傳型態必須是 list。
- list 裡面放的是完整的股票 dictionary，不是只有股票代號。
- 門檻值本身也算符合條件。

---

## 計算平均漲跌幅

情境：
投資人想知道整份股票觀察清單的平均漲跌幅。
要求：請寫一個函式

- 根據所有股票的 `return_pct` 計算平均值。
- 回傳平均漲跌幅。
- 請注意空清單的情況。
- 如果傳入空清單，請回傳 `0`。

---

## 建立股票摘要字串：練 return

情境：
系統需要把單一股票資料轉成容易閱讀的摘要文字，之後可能拿去印出、寫進報告、存成檔案。

要求：請寫一個函式

- 函式負責「產生摘要字串」。
- 不要在函式裡面直接 `print()`。
- 請用 `return` 把摘要字串交出去。
- 摘要中要包含股票代號、價格、漲跌幅、成交量。

測試：
summary = build_stock_summary(stocks[0])
print(summary)

預期輸出：
NVDA | Price: 1200 | Return: 3.2% | Volume: 35

---

## 印出全部需要的股票摘要：練 print

def print_stock_summary(stock):

情境：
前一題已經有一個函式可以產生股票摘要。現在需要另一個函式，專門負責把摘要顯示在畫面上。
要求：請寫一個函式

- 可以重複利用第 7 題的 `build_stock_summary(stock)`。
- 這個函式的主要任務是顯示資料。
- 不需要特別回傳資料。
  '''

---

## Simple Exercise I:

# ---

第一題.Write a function called "printMany" that prints out integers 1, 2, 3, ..., 100.

答:
def printMany():
for number in range(1, 101):
print(number)

# ---

第二題.Write a function called "printEvery3" that prints out integers 1, 4, 7, 10, ..., 88.

答:
def printEvery3():
for number in range(1, 89, 3):
print(number)

# ---

第三題.Write a function called "position" that returns a tuple of the first uppercase letter
and its index location. If not found, returns - 1.

答:
def position(text):
for index, char in enumerate(text):
if char.isupper():
return (char, index)
return -1

# ---

第四題.Write a function called "findSmallCount"
that takes one list of integers and one integer as input,
and returns an integer indicating how many elements in the list is smaller than the input integer.

答:
def findSmallCount(int_list, target):
count = 0
for integer in int_list:
if integer < target:
count += 1
return count

# ---

第五題.Write a function called "findSmallerTotal"
that takes one list of integers and one integer as input,
and returns the sum of all elements in the list that are smaller than the input integer.

答:
def findSmallerTotal(numbers, target):
total = 0
for number in numbers:
if number < target:
total += number
return total

(以下是被建議的,已經修正)

# 強烈建議改:sum_int → total

sum_int 有兩個小問題：

第一，它把型態 int 寫進名字裡，不太 Pythonic。

第二，雖然它沒有直接覆蓋內建函式 sum，但靠近 sum 這個名字，讀起來還是容易讓人想到內建函式。

更自然的是： total

# 建議改:int_list → numbers

在 Python 裡通常不會把資料型態寫進變數名稱

# 可考慮:number → number 或 num

# ---

第五題.Write a function called "findSmallerTotal"
that takes one list of integers and one integer as input,
and returns the sum of all elements in the list that are smaller than the input integer.
答:

def findSmallerTotal(numbers, target):
total = 0
for number in numbers:
if number < target:
total += number
return total

# ---

第六題.Write a function called "findAllSmall"
that takes one list of integers and another integer as input,
and returns a list of integers that contains all elements that are smaller than the input integer.

答:
def findAllSmall(numbers, target):

result = []

for number in numbers:

if number < target:

result.append(number)

return result

# 進階簡潔寫法:

def findAllSmall(numbers, target):
return [number for number in numbers if number < target]

# ---

第七題.Write a function called "summ" that takes one list of numbers,
and return the sum of all elements in the input list.

答:
def summ(numbers):
total = 0
for number in numbers:
total += number
return total

### Simple Exercise II - Python Loop Practice

這次練習主要複習 Python 的 `for loop`、`range()`、巢狀迴圈、字串大小寫轉換，以及用迴圈尋找 list 中的最小值。

## 練習內容

本次完成的題目包含：

1. 印出遞增星星圖案
2. 印出先遞增再遞減的星星圖案
3. 印出指定數字的九九乘法表
4. 印出完整 1 到 9 的九九乘法表
5. 將字串中的大寫轉小寫、小寫轉大寫
6. 找出 list 中的最小值

## 學到的重點

這次練習讓我更熟悉 `range(start, stop, step)` 的使用方式，尤其是在處理遞減迴圈時，例如：

```python
range(number - 1, 0, -1)
```

也透過九九乘法表練習了巢狀迴圈，理解外層迴圈與內層迴圈各自負責的邏輯。

在字串處理的題目中，我練習了：

```python
isupper()
lower()
upper()
```

並理解如何用 `if-else` 判斷每個字元應該轉成大寫或小寫。

最後在 `findMin` 題目中，我練習不用內建的 `min()`，而是手動用迴圈比較每個元素，理解尋找最小值的基本演算法。

## 心得

這次的題目整體比前面的練習更接近實際的程式邏輯訓練。星星圖案和九九乘法表讓我更熟悉迴圈的控制方式，而 `swap` 和 `findMin` 則讓我練習如何用條件判斷處理資料。

我發現自己已經能寫出正確的基礎邏輯，但還需要繼續練習讓程式碼更簡潔、更 Pythonic。例如在字串轉換時，可以減少重複的程式碼；在處理空 list 時，也要注意 Python 比較常見的寫法是回傳 `None` 或拋出錯誤，而不是使用 `"undefined"`。

這次練習的收穫是：不只是把題目寫對，也開始學會思考程式碼的可讀性、命名方式，以及特殊情況的處理。

---

# Secret Number Guessing Game

這是一個使用 Python 製作的終端機猜數字遊戲。
玩家需要在有限次數內猜出 1 到 1000 之間的秘密數字。

## 功能特色

- 隨機產生 1 到 1000 之間的答案
- 玩家共有 10 次猜測機會
- 會根據玩家輸入提示「太大」或「太小」
- 會動態縮小可能範圍
- 支援輸入 `q` 離開遊戲
- 支援遊戲結束後重新開始
- 使用 `try / except` 處理非整數輸入
- 使用 ANSI escape codes 顯示彩色文字

## 練習重點

這個專案主要練習了以下 Python 基礎觀念：

- `while True` 迴圈控制
- `if / elif / else` 條件判斷
- `try / except` 錯誤處理
- `int()` 型別轉換
- `random.randint()` 隨機數字
- 函式拆分與程式結構整理
- `return` 與 `break` 的使用差異
- 使用變數追蹤遊戲狀態，例如答案、範圍、猜測次數

## 程式結構

程式被拆分成幾個主要函式：

- `reset()`：重設答案、範圍與猜測次數
- `check_guess_range()`：取得並驗證玩家輸入
- `show_remaining_attempts()`：顯示目前可能範圍與剩餘次數
- `play_round()`：控制一整局遊戲流程
- `try_again()`：詢問玩家是否再玩一次
- `exit_game()`：結束遊戲

## 如何執行

請先確認電腦已安裝 Python。

在終端機中執行：

```bash
python main.py
```

如果檔案名稱不是 `main.py`，請改成實際的 Python 檔案名稱。

## 學習心得

這個練習讓我更熟悉如何設計一個完整的互動式小程式。
一開始我把多層 `while True` 全部寫在主程式中，雖然可以執行，但結構比較集中。後來將輸入驗證、單局遊戲流程、重新開始邏輯拆成不同函式，讓主程式變得更清楚，也更容易維護。

這次練習也讓我理解到，函式拆分不是越多越好，而是要讓每個函式有明確責任。當程式功能變多時，良好的結構會讓程式更容易閱讀與修改。

## 2026/6/11 Practice Notes

這次練習完成了三種不同類型的 Python 題目：

1. `contains_sequence`
   - 練習 list 掃描與狀態追蹤。
   - 重點是使用 `target_index` 追蹤目前要找的目標位置。
   - 注意空的 `target` 應該回傳 `True`。

2. `nested_count`
   - 練習遞迴處理巢狀 list。
   - 重點是遇到 list 時，把同一個任務交給函式自己處理，並把結果加總回來。
   - 這題加強了對「遞迴回傳值」的理解。

3. `word_frequency`
   - 練習字串清洗與 dictionary 統計。
   - 重點是先轉小寫、移除標點符號，再用 dictionary 統計每個單字出現次數。
   - 使用 `split()` 而不是 `split(" ")`，可以更好處理多個空白或空字串。

整體收穫：
這次練習不只是寫出能執行的程式，而是分別練到三種重要問題模型：狀態追蹤、遞迴累加、資料統計。這些能力對後續學習資料分析與更複雜的 Python 題目都有幫助。

```md
## 2026/6/24

- 完成兩題 `shelve` 練習：冒險者存檔管理、商店庫存存檔
- 練習 `shelve.open()`、`db.keys()`、key 查詢、資料修改與整包寫回
- 理解 shelve 會保存上次執行後的狀態，重複執行修改程式會讓數值持續變動
- 完成資料存在 / 不存在的查詢判斷