import shelve

shop_items = {
    "potion": {
        "name": "藥水",
        "price": 50,
        "stock": 10
    },
    "sword": {
        "name": "鐵劍",
        "price": 300,
        "stock": 3
    },
    "shield": {
        "name": "木盾",
        "price": 180,
        "stock": 5
    }
}

with shelve.open("shelve_save") as shelve_save:
    shelve_save['potion'] = shop_items['potion']
    shelve_save['shield'] = shop_items['shield']
    shelve_save['sword'] = shop_items['sword']
