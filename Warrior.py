from cgi import test
import uuid
import random

class Warrior:
  def __init__(self, name=None, hp=None, ap=None, inventory=None):
    self.name = name
    self.hp = hp
    self.ap = ap
    self.inventory = inventory
    if name is None:
      self.name = uuid.uuid4().hex[:6]
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

# Use when debugging the Warror class
# test_warrior = Warrior()
# print(test_warrior)