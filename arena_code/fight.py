"""
The main logic for how different characters will fight one another
Fight takes in two Warriors and pitts them against one another
This should happen asynchronously, so each character can have an attack speed stat
The attack speed stat should determine how fast the character is able to attack
"""
# import asyncio

def fight(atk, dfd):
  print(atk.name + " vs " + dfd.name)
  print("Fight happens")