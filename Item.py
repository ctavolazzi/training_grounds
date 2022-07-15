class Item:
  def __init__(self, name, ap, abilities):
    self.name = name
    self.ap = ap
    self.abilities = abilities

  def __str__(self):
    return f'name: {self.name}, ap: {self.ap}, abilities: {self.abilities}'

  # def __repr__(self):
  #   return f'name: {self.name}, ap: {self.ap}, abilities: {self.abilities}'