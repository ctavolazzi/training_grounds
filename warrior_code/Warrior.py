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
      self.hp = random.randint(1, 100)
    if ap is None:
      self.ap = random.randint(1, 10)
    if inventory is None:
      self.inventory = []

  def __str__(self):
    if len(self.inventory) > 0:
      inv = []
      for item in self.inventory:
        inv.append(str(item))
      return f'NAME: {self.name}, HP: {self.hp}, AP: {self.ap}, inventory: {inv}'
    else:
      return f'NAME: {self.name}, HP: {self.hp}, AP: {self.ap}, inventory: {self.inventory}'

  def attack(self, target):
    print(f'{self.name} attacks {target.name} for {self.ap} damage')
    target.hp -= self.ap
    # print(f'{self.name} HP: {self.hp}')
    # print(f'{target.name} HP: {target.hp}')

  def item_check(self, item):
    print(f'{self.name} checks their inventory')
    print(item)

  def pick_up(self, item):
    print(f'{self.name} picks up the {item.name}')
    if (item.ap > 0):
      self.ap += item.ap
      print(f'{self.name} now has {self.ap} AP')
      self.inventory.append(item)
    else:
      print(f'{item.name} has no AP')
    return self.inventory

  def grab_random_item(self, all_items):
    item = random.choice(all_items)
    print(f'{self.name} ({self.ap} AP) chooses a random item:')
    print(item)
    self.pick_up(item)
    # self.inventory.append(item)
    # if (item.ap > 0):
    #   self.ap += item.ap
    #   print(f'{self.name} now has {self.ap} AP')
    # else:
    #   print(f'{item.name} has no AP')
    return self.inventory

  def yell(self):
    print(f'{self.name} yells: "I am a warrior!"')
    return self.name


# # Debugging
# test_warrior = Warrior()
# print(test_warrior)
# # ogre = {"name" : "Ogre", "hp" : 100, "ap" : 5}
# ogre = Warrior("Ogre", 100, 5)
# print(ogre.name)
# test_warrior.attack(ogre)