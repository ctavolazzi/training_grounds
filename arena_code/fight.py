def fight(your, their):
  if your.hp <= 0:
    return "You are dead"
  if their.hp <=0:
    return "Your target is dead"
  else:
    print(your.name + " vs " + their.name)
    return "Fight Logic Runs...\nSomebody wins!"