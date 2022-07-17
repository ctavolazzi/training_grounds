from cgi import test
# import uuid
import random
from warrior_code.warrior_name_generator import warrior_name_generator
# from warrior_name_generator import warrior_name_generator

class Warrior:
  def __init__(self, name=None, hp=None, ap=None, inventory=None):
    self.name = name
    self.hp = hp
    self.ap = ap
    self.inventory = inventory
    if name is None:
      # self.name = uuid.uuid4().hex[:6]
      self.name = warrior_name_generator()
    if hp is None:
      self.hp = random.randint(1, 10)
    if ap is None:
      self.ap = random.randint(1, 10)
    if inventory is None:
      self.inventory = []

  def __str__(self):
    if len(self.inventory) > 0:
      inv = []
      for item in self.inventory:
        inv.append(str(item))
      return f'name: {self.name}, hp: {self.hp}, ap: {self.ap}, inventory: {inv}'
    else:
      return f'name: {self.name}, hp: {self.hp}, ap: {self.ap}, inventory: {self.inventory}'

  def attack(self, target):
    print(f'{self.name} attacks {target.name} for {self.ap} damage')
    target.hp -= self.ap

# # Debugging
# test_warrior = Warrior()
# print(test_warrior)
# # ogre = {"name" : "Ogre", "hp" : 100, "ap" : 5}
# ogre = Warrior("Ogre", 100, 5)
# print(ogre.name)
# test_warrior.attack(ogre)