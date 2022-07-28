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

def run_simulation(warriors, items):
  winners = []
  while len(warriors) >= 0:
    # comb1 = warriors.pop(warriors[random.randint(0, len(warriors) - 1)])
    # comb2 = warriors.pop(warriors[random.randint(0, len(warriors) - 1)])
    if len(warriors) == 2:
      print(f'\n{warriors[0].name} and {warriors[1].name} are the final combatants!')
      print(warriors)
      print(f'\n{warriors[0].name} has {warriors[0].hp} health and {warriors[0].ap} AP and is carrying')
      warrior1inv = []
      for item in warriors[0].inventory:
        warrior1inv.append(str(item))
      print(warrior1inv)
      print(f'\n{warriors[1].name} has {warriors[1].hp} health and {warriors[1].ap} AP and is carrying')
      warrior2inv = []
      for item in warriors[1].inventory:
        warrior2inv.append(str(item))
      print(warrior2inv)
      print("\n")
      break
    elif len(warriors) <= 1:
      # # If theres only 1 warrior left, they win by default and move up a bracket
      if(len(warriors)) == 1:
        warrior = warriors.pop(0)
        winners.append(warrior)
        # print("Only one warrior remains...")
      else:
        print("0 warriors")
        print(warriors)
        print("End of round")
      break
    else:
      comb1 = warriors.pop(random.randint(0, len(warriors) - 1))
      comb2 = warriors.pop(random.randint(0, len(warriors) - 1))

    if comb1 and comb2:
      while comb1.hp > 0 or comb2.hp > 0:
        if comb1.hp <= 0 and comb2.hp <= 0:
          print("They both died :(")
          print("\n")
          break
        elif comb2.hp <= 0 and comb1.hp > 0:
          print(comb2.name + ' dies...')
          print(comb1.name + " wins!")
          for item in comb2.inventory:
            # comb1.inventory.append(item)
            comb1.pick_up(item)
          winners.append(comb1)
          print("\n")
          break
        elif comb1.hp <= 0 and comb2.hp > 0:
          print(comb1.name + ' dies...')
          print(comb2.name + " wins!")
          for item in comb1.inventory:
            # comb2.inventory.append(item)
            comb2.pick_up(item)
          winners.append(comb2)
          print("\n")
          break
        else:
          comb1.attack(comb2)
          comb2.attack(comb1)
    else:
      print("No one left to fight...\n")
    # if comb1 and comb2 > 0:
    #   winner = fight(comb1, comb2)
    #   if winner == comb1:
    #     winners.append(comb1)
    #   elif winner == comb2:
    #     winners.append(comb2)
    #   else:
    #     print("Something went wrong")
    #     quit()
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