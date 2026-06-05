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

# 印出全部股票摘要：練 print


def print_stock_summary(stocks):
    for stock in stocks:
        print(build_stock_summary(stock))
