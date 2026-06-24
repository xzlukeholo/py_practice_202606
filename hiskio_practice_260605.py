# Intermediate Exercise I:
# ---
# 第一題.Write a function called "mySort"
# that takes an list of integers as input,
# and returns the sorted version of the input list.
# You are not allowed to use the built-in sorted() function.
# ---
# mySort([17, 0, -3, 2, 1, 0.5]) returns [-3, 0, 0.5, 1, 2, 17]
# ---
# 答:

def mySort_fail(numbers):
    if not numbers:
        return "No data"

    result = []
    for time in range(len(numbers)):
        numbers = [num for num in numbers if num not in result]
        min_num = numbers[0]

        for number in numbers:
            if number < min_num:
                min_num = number
        result.append(min_num)
    return result


'''
 上面有不少問題:
     問題	                      說明
 重複數字會錯	    num not in result 會刪掉所有相同值
 空 list 會錯	    numbers[0] 在空 list 會報錯
 不建議用 round    當變數	round 是 Python 內建函式名稱
 反覆重建 list	    效率比較差，而且邏輯容易出錯

 下面是修正版:
'''


def mySort_notgood(numbers):
    result = []
    r_numbers = numbers.copy()

    while len(r_numbers) > 0:
        min_num = r_numbers[0]

        for number in r_numbers:
            if number < min_num:
                min_num = number
        result.append(min_num)
        r_numbers.remove(min_num)

    return result


'''
remove() 會再從 list 裡面找一次 min_num，所以有點重複工作。

妳的流程其實是：

1.找最小值
2.放進 result
3.從 remaining 移除那個最小值
4.重複

這是可以的，但不算最標準的排序演算法寫法。

更標準的 selection sort在下面練習

下面這版比較像正式的「選擇排序」。

# 被建議的寫法:
'''
# mySort([17, 0, -3, 2, 1, 0.5]) returns [-3, 0, 0.5, 1, 2, 17]


def mySort(numbers):
    re_numbers = numbers.copy()

    for i in range(len(re_numbers)):
        min_index = i

        for j in range(i + 1, len(re_numbers)):
            if re_numbers[min_index] > re_numbers[j]:
                min_index = j
        re_numbers[i], re_numbers[min_index] = re_numbers[min_index], re_numbers[i]

    return re_numbers


# ---
# 第二題.Write a function called "isPrime"
# that takes an integer as input,
# and returns a boolean value that indicates if the input number is prime.
# ---
# isPrime(1); # returns false
# isPrime(5); # returns true
# isPrime(91); # returns false
# isPrime(1000000); # returns false
# ---
# 答:


def isPrime_my(number):
    if not isinstance(number, int):
        # 我知道題目說是integer,但不能確保使用者輸入一定正確,我覺得還是要防呆
        return False

    if number <= 1:
        return False

    if number == 2:
        return True

    if number % 2 == 0:
        return False

    for i in range(3, int(number ** 0.5) + 1, 2):
        if number % i == 0:
            return False

    return True


'''
#被告知可以優化,找到開根號就好,所以有修正過了
簡單來說：「如果一個大於 1 的正整數有因數，那其中一個因數一定小於或等於它的平方根。」
因此，要檢查是不是質數，我們不需要一路上網查到 (n-1)
只需要檢查到 (\sqrt{n}\)（也就是 n ** 0.5)就完全足夠了。

如果一個數可以被分解：
number = a * b
那麼 a 和 b 不可能都大於 sqrt(number)。
所以只要檢查到平方根，前面沒找到因數，後面也不會有新的必要檢查。

🚀 速度差多少？（驚人的差距）
假設我們要檢查剛剛那個 7 位數的質數 6911321：老實的做法：從 2 一直除到 6911320，要跑 6,911,319 次 迴圈。
數學加速做法：
(\sqrt{6911321} \approx 2628.9\)。加上 int 和 + 1 後，
range(2, 2630) 只要跑 2,628 次 迴圈。運算次數直接縮小了 2600 倍！
電腦本來要算幾秒鐘，現在一瞬間就噴出答案了。
'''
