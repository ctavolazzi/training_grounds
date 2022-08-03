import random
from app_logic.battle_record import battle_record

from app_logic.commence_battle import commence_battle

def run_simulation_v2(warriors, battle_log):
  battle_count = 0
  # result = {
  #   "winners": [],
  #   "losers": [],
  #   "history": []
  # }
  winners = []
  while len(warriors) >= 2:
    current_pair = []
    current_pair.append(warriors.pop(random.randint(0, len(warriors) - 1)))
    current_pair.append(warriors.pop(random.randint(0, len(warriors) - 1)))
    # print("warriors: " + str(warriors))
    # print("\ncurrent_pair: " + str(current_pair))
    winner = commence_battle(current_pair, battle_log)
    # if (winner["win_count"]):
    #   winner.win_count += 1
    # else:
    #   winner["win_count"] = 1
    print("Battle complete")
    print("Winner:\n", str(winner))
    winners.append(winner)
    battle_count += 1
  if len(warriors) == 1:
    print(f"\nWarrior {warriors[0].name} fights nobody and still wins...")
    print("Winner:\n", str(warriors[0]))
    warriors[0].memory["win_count"] += 1
    warriors[0].memory["fight_history"].append(f"Win by Default: self")
    warriors[0].memory["fight_count"] += 1
    winners.append(warriors[0])
    battle_count += 1
  print("\nWinners: ")
  count = 0
  for w in winners:
    print(w)
    count += 1
  print(f"Total Winners:\n{count}")
  print(f"Total Battles:\n{battle_count}")
  return winners