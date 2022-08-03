# import uuid
import random
from item_code.item_name_generator import item_name_generator

class Item:
  def __init__(self, name=None, type=None):
    self.name = name if name else item_name_generator(type)
    self.type = type if type else random.choice(['weapon', 'armor', 'potion'])
    self.stats = {}
    if self.type == 'weapon':
      self.stats['ap'] = random.randint(1, 10)
      self.stats['durability'] = random.randint(1, 100)
    elif self.type == 'armor':
      self.stats['dp'] = random.randint(1, 10)
      self.stats['durability'] = random.randint(1, 100)
    elif self.type == 'potion':
      self.stats['hp'] = random.randint(1, 100)
      self.stats['durability'] = random.randint(1, 100)
    else:
      self.stats = {}

  def __str__(self):
    item = ''
    item += f'name: {self.name}, type: {self.type}, stats: {self.stats}'
    return item
    # for stat in self.stats:
    #   print(f'{stat}: {self.stats[stat]}')

# class Item:
#   def __init__(self, name = None, type = None):
#     self.type = type
#     self.stats = {}
#     self.__index = 0
#     # self.stats_total = 0
#     if (self.type == None):
#       self.type = random.choice(['weapon', 'armor', 'potion'])
#     count = 0
#     if self.type == 'weapon':
#       self.name = item_name_generator(self.type)
#       self.stats[str(count)] = {'ap': random.randint(1, 10)}
#       count += 1
#       self.stats[str(count)] = {'durability': random.randint(1, 10)}
#       # self.stats_total = 2
#     elif self.type == 'armor':
#       self.name = item_name_generator(self.type)
#       self.stats['ap'] = random.randint(1, 10)
#       self.stats['durability'] = random.randint(1, 10)
#       # self.stats_total = 2
#     elif self.type == 'potion':
#       self.name = item_name_generator(self.type)
#       self.stats['hp'] = random.randint(10, 100)
#       self.stats['uses'] = random.randint(1, 10)
#       # self.stats_total = 2
#     # if name is None:
#     #   # self.name = uuid.uuid4().hex[:6]
#     #   self.name = item_name_generator() # this function is still in development
#     # if ap is None:
#     #   self.ap = random.randint(1, 10)

#   def __str__(self):
#     # return f'name: {self.name}, ap: {self.ap}, id: {id(self)}' # I discovered there's a built-in id function and I didn't need the uuid thing at all. Such is life.
#     item = ''
#     for key, value in self.__dict__.items():
#       item += f'{key}: {value} '
#     return item

#   def __iter__(self):
#     return self

#   def __next__(self):
#     keys = self.stats.keys()
#     # print(keys)
#     if self.__index < len(keys):
#       self.__index += 1
#       # print(self.stats[str(self.__index - 1)])
#       return self.stats[str(self.__index - 1)]
#       # return '0'
#       # return self.stats[str(self.index - 1)]
#     raise StopIteration

#   # def __next__(self):
#   #   if (self.index <= self.stats_total):
#   #     self.index += 1
#   #     return self.stats[self.index - 1]
#   #   self.index = 0
#   #   raise StopIteration
#   # def __next__(self):
#   #   self.index += 1
#   #   if self.index <= self.att_total:
#   #     return self.index
#   #   raise StopIteration
#     # if self.index < self.att_total:
#     #   self.index += 1
#     #   att = self.__dict__[f'att_{self.index}']
#     #   return att
#     # raise StopIteration




#   # def __repr__(self):
#   #   return f'name: {self.name}, ap: {self.ap}, abilities: {self.abilities}'

#   def add_method(self, method_name, method):
#     setattr(self, method_name, method)
#     return self

# # # Debugging
# # test_group = []
# # for x in range(3):
# #   test_item = Item()
# #   test_group.append(test_item)
# #   print(test_item)