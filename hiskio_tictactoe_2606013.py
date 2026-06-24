import os
import sys
os.system('color')  # 啟動 Windows 顏色支援

# 定義顏色與樣式變數
BOLD = '\033[1m'      # 加粗
GREEN = '\033[92m'     # 綠色 (適合 "Add" 或 "Success")
YELLOW = '\033[93m'    # 黃色 (適合 "Menu" 或 "Warning")
RED = '\033[91m'       # 紅色 (適合 "Delete" 或 "Exit")
CYAN = '\033[96m'      # 青色 (適合選單標題)
RESET = '\033[0m'      # 重置 (一定要加，不然之後的字都會變色)

grid = [1, 2, 3,
        4, 5, 6,
        7, 8, 9]
turn = 0


def print_grid(grid):
    print(f" {grid[0]} | {grid[1]} | {grid[2]} ")
    print("---+---+---")
    print(f" {grid[3]} | {grid[4]} | {grid[5]} ")
    print("---+---+---")
    print(f" {grid[6]} | {grid[7]} | {grid[8]} ")
    print()


def user_input(xo):
    while True:
        try:
            user_choose = int(
                input(f"{BOLD}{GREEN}請{RESET}{BOLD}{CYAN}「{xo}」玩家{RESET}{BOLD}{GREEN}選擇要畫在幾號(請輸入1~9):{RESET}"))
            if user_choose > 9 or user_choose < 1:
                print(f"{BOLD}{YELLOW}超出1~9的範圍了呦{RESET}")
                continue
            elif user_choose not in grid:
                print(f"{BOLD}{YELLOW}不能選在別人下過的地方喔!{RESET}")
                continue
            else:
                print()
                print(f"{BOLD}{GREEN}{xo}選擇了{user_choose}號格子{RESET}")
                return user_choose - 1

        except ValueError:
            print(f"{BOLD}{YELLOW}請輸入整數1~9喔!{RESET}")


def OX_control():
    if turn % 2 == 0:
        return "X"
    else:
        return "O"


def win_control(xo):

    win_data = [[1, 2, 3], [3, 6, 9], [7, 8, 9], [1, 4, 7],
                [2, 5, 8], [4, 5, 6], [1, 5, 9], [3, 5, 7,]]
    for target in win_data:
        target_num = 0
        for num in target:
            if grid[num - 1] == xo:
                target_num += 1
        if target_num == 3:
            print(f"{BOLD}{CYAN}{xo}贏了!{RESET}")
            sys.exit()
    if turn == 9:
        print(f"{BOLD}{CYAN}平手囉!{RESET}")
        sys.exit()


print()
print_grid(grid)
while True:
    turn += 1

    grid[user_input(OX_control())] = OX_control()
    print_grid(grid)
    win_control(OX_control())
