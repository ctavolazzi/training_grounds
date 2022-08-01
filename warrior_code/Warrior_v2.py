import random
from warrior_code.warrior_name_generator import warrior_name_generator

class Warrior:
  def __init__(self):
    self.name = warrior_name_generator()
    self.hp = random.randint(1, 100)
    self.ap = random.randint(1, 10)
    self.inventory = []
    self.abilities = []

  def __str__(self):
    if len(self.inventory) > 0:
      inv = []
      for item in self.inventory:
        inv.append(str(item))
      return f'NAME: {self.name}, HP: {self.hp}, AP: {self.ap}, inventory: {inv}'
    else:
      return f'NAME: {self.name}, HP: {self.hp}, AP: {self.ap}, inventory: {self.inventory}'

  def add_method(self, method_name, method):
    self[method_name] = method

  def attack(self, target):
    if self.hp > 0:
      print(f'{self.name} attacks {target.name} for {self.ap} damage')
      target.hp -= self.ap
      # print(f'{self.name} HP: {self.hp}')
      # print(f'{target.name} HP: {target.hp}')
    else:
      print(f'{self.name} is dead')

  def add_ability(self, ability):
    self.abilities.append(ability)

  def pick_up(self, item):
    print(f'{self.name} picks up the {item.name}')
    self.inventory.append(item)
    if (item.ap > 0):
      self.ap += item.ap
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
    # return self.inventory

  def yell(self):
    print(f'{self.name} yells: "I am a warrior!"')