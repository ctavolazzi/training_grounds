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
  firstnames = ["Gronk", "Alexander", "Greek", "Glum", "Pallut", "Brixby", "Figglestix", "Adam", "Barney", "Colt", "Dewey", "Ed", "Frodo", "Gandalf", "Harry", "Iroh", "Jabba", "Kev", "Lancelot", "Mordor", "Ned", "Odin", "Pippin", "Quig", "Ragnar", "Sauron", "Tyrion", "Ug", "Voldemort", "Waldo", "Xyzzy", "Yoda", "Zed", "Ziggy", "Barnaby", "Ruth", "Jaxon", "Lily", "Sophie", "Lucy", "Mia", "Isabella", "Olivia", "Amelia", "Elizabeth", "Ella", "Molly", "Ava", "Lily", "Sophie", "Lucy", "Mia", "Isabella", "Olivia", "Amelia", "Elizabeth", "Ella", "Molly", "Ava", "Michael", "Max", "Richard", "Pox", "Peter", "Dexter", "Elfkut", "Johan", "Schmee", "Gweebo"]
  surnames = ["Born", "Spittle", "Plow", "Flume", "Fain", "Waxler", "Ungo", "Jamkit", "Smith", "Axner", "Bartov", "Cannon", "Dex", "Eddy", "Frost", "Gandalf", "Harry", "Iroh", "Jabba", "Kev", "Lancelot", "Mordor", "Ned", "Odin", "Pippin", "Quig", "Ragnar", "Sauron", "Tyrion", "Ug", "Voldemort", "Waldo", "Xyzzy", "Yoda", "Zed", "Ziggy", "Barnaby", "Ruth", "Jaxon", "Lily", "Sophie", "Lucy", "Mia", "Isabella", "Olivia", "Amelia", "Elizabeth", "Ella", "Molly", "Ava", "Lily", "Sophie", "Lucy", "Mia", "Isabella", "Olivia", "Amelia", "Elizabeth", "Ella", "Molly", "Ava", "Michael", "Max", "Richard", "Pox", "Peter", "Dexter", "Elfkut", "Gabbagool"]
  reputations = ["the Great", "the Cowardly", "of Yore", "the Burly", "the Brave", "of Your Mom", "the Wise", "the Ungodly", "the Righteous", "the Unclean", "the Maniac", "living Slaughterhouse", "of the People", "of the Streets", "who is actually a Bat", "Goated with the Sauce", "of Higgens Glenn", "- Victorious", "without Fear", "who is High as Balls"]
  result = str(firstnames[random.randint(0, len(firstnames) - 1)]) + " " + str(surnames[random.randint(0, len(surnames) - 1)]) + " " + str(reputations[random.randint(0, len(reputations) - 1)])
  return result

# # Debugging
# print(warrior_name_generator())