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
stocks = [
    {"ticker": "NVDA", "price": 1200, "return_pct": 3.2, "volume": 35},
    {"ticker": "MSFT", "price": 430, "return_pct": -1.2, "volume": 20},
    {"ticker": "GOOG", "price": 175, "return_pct": -0.4, "volume": 15},
    {"ticker": "MU", "price": 110, "return_pct": 2.1, "volume": 48},
    {"ticker": "PLTR", "price": 85, "return_pct": 5.5, "volume": 60},
    {"ticker": "VSH", "price": 100, "return_pct": 10.0, "volume": 78},
]

# 用最低漲跌幅篩選股票


def filter_by_return(stocks, min_return=0):
    passed_return_stocks = []
    for stock in stocks:
        if stock["return_pct"] >= min_return:
            passed_return_stocks.append(stock)
    return passed_return_stocks


# 計算平均漲跌幅
def calculate_average_return(stocks):
    sum_return_pct = 0
    if stocks:
        for stock in stocks:
            sum_return_pct += stock["return_pct"]
        average_return = sum_return_pct / len(stocks)
    else:
        return 0
    return average_return


# 建立股票摘要字串：練 return

def build_stock_summary(stock):
    return f"{stock['ticker']} | Price:{stock['price']} | Return:{stock['return_pct']} | Volume:{stock['volume']}"

# 印出股票摘要：練 print


def print_stock_summary(stock):
    print(build_stock_summary(stock))


result = print_stock_summary(stocks[0])
print(result)
