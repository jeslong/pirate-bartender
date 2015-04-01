import random

questions = {
    "strong": "Do ye like yer drinks strong?",
    "salty": "Do ye like it with a salty tang?",
    "bitter": "Are ye a lubber who likes it bitter?",
    "sweet": "Would ye like a bit of sweetness with yer poison?",
    "fruity": "Are ye one for a fruity finish?"
}

ingredients = {
    "strong": ["glug of rum", "slug of whisky", "splash of gin"],
    "salty": ["olive on a stick", "salt-dusted rim", "rasher of bacon"],
    "bitter": ["shake of bitters", "splash of tonic", "twist of lemon peel"],
    "sweet": ["sugar cube", "spoonful of honey", "splash of cola"],
    "fruity": ["slice of orange", "dash of cassis", "cherry on top"]
}

def order_drink():
  drink_order = {}
  for key, value in questions.items():
    response = raw_input(value)
    if response.lower() == 'yes' or response.lower() == 'y':
      answer = True
    else:
      answer = False
    drink_order[key] = answer
  return drink_order
  
def mix_drink(order):
  drink = []
  for key, value in order.items():
    if key[value] == True:
      drink.append("HEllo")
  print drink
"""  if order['salty'] == True:
    drink.append(random.choice(ingredients['salty']))
  if order['strong'] == True:
    drink.append(random.choice(ingredients['strong']))
"""
o = order_drink()
print o
print mix_drink(o)