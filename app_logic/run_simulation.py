import random
# from arena_code.fight import fight
# from warrior_code.Warrior import Warrior

# def run_simulation(group):
#   ogre = Warrior("Ogre", 100, 5)
#   for warrior in group:
#     if (ogre.hp <= 0):
#       print(f'{ogre.name} is dead')
#       quit()
#     elif (ogre.hp > 0):
#       warrior.attack(ogre)
#       if (ogre.hp <=0):
#         print(f'{ogre.name} is dead')
#         print(f'{warrior.name} killed him!')
#         quit()
#       else:
#         print(f'{ogre.name} has {ogre.hp} health')
#   return("Simulation complete")

def run_simulation(warriors):
  winners = []
  while len(warriors) > 0:
    # comb1 = warriors.pop(warriors[random.randint(0, len(warriors) - 1)])
    # comb2 = warriors.pop(warriors[random.randint(0, len(warriors) - 1)])
    comb1 = warriors.pop(random.randint(0, len(warriors) - 1))
    comb2 = warriors.pop(random.randint(0, len(warriors) - 1))
    while comb1.hp > 0 and comb2.hp > 0:
      comb1.attack(comb2)
      comb2.attack(comb1)
    if comb1.hp > 0:
      print(comb1.name + " wins!")
      for item in comb2.inventory:
        comb1.inventory.append(item)
      winners.append(comb1)
    elif comb2.hp > 0:
      print(comb2.name + " wins!")
      for item in comb1.inventory:
        comb2.inventory.append(item)
      winners.append(comb2)
    else:
      print("They both died...")
  return winners


# I want the simulation to grab two random warriors from the group, make them fight to the death, and then add the winners to a new group of winners.
"""
Take the group of warriors
Choose two random warriors from the group
Make them fight to the death
Add the winner to a list of winners
Continue this until there are no warriors left in the original group
If there is only one warrior left who has nobody to fight, add them into the winners group with the added attribute "lucky"
Return the group of winners
"""