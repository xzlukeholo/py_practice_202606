import shelve

players = {
    "Mia": {
        "level": 5,
        "gold": 300,
        "items": ["藥水", "短劍"]
    },
    "MeiMei": {
        "level": 8,
        "gold": 520,
        "items": ["魔法杖"]
    },
    "Alice": {
        "level": 3,
        "gold": 150,
        "items": []
    }
}


with shelve.open("player_save") as s_save:
    s_save['Mia'] = players['Mia']
    s_save['MeiMei'] = players['MeiMei']
    s_save['Alice'] = players['Alice']
    print("存檔成功")
