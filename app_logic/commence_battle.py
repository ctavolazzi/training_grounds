import random

def commence_battle(warriors, battle_log):
  print("\nBattle Commencing...\n")
  print("Fight Begins!")
  w1 = warriors[0]
  w2 = warriors[1]
  # log = {
  #   "warriors": [w1, w2],
  #   "winner": None,
  #   "loser": None,
  #   "history": [],
  #   "w1_attack_count": 0,
  #   "w2_attack_count": 0,
  #   "w1_damage_dealt": 0,
  #   "w2_damage_dealt": 0,
  #   "w1_blocked_attacks": 0,
  #   "w2_blocked_attacks": 0,
  #   "w1_damage_taken": 0,
  #   "w2_damage_taken": 0,
  #   "w1_abilities_used": [],
  #   "w2_abilities_used": [],
  # }
  w1.memory["fight_count"] += 1
  w2.memory["fight_count"] += 1
  # w1.memory["fight_history"].append(w2.name)
  # w2.memory["fight_history"].append(w1.name)
  w1.memory["last_enemy"] = w2.name
  w2.memory["last_enemy"] = w1.name

  print("\nWarrior 1:\n", w1, "\nvs\nWarrior 2:\n", w2, "\n")
  w1endorig = w1.endurance
  w2endorig = w2.endurance
  # log.history.append(f"{w1.name} begin {w2.name} exchanging blows!")
  while w1.hp > 0 and w2.hp > 0:
    w1.attack(w2)
    # log.w1_attack_count += 1
    w2.attack(w1)
    # log.w2_attack_count += 1
    print(f"{w1.name} hp: {w1.hp}\n{w2.name} hp: {w2.hp}")
    if w1.hp <= 0 and w2.hp <= 0:
      # log.history.append(f"{w1.name} and {w2.name} both die in the same blow!")
      print("They both died :(")
      print("\n")
      w1.memory["killed_by"] = w2.name
      w2.memory["killed_by"] = w1.name
      w1.memory["fight_history"].append(f"Loss: {w2.name}")
      w2.memory["fight_history"].append(f"Loss: {w1.name}")
      w1.memory["killed_by"] = w2.name
      w2.memory["killed_by"] = w1.name
      print(f"Losers: {w1} and {w2}")
      return None
    elif w2.hp <= 0 and w1.hp > 0:
      # log.history.append(f"{w1.name} wins the fight!")
      print(w2.name + ' dies...')
      print(w1.name + " wins!")
      for item in w2.inventory:
        w1.pick_up(item)
      w1.memory["win_count"] += 1
      # if (w1.memory["win_count"]):
      #   w1.memory["win_count"] += 1
      # else:
      #   w1.memory["win_count"] = 1
      w1.memory["fight_history"].append(f"Win: {w2.name}")
      w2.memory["fight_history"].append(f"Loss: {w1.name}")
      w2.memory["killed_by"] = w1.name
      w1.endurance = w1endorig
      print(f"Loser: {w2}")
      return w1
    elif w1.hp <= 0 and w2.hp > 0:
      # log.history.append(f"{w2.name} wins the fight!")
      print(w1.name + ' dies...')
      print(w2.name + " wins!")
      for item in w1.inventory:
        w2.pick_up(item)
      w2.memory["win_count"] += 1
      # if (w2.memory["win_count"]):
      #   w2.memory["win_count"] += 1
      # else:
      #   w2.memory["win_count"] = 1
      w2.memory["fight_history"].append(f"Win: {w1.name}")
      w1.memory["fight_history"].append(f"Loss: {w2.name}")
      w1.memory["killed_by"] = w2.name
      w2.endurance = w2endorig
      print(f"Loser: {w1}")
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
