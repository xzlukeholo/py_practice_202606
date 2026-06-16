import shelve

player_names = ["Mia", "Meimei", "Nina"]

player_levels = [12, 15, 8]

player_items = [
    ["potion", "wooden sword"],
    ["magic staff", "healing herb"],
    ["shield", "apple"]
]


with shelve.open("save_shelf") as s_save:
    s_save["player_names"] = player_names
    s_save["player_levels"] = player_levels
    s_save["player_items"] = player_items
print("運行成功")
