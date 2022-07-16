# # Import functions, classes, items, etc
from Warrior import Warrior
from item_code.Items import Items
from helper_functions.item_check import item_check
# from fight import fight


# # Initialize the simulation
print("Initializing...")


# # Set up environmental variables
warriors = []
# Ask user how many Warriors to create
number_of_warriors = input("How many Warriors?: ")
if int(number_of_warriors) <= 0:
  print("Closing Simulation...")
  quit() # Hard quits the program if you don't generate any Warriors
# Ask user if they want to customize their Warriors
number_of_items = input("How many Items do you want to generate? ")
# similar code to warriors setup here

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
  # Run environmental setup again
  # Note: environmental setup should be extracted and encapsulated in modular code
  print("Running environment setup again...")
  print("ERROR: unable to complete environment setup\nSimulation Cancelled")
else:
  print("Unrecognized Input...Simulation Cancelled")

# Run simulation
# fight_result = fight(warrior1, warrior2)