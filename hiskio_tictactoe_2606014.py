import os
import time

# 定義顏色與樣式變數
BOLD = '\033[1m'      # 加粗
GREEN = '\033[92m'     # 綠色 (適合 "Add" 或 "Success")
YELLOW = '\033[93m'    # 黃色 (適合 "Menu" 或 "Warning")
RED = '\033[91m'       # 紅色 (適合 "Delete" 或 "Exit")
CYAN = '\033[96m'      # 青色 (適合選單標題)
RESET = '\033[0m'      # 重置 (一定要加，不然之後的字都會變色)

WIN_DATA = [[1, 2, 3], [3, 6, 9], [7, 8, 9], [1, 4, 7],
            [2, 5, 8], [4, 5, 6], [1, 5, 9], [3, 5, 7,]]


def create_grid():
    return [1, 2, 3,
            4, 5, 6,
            7, 8, 9]


def print_grid(grid):
    print(f" {grid[0]} | {grid[1]} | {grid[2]} ")
    print("---+---+---")
    print(f" {grid[3]} | {grid[4]} | {grid[5]} ")
    print("---+---+---")
    print(f" {grid[6]} | {grid[7]} | {grid[8]} ")
    print()


def user_input(grid, xo):
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
                print(f"{BOLD}{YELLOW}{xo}選擇了{user_choose}號格子{RESET}")
                return user_choose - 1

        except ValueError:
            print(f"{BOLD}{YELLOW}請輸入整數1~9喔!{RESET}")


def ox_control(turn):
    if turn % 2 == 0:
        return "X"
    else:
        return "O"


def win_control(grid, turn, xo):

    for target in WIN_DATA:
        target_num = 0
        for num in target:
            if grid[num - 1] == xo:
                target_num += 1
        if target_num == 3:
            return "win"

    if turn == 9:
        return "draw"

    return None


def restart():
    while True:
        choose = input("是否再玩一局?(輸入 yes 再來一局,或者 no 離開遊戲):")
        choose = choose.lower().strip()

        if choose == "yes":
            return "yes"
        elif choose == "no":
            return "no"
        else:
            print(f"{BOLD}{RED}請輸入「yes」或「no」喔!{RESET}")


def main():
    os.system('color')  # 啟動 Windows 顏色支援
    turn = 0
    restart_choice = None
    grid = create_grid()

    print()
    print_grid(grid)
    while True:
        turn += 1
        current_player = ox_control(turn)

        position = user_input(grid, current_player)
        grid[position] = current_player

        print_grid(grid)

        result = win_control(grid, turn, current_player)

        if result == "win":
            print(f"{BOLD}{CYAN}{current_player}贏了!{RESET}")
            restart_choice = restart()
        elif result == "draw":
            print(f"{BOLD}{CYAN}平手囉!{RESET}")
            restart_choice = restart()

        if restart_choice == "yes":
            grid = create_grid()
            turn = 0
            restart_choice = None

            print()
            print_grid(grid)

            continue
        elif restart_choice == "no":
            print("好的,正在離開程式......")
            time.sleep(2)
            print(f"{BOLD}{GREEN}感謝遊玩,下次再見owo!{RESET}")
            return


if __name__ == "__main__":
    main()
