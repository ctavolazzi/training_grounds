from arena_code.fight import fight
from warrior_code.Warrior import Warrior

def run_simulation(group):
  ogre = Warrior("Ogre", 100, 5)
  for warrior in group:
    if (ogre.hp <= 0):
      print(f'{ogre.name} is dead')
      quit()
    elif (ogre.hp > 0):
      warrior.attack(ogre)
      if (ogre.hp <=0):
        print(f'{ogre.name} is dead')
        print(f'{warrior.name} killed him!')
        quit()
      else:
        print(f'{ogre.name} has {ogre.hp} health')
  return("Simulation complete")