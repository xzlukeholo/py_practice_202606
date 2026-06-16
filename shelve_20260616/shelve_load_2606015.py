import shelve


with shelve.open("save_shelf") as load_s:
    print("所有 key")
    for key in load_s.keys():
        print(key)

    print("印出 levels 對應的資料")
    player_levels = load_s["player_levels"]
    print(player_levels)

    name = load_s["player_names"]
    level = load_s["player_levels"]
    items = load_s["player_items"]

    print("第二位玩家資訊:")
    print(f"名字:{name[1]}")
    print(f"等級:{level[1]}")
    print(f"道具:{items[1]}")

    # Meimei 的等級從升級
    level[1] += 1
    load_s["player_levels"] = level

    level = load_s["player_levels"]

    print("第二位玩家資訊(升級後):")
    print(f"名字:{name[1]}")
    print(f"等級:{level[1]}")
    print(f"道具:{items[1]}")
