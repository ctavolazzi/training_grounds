"""
Combine words together to make randomized item names

From a list of words, combine a prefix, type, and "of" statement

Example: "Great Broadsword of the Eagle"

MVP: Combine random words together
ADV: Combine words together based on the item's attributes
EXT: Add support for abilities and modifications

"""

import random

def item_name_generator(item = None):
  types = ["Sword", "Axe"]
  pre = ["Great", "Weak", "Basic"]
  result = str(pre[random.randint(0, len(pre) - 1)]) + " " + str(types[random.randint(0, len(types) - 1)])
  return result

# # Debugging
print(item_name_generator())