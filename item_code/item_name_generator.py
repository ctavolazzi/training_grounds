"""
Combine words together to make randomized item names

From a list of words, combine a prefix, type, and "of" statement

Example: "Great Broadsword of the Eagle"

MVP: Combine random words together
ADV: Combine words together based on the item's attributes
EXT: Add support for abilities and modifications

"""

from os import pread
import random
from site import PREFIXES

def item_name_generator(type = None):
  if type == None:
    type = random.choice(['weapon', 'armor', 'potion'])
  if type == 'weapon':
    PREFIXES = ["Great", "Weak", "Basic", "Sharp", "Dull", "Long", "Bloody", "Damaged", "Honed", "Battle-worn", "Sturdy", "Heavy", "Fast", "Surefooted", "Swanky", "Thief's", "Hidden", "Translucent", "Ephemeral", "Blissful", "Foolish", "Fatal", "Dangerous", "Super Lit", "Black", "White"]
    WEAPON_CATEGORIES = ["Sword", "Axe", "Mace", "Dagger", "Bow", "Staff", "Wand"]
    prefix = random.choice(PREFIXES)
    weapon = random.choice(WEAPON_CATEGORIES)
    binder = random.choice(['of', 'from', 'with'])
    suffix = random.choice(['Eagle', 'Greatness', 'Below', 'Above', 'Protection', 'Devastation', 'Vengance', 'Glory', 'Great Pain'])
    return f'{prefix} {weapon} {binder} the {suffix}'
  elif type == 'armor':
    PREFIXES = ["Great", "Weak", "Basic", "Sharp", "Dull", "Long", "Bloody", "Damaged", "Honed", "Battle-worn", "Sturdy", "Heavy", "Fast", "Surefooted", "Swanky", "Thief's", "Hidden", "Translucent", "Ephemeral", "Blissful", "Foolish", "Fatal", "Dangerous", "Super Lit", "Black", "White"]
    ARMOR_CATEGORIES = ["Helmet", "Chestplate", "Leggings", "Boots", "Gloves", "Shield"]
    SUFFIXES = ['Greatness', 'Below', 'Above', 'Protection', 'Devastation', 'Vengance', 'Glory', 'Great Pain']
    prefix = random.choice(PREFIXES)
    armor = random.choice(ARMOR_CATEGORIES)
    binder = random.choice(['of', 'from', 'with'])
    suffix = random.choice(SUFFIXES)
    return f'{prefix} {armor} {binder} the {suffix}'
  elif type == 'potion':
    PREFIXES = ["Great", "Weak", "Basic", "Sharp", "Dull", "Long", "Bloody", "Damaged", "Honed", "Battle-worn", "Sturdy", "Heavy", "Fast", "Surefooted", "Swanky", "Thief's", "Hidden", "Translucent", "Ephemeral", "Blissful", "Foolish", "Fatal", "Dangerous", "Super Lit", "Black", "White"]
    POTION_CATEGORIES = ['Healing', 'Damage', 'Buff', 'Debuff', 'Utility']
    SUFFIXES = ['Greatness', 'Below', 'Above', 'Protection', 'Devastation', 'Vengance', 'Glory', 'Great Pain']
    prefix = random.choice(PREFIXES)
    potion = random.choice(POTION_CATEGORIES)
    binder = random.choice(['of', 'from', 'with'])
    suffix = random.choice(SUFFIXES)
    return f'{prefix} {potion} {binder} the {suffix}'
  else:
    return 'Invalid item type'

  # result = str(pre[random.randint(0, len(pre) - 1)]) + " " + str(types[random.randint(0, len(types) - 1)]) + " " + str(flairs[random.randint(0, len(flairs) - 1)])
  # return result

# # Debugging
# print(item_name_generator())
# df = [1, 2, 3]
# print(len(df))