"""
Combine words together to make randomized warrior names

From a list of words, combine a prefix, type, and optional "the" statement

Example: "Gronk Born the Great", "Alexander Spittle the Cowardly"

MVP: Combine random words together
ADV: Combine words together based on the warrior's attributes
EXT: Add support for abilities and modifications

"""

import random

def warrior_name_generator(warrior = None):
  firstnames = ["Gronk", "Alexander", "Greek", "Glum", "Pallut", "Brixby", "Figglestix"]
  surnames = ["Born", "Spittle", "Plow", "Flume", "Fain", "Waxler", "Ungo", "Jamkit"]
  reputations = ["the Great", "the Cowardly", "of Yore", "the Burly", "the Brave", "of Your Mom", "the Wise", "the Ungodly"]
  result = str(firstnames[random.randint(0, len(firstnames) - 1)]) + " " + str(surnames[random.randint(0, len(surnames) - 1)]) + " " + str(reputations[random.randint(0, len(reputations) - 1)])
  return result

# # Debugging
print(warrior_name_generator())