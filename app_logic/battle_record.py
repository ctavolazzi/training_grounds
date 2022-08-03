def battle_record():
  battle_record = {}
  battle_record["history"] = []
  # battle_record["winners"] = []
  # battle_record["losers"] = []
  return battle_record

def battle_record_add(battle_record, result):
  battle_record["history"].append(result)
  return battle_record

def record_battle(battle_record, result):
  battle_record = battle_record_add(battle_record, result)
  return battle_record