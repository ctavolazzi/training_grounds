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

def item_name_generator(item = None):
  types = ["Sword", "Axe", "Pike", "Trident", "Net", "Broadsword", "Shield", "Claw", "Bat", "Stick", "Scythe", "Mallet", "Flail"]
  pre = ["Great", "Weak", "Basic", "Sharp", "Dull", "Long", "Bloody", "Damaged", "Honed", "Battle-worn", "Sturdy", "Heavy"]
  flairs = ["of Onyx", "of the Eagle", "of Greatness", "of the Bear", "of Strength", "of the Bull", "of the Night", "of Righteousness", "of the Unholy"]
  result = str(pre[random.randint(0, len(pre) - 1)]) + " " + str(types[random.randint(0, len(types) - 1)]) + str(flairs[random.randint(0, len(flairs) - 1)])
  return result

# # Debugging
print(item_name_generator())