# # Import functions, classes, items, etc
# from warrior_code.custom_warrior import Custom_Warrior
from types import NoneType
from app_logic.battle_record import battle_record
from warrior_code.Warrior_v2 import Warrior
# from item_code.Items import Items # Obsolete - could be used to create a default set of items
from item_code.Item import Item
from warrior_code.item_check import item_check
# from arena_code.fight import fight
from app_logic.run_simulation import run_simulation
from app_logic.commence_battle import commence_battle
from app_logic.run_simulation_v2 import run_simulation_v2
import copy


# # Initialize the simulation
print("Initializing...")


# # Set up environmental variables
all_warriors = [] # warrior_setup()
all_items = [] # item_setup()

number_of_warriors = input("How many Warriors?\n")
if int(number_of_warriors) <= 0:
  print("Closing Simulation...")
  quit() # Hard quits the program if you don't generate any Warriors

number_of_items = input("How many Items?\n")

# custom_warriors = input("Do you want to set custom values for your Warriors?\n(Y), (N)? ")
# custom_items = input("Do you want to set custom values for your Items?\n(Y), (N)? ")

# if custom_items.lower() == "y":
#   print("\nPlease customize your Items\n")
#   count = 0
#   while count < int(number_of_items):
#     item = Item(input("Name: "), int(input("AP: ")))
#     print("Item " + str(count)+ ":\n", item, "\n")
#     all_items.append(item)
#     count+=1
# else:
print("Generating random Items...\n")
count = 0
while count < int(number_of_items):
  item = Item(None, None)
  all_items.append(item)
  print("\nItem " + str(count + 1)+ ":\n", item, "\n")
  count+=1

# if custom_warriors.lower() == "y":
#   print("\nPlease customize your Warriors\n")
#   count = 0
#   while count < int(number_of_warriors):
#     warrior = Custom_Warrior(input("Name: "), int(input("HP: ")), int(input("AP: ")), item_check(all_items))
#     print("Warrior " + str(count) + ":\n", warrior, "\n")
#     warrior.yell()
#     all_warriors.append(warrior)
#     count+=1
# else:
print("Generating random Warriors...\n")
count = 0
while count < int(number_of_warriors):
  warrior = Warrior()
  print("\nWarrior " + str(count + 1) + ":\n", warrior, "\n")
  # for item in all_items:
  #   warrior.item_check(item)
  warrior.grab_random_item(all_items)
  all_warriors.append(warrior)
  count+=1


# # Perform final check
print("\nProceed with simulation?\n")
print("\nWarriors: ")
for warrior in all_warriors:
  print(warrior)
# print("(readout of simulation parameters)")
proceed_with_simulation = input("Y, N? ").upper()
if proceed_with_simulation == "Y":
  # Run simulation
  # Call functions here to run the simulation
  print("\nRunning simulation...")
  # # Run simulation
  # grand_victors = run_simulation_v2(all_warriors)
  battle_log = battle_record()
  combatants = copy.deepcopy(all_warriors)
  while(len(combatants) >= 2):
    winners = run_simulation_v2(combatants, battle_log)
    combatants = winners
  print("\nSimulation complete!")
  # print("\nNumber of battles: " + str(number_of_battles))
  print("\nFinal Victor: ")
  for w in combatants:
    print(w)
  print("\nNumber of Items: " + str(len(all_warriors[0].inventory)))
  print("\nTotal Winners: " + str(len(all_warriors)))
  # print("\nGrand Victors: ")
  # for w in grand_victors:
  #   print(w)
  # if(len(all_warriors) == 1):
  #   print("\nFinal Warrior: ")
  #   print(all_warriors[0])
  # else:
  #   print("\nNo Warriors remain!")
  #   print(all_warriors) # used for debugging
  # winners = run_simulation(all_warriors)
  # print("\nWinners:\n")
  # for warrior in winners:
  #   print(warrior)
elif proceed_with_simulation == "N":
  # Run environmental setup again
  # Note: environmental setup should be extracted and encapsulated in modular code
  print("\nRunning environment setup again...")
  print("\nERROR: unable to complete environment setup\nSimulation Cancelled")
else:
  print("\nUnrecognized Input...Simulation Cancelled")

"""
Put the warriors in the arena
Make them fight
Only one is victorious
"""