import random
from warrior_code.warrior_name_generator import warrior_name_generator
from warrior_code.stat_modifier import stat_modifier

class Warrior:
  def __init__(self):
    self.name = warrior_name_generator()
    self.hp = random.randint(1, 100)
    self.ap = random.randint(1, 10)
    self.dp = random.randint(1, 10)
    self.endurance = random.randint(1, 10)
    self.inventory = []
    self.abilities = []
    self.memory = {"fight_count": 0, "fight_history": [], "last_enemy": None, "killed_by": None, "win_count": 0}

  def __str__(self):
    if len(self.inventory) > 0:
      inv = []
      for item in self.inventory:
        inv.append(str(item))
      return f'NAME: {self.name}, HP: {self.hp} AP: {self.ap} DP: {self.dp} END: {self.endurance} INV: {inv} ABL: {self.abilities} MEM: {self.memory}'
      # return f'NAME: {self.name}, HP: {self.hp}, AP: {self.ap}, DP: {self.dp}, inventory: {inv}, memory: {self.memory}'
    else:
      return f'NAME: {self.name}, HP: {self.hp} AP: {self.ap} DP: {self.dp} END: {self.endurance} INV: {self.inventory} ABL: {self.abilities} MEM: {self.memory}'
      # return f'NAME: {self.name}, HP: {self.hp}, AP: {self.ap}, DP: {self.dp}, inventory: {self.inventory}, memory: {self.memory}'

  def __iter__(self):
    return self.__dict__.items()

  def __next__(self):
    return self.__iter__()

  def add_method(self, method_name, method):
    self[method_name] = method

  def add_attribute(self, attribute, value):
    self[attribute] = value
    return self[attribute]

  def attack(self, target):
    if self.hp > 0:
      if (target.dp > 0 and target.endurance > 0):
        damage = self.ap - target.dp
        if damage > 0:
          target.hp -= damage
          print(f'{self.name} attacks {target.name} for {damage} damage!')
        else:
          target.endurance -= 1
          print(f'{self.name} attacks {target.name} but does no damage! {target.name} has {target.endurance} endurance left!')
      else:
        print(f'{self.name} attacks {target.name} for {self.ap} damage')
        target.hp -= self.ap
        # print(f'{self.name} HP: {self.hp}')
        # print(f'{target.name} HP: {target.hp}')
    else:
      print(f'{self.name} is dead')

  def add_ability(self, ability):
    self.abilities.append(ability)

  def modify_stats(self, stats):
    print('warrior: modify_stats:', stats)
    for stat in stats:
      print("warrior: modify_stats: loop: stat: ", stat)
      # print('warrior: modify_stats: loop: value: ', value)
      # print(type(stat))
      # print(stats[stat])
      if (stat != 'durability'): # skip unsupported stat types
        self[stat] += stats[stat]
        print(f"{self.name} new stat: {stat}: {self[stat]}")
      # self[stat] += stats[stat]
    return self.inventory

  def __getitem__(self, key):
    return self.__dict__[key]

  def __setitem__(self, key, value):
    self.__dict__[key] = value
    return self.__dict__[key]

  def pick_up(self, item):
    print(f'{self.name} picks up the {item.name}')
    # print('warrior: pick_up:', item)
    # for stat in item:
    #   print("warrior: stat: ", stat)
    #   # print ("warrior: value: ", value)
    #   # stat_name = stat[0]
    #   # stat_value = stat[1]
    self.modify_stats(item.stats)
    self.inventory.append(item)
    return self.inventory

  def grab_random_item(self, items):
    if (len(items) > 0):
      item = items.pop(random.randint(0, len(items)-1))
      print(f'{self.name} chooses a random item:')
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