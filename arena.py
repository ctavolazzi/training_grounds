# # Import functions, classes, items, etc
from Warrior import Warrior
from Items import Items
from fight import fight


# # Initialize the simulation
warrior1 = Warrior("Ognar", 100, 5, [Items[0]])
# print("Warrior 1: ")
# print(warrior1)
# for key, value in warrior1.items():
#   print(key, ' : ', value)

warrior2 = Warrior("Glubart", 100, 6, [Items[1]])
# print("Warrior 2 : ")
# print(warrior2)


# # Set up environmental variables
warriors = []
warriors.append(warrior1)
warriors.append(warrior2)
# print("Warriors: ")
# for Warrior in warriors:
#   print(Warrior)


# # Perform final check
print("Does this look right?")
print("Warriors: ")
for Warrior in warriors:
  print(Warrior)
# print("(readout of simulation parameters)")
proceed_with_simulation = input("Y, N? ").lower()

# Run simulation
fight_result = fight(warrior1, warrior2)
print(fight_result)