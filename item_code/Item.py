# import uuid
import random
from item_code.item_name_generator import item_name_generator

class Item:
  def __init__(self, name = None, ap = None):
    self.name = name
    self.ap = ap
    if name is None:
      # self.name = uuid.uuid4().hex[:6]
      self.name = item_name_generator() # this function is still in development
    if ap is None:
      self.ap = random.randint(1, 10)

  def __str__(self):
    # return f'name: {self.name}, ap: {self.ap}, id: {id(self)}' # I discovered there's a built-in id function and I didn't need the uuid thing at all. Such is life.
    return f'NAME: {self.name}, AP: {self.ap}'

  # def __repr__(self):
  #   return f'name: {self.name}, ap: {self.ap}, abilities: {self.abilities}'

  def add_method(self, method_name, method):
    setattr(self, method_name, method)
    return self

# # Debugging
# test_group = []
# for x in range(3):
#   test_item = Item()
#   test_group.append(test_item)
#   print(test_item)