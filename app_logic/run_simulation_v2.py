import random

from app_logic.commence_battle import commence_battle

def run_simulation_v2(warriors):
  winners = []
  while len(warriors) >= 2:
    current_pair = []
    current_pair.append(warriors.pop(random.randint(0, len(warriors) - 1)))
    current_pair.append(warriors.pop(random.randint(0, len(warriors) - 1)))
    # print("warriors: " + str(warriors))
    # print("\ncurrent_pair: " + str(current_pair))
    winner = commence_battle(current_pair)
    print("Battle complete")
    print("Winner:\n", str(winner))
    winners.append(winner)
  if len(warriors) == 1:
    print(f"\nWarrior {warriors[0].name} fights nobody and still wins...")
    print("Winner:\n", str(warriors[0]))
    winners.append(warriors[0])
  print("\nWinners: ")
  count = 0
  for w in winners:
    print(w)
    count += 1
  print(f"Total Winners:\n{count}")
  return winners