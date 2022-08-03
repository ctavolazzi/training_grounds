def stat_modifier(warrior, stat, value):
  if stat == 'ap':
    warrior.ap += value
  elif stat == 'dp':
    warrior.dp += value
  elif stat == 'hp':
    warrior.hp += value
  else:
    warrior.stat += value
    # print(f'{stat} is not a valid stat')
  return warrior