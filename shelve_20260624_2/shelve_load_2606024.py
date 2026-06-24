import shelve


with shelve.open("shelve_save") as shelve_save:
    print("目前商品:" + "、".join(shelve_save.keys()))

    potion = shelve_save['potion']
    potion['stock'] -= 2
    shelve_save['potion'] = potion

    shop_item = input("請輸入要查詢的商品")

    if shop_item in shelve_save:
        item = shelve_save[shop_item]

        print(f"商品名稱: {item['name']}")
        print(f"價格: {item['price']}")
        print(f"庫存: {item['stock']}")
    else:
        print(f"找不到{shop_item}這個商品！")
