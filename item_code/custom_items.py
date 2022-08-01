from item_code.Item import Item # Use when debugging the main app.py file
# from Item import Item # Use when debugging this file by itself

custom_items = [
  Item("Basic Sword", 1),
  Item("Basic Shield", 1),
  {"name": "Basic Armor", "dp": 1},
]

health_potion = Item("Health Potion")
health_potion.add_method("heal", lambda self: self.hp += 10)
# Use when debugging the Items array
# for Item in Items:
#   print(Item)