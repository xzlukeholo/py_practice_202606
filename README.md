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

## 印出股票摘要：練 print

def print_stock_summary(stock):

情境：
前一題已經有一個函式可以產生股票摘要。現在需要另一個函式，專門負責把摘要顯示在畫面上。
要求：請寫一個函式

- 可以重複利用第 7 題的 `build_stock_summary(stock)`。
- 這個函式的主要任務是顯示資料。
- 不需要特別回傳資料。

測試：

result = print_stock_summary(stocks[0])
print(result)

思考：

1. 第一行會印出什麼？
2. 第二行會印出什麼？
3. 為什麼這個函式沒有寫 `return` 時，`result` 會是 `None`？

'''