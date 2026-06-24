import shelve


with shelve.open("player_save") as player_save:
    player_find = input("查詢的角色:")

    if player_find not in player_save:
        print(f"找不到 {player_find} 的存檔！")
    else:
        player_result = player_save[player_find]
        print(f"等級: {player_result['level']}")
        print(f"金幣: {player_result['gold']}")
        print(f"道具: {player_result['items']}")
