"""
Write a function that would take any possible “inventory” and display it like the following:

Inventory:
12 arrow
42 gold coin
1 rope
6 torch
1 dagger
Total number of items: 62
"""


def display_inventory(inventory_list):
    print("Inventory:")
    item_count = 0
    for item, qty in inventory_list.items():
        item_count += qty
        print("{} {}".format(qty, item))
    print("Total number of items: {}".format(item_count))


def add_to_inventory(inventory_list, new_loot):
    for item in new_loot:
        inventory_list.setdefault(item, 0)
        inventory_list[item] += 1
    return inventory_list


your_stuff = {'rope': 1, 'torch': 6, 'gold coin': 42, 'dagger': 1, 'arrow': 12}
dragon_loot = ['gold coin', 'dagger', 'gold coin', 'gold coin', 'ruby']

display_inventory(your_stuff)

print("""
Your rewards for slaying the dragon:
""")
for loot in dragon_loot:
    print(loot)

print()
add_to_inventory(your_stuff, dragon_loot)
display_inventory(your_stuff)