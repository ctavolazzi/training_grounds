# # Import functions, classes, items, etc
from Warrior import Warrior
from item_code.Items import Items
from helper_functions.item_check import item_check
# from fight import fight


# # Initialize the simulation
print("Initializing...")
# warrior1 = Warrior("Ognar", 100, 5, [Items[0]])
# print("Warrior 1: ")
# print(warrior1)
# for key, value in warrior1.items():
#   print(key, ' : ', value)

# warrior2 = Warrior("Glubart", 100, 6, [Items[1]])
# print("Warrior 2 : ")
# print(warrior2)


# # Set up environmental variables
warriors = []
# Ask user how many Warriors to create
number_of_warriors = input("How many Warriors?: ")
if number_of_warriors == "0":
  print("Closing Simulation...")
  quit()
# Ask user if they want to customize their Warriors
custom_warriors = input("Do you want to customize your Warriors?\n(Y), (N)? ")

if custom_warriors.lower() == "y":
  print("Customize your Warriors\n")
  count = 0
  while count < int(number_of_warriors):
    warriors.append(Warrior(input("Name: "), input("HP: "), input("AP: "), item_check(Items)))
    count+=1
else:
  print("Generating random Warriors...\n")
  count = 0
  while count < int(number_of_warriors):
    warriors.append(Warrior(None, None, None, item_check(Items)))
    count+=1


# # Perform final check
print("Does this look right?")
print("Warriors: ")
for Warrior in warriors:
  print(Warrior)
# print("(readout of simulation parameters)")
proceed_with_simulation = input("Y, N? ").upper()
if proceed_with_simulation == "Y":
  print("Simulation Complete")
elif proceed_with_simulation == "N":
  print("Simulation Cancelled")
else:
  print("Unrecognized Input...Simulation Cancelled")

# Run simulation
# fight_result = fight(warrior1, warrior2)