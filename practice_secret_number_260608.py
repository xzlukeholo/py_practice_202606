import random
import sys
import time
import os

os.system('color')

# 定義顏色與樣式變數
BOLD = '\033[1m'      # 加粗
GREEN = '\033[92m'     # 綠色 (適合 "Add" 或 "Success")
YELLOW = '\033[93m'    # 黃色 (適合 "Menu" 或 "Warning")
RED = '\033[91m'       # 紅色 (適合 "Delete" 或 "Exit")
CYAN = '\033[96m'      # 青色 (適合選單標題)
RESET = '\033[0m'      # 重置 (一定要加，不然之後的字都會變色)


print(f"{BOLD}{CYAN}{'=' * 23}{RESET}")
time.sleep(1)
print(f"{BOLD}{CYAN}歡迎來到 Secret Number!{RESET}")
print(f"{BOLD}{CYAN}在 1 到 1000 之間有一個藏著宇宙解答的秘密數字{RESET}")
time.sleep(1)
print(f"{BOLD}{YELLOW}現在! 你有 10 次機會{RESET}")
time.sleep(1)
print()


def reset():
    global answer, low, high, attempts
    answer = random.randint(1, 1000)
    low = 1
    high = 1000
    attempts = 0


def try_again():
    while True:
        play_again = input("感謝遊玩。\n是否要再玩一次？請輸入 y 或 n :").strip().lower()
        if play_again == "y":
            return

        elif play_again == "n":
            exit_game()
        else:
            print("請輸入y或n")


def exit_game():
    print(f"{BOLD}{CYAN}遊戲結束{RESET}")
    time.sleep(1)
    print(f"{BOLD}{CYAN}我們下次再見OwO!{RESET}")
    sys.exit()


def show_remaining_attempts():
    remaining_attempts = max_attempts - attempts

    print(f"{BOLD}{CYAN}目前可能範圍：{low}~{high}{RESET}")
    if remaining_attempts > 3:
        print(f"{BOLD}{YELLOW}剩餘的猜測次數: {remaining_attempts} 次{RESET}")
    else:
        print(f"{BOLD}{RED}剩餘的猜測次數: {remaining_attempts} 次{RESET}")
    print()


def check_guess_range():  # 檢查輸入是否在範圍內 & 是否是合法
    global attempts
    while True:
        try:
            user_input = input("請猜一個數字,或輸入 q 離開:").strip().lower()
            if user_input == "q":
                exit_game()
            user_input = int(user_input)
            if low <= user_input <= high:
                attempts += 1
                return user_input
            else:
                print(f"{BOLD}{RED}請輸入目前範圍內的數字喔!{RESET}")
                continue
        except ValueError:
            print(f"{BOLD}{RED}請輸入整數喔!愛您!{RESET}")
            continue


def play_round():
    global low, high

    while True:

        user_input = check_guess_range()

        if user_input == answer:
            print(f"{BOLD}{GREEN}恭喜你猜對了！太厲害了! 答案就是{answer}{RESET}!!!")
            print(f"你總共猜了 {attempts} 次")
            print()
            return

        if attempts >= max_attempts:
            print(f"{BOLD}{YELLOW}你輸了QwQ!好可惜，答案是{answer}喲!{RESET}")
            print()
            return

        if user_input > answer:
            print()
            print(f"{BOLD}{CYAN}太大囉!{RESET}")
            high = user_input - 1
            show_remaining_attempts()
            continue

        if user_input < answer:
            print()
            print(f"{BOLD}{CYAN}太小囉!{RESET}")
            low = user_input + 1
            show_remaining_attempts()
            continue


max_attempts = 10

while True:
    reset()
    play_round()
    try_again()
