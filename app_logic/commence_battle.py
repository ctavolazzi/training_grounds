import random

def commence_battle(warriors):
  print("\nBattle Commencing...\n")
  print("Fight Begins!")
  w1 = warriors[0]
  w2 = warriors[1]
  print("\nWarrior 1:\n", w1, "\nvs\nWarrior 2:\n", w2, "\n")
  while w1.hp > 0 and w2.hp > 0:
    w1.attack(w2)
    w2.attack(w1)
    print(f"{w1.name} hp: {w1.hp}\n{w2.name} hp: {w2.hp}")
    if w1.hp <= 0 and w2.hp <= 0:
      print("They both died :(")
      print("\n")
      return None
    elif w2.hp <= 0 and w1.hp > 0:
      print(w2.name + ' dies...')
      print(w1.name + " wins!")
      for item in w2.inventory:
        w1.pick_up(item)
      return w1
    elif w1.hp <= 0 and w2.hp > 0:
      print(w1.name + ' dies...')
      print(w2.name + " wins!")
      for item in w1.inventory:
        w2.pick_up(item)
      return w2
    else:
      print("\n")
      continue


  # winners = []
  # if warriors.__len__() > 1:
  #   while(len(warriors) > 2):
  #     w1 = warriors.pop(random.randint(0, len(warriors) - 1))
  #     w2 = warriors.pop(random.randint(0, len(warriors) - 1))
  #     while w1.hp > 0 and w2.hp > 0:
  #       if w1.hp <= 0 and w2.hp <= 0:
  #         print("They both died :(")
  #         print("\n")
  #         break
  #       elif w1.hp <= 0 and w2.hp > 0:
  #         print(w1.name + ' dies...')
  #         print(w2.name + " wins!")
  #         for item in w1.inventory:
  #           w2.pick_up(item)
  #         winners.append(w2) # add w2 to winners list
  #         print("\n")
  #         break
  #       elif w2.hp <= 0 and w1.hp > 0:
  #         print(w2.name + ' dies...')
  #         print(w1.name + " wins!")
  #         for item in w2.inventory:
  #           w1.pick_up(item)
  #         winners.append(w1) # add w1 to winners list
  #         print("\n")
  #         break
  #       else:
  #         w1.attack(w2)
  #         w2.attack(w1)
  #     if warriors.__len__() == 2:
  #       print(f'\n{warriors[0].name} and {warriors[1].name} are the final combatants!')
