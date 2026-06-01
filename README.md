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

#評語:
85 / 100。

主要扣分點在兩個：

is_positive() 遇到 return_pct == 0 時沒有回傳 False，而是 print("股票平盤")，函式實際回傳 None。
find_all_positive() 題目說「回傳所有上漲股票」，比較嚴格來看應該回傳整個 dictionary；妳現在是只回傳 ticker 字串。