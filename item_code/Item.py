import uuid

class Item:
  def __init__(self, name = uuid.uuid4().hex[:6], ap = 1):
    self.name = name
    self.ap = ap
    if name is None:
      self.name = uuid.uuid4().hex[:6]
    if ap is None:
      self.ap = 1

  def __str__(self):
    return f'name: {self.name}, ap: {self.ap}'

  # def __repr__(self):
  #   return f'name: {self.name}, ap: {self.ap}, abilities: {self.abilities}'