import uuid

class Warrior:
  def __init__(self, name, hp, ap, inventory):
    self.name = name
    self.hp = hp
    self.ap = ap
    self.inventory = inventory
    if name is None:
      self.name = uuid.uuid4().hex[:6]
    if hp is None:
      self.hp = 1
    if ap is None:
      self.ap = 1

  def __str__(self):
    if len(self.inventory) > 0:
      inv = []
      for item in self.inventory:
        inv.append(str(item))
      return f'name: {self.name}, hp: {self.hp}, ap: {self.ap}, inventory: {inv}'
    else:
      return f'name: {self.name}, hp: {self.hp}, ap: {self.ap}, inventory: {self.inventory}'