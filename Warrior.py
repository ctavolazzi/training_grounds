class Warrior:
  def __init__(self, name, hp, ap, inventory):
    self.name = name
    self.hp = hp
    self.ap = ap
    self.inventory = inventory

  def __str__(self):
    if len(self.inventory) > 0:
      inv = []
      for item in self.inventory:
        inv.append(str(item))
      return f'name: {self.name}, hp: {self.hp}, ap: {self.ap}, inventory: {inv}'
    else:
      return f'name: {self.name}, hp: {self.hp}, ap: {self.ap}, inventory: {self.inventory}'