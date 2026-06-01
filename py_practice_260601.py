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
stocks = [
    {"ticker": "NVDA", "price": 1200, "return_pct": 3.2, "volume": 35},
    {"ticker": "MSFT", "price": 430, "return_pct": -1.2, "volume": 20},
    {"ticker": "GOOG", "price": 175, "return_pct": -0.4, "volume": 15},
    {"ticker": "MU", "price": 110, "return_pct": 2.1, "volume": 48},
    {"ticker": "PLTR", "price": 85, "return_pct": 5.5, "volume": 60},
]


# 取得股票代號
def get_ticker(stock):
    ticker = stock["ticker"]
    return ticker


# 判斷股票是否上漲
def is_positive(stock):
    if stock["return_pct"] > 0:
        return True
    elif stock["return_pct"] < 0:
        return False
    else:
        print("股票平盤")


# 找出第一檔上漲的股票
def find_first_positive(stocks):
    for stock in stocks:
        if stock["return_pct"] > 0:
            return stock

    return None


# 找出所有上漲股票
def find_all_positive(stocks):
    rising_stocks = []
    for stock in stocks:
        if stock["return_pct"] > 0:
            rising_stocks.append(stock["ticker"])
    return rising_stocks


print(find_all_positive(stocks))
