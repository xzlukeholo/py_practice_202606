import pickle

player_name = "Mia"
level = 7
hp = 85
gold = 320
items = ["potion", "iron sword", "apple"]


def save_data():
    global player_name, level, hp, gold, items

    data = {"player_name": player_name, "level": level, "hp": hp,
            "gold": gold, "items": ["potion", "iron sword", "apple"]}

    with open("pickle_rpg_save", "wb") as p_save:
        pickle.dump(data, p_save)


save_data()

'''
pickle_rpg_save.py

player_name = "Mia"
level = 7
hp = 85
gold = 320
items = ["potion", "iron sword", "apple"]

請寫一個函式：
def save_data():
    ...


要求：
把 player_name, level, hp, gold, items 包成一個字典 data
字典的 key 請使用：
"name"
"level"
"hp"
"gold"
"items"

第二部分：寫 restore_data()
使用 global 還原這些全域變數：
player_name
level
hp
gold
items


測試:
save_data()

player_name = None
level = None
hp = None
gold = None
items = None

restore_data()

print(player_name)
print(level)
print(hp)
print(gold)
print(items)

輸出:
Mia
7
85
320
['potion', 'iron sword', 'apple']
'''
