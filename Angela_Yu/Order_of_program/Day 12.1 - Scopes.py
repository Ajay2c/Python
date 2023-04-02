################### Scope ####################

enemies = 1

def increase_enemies():
  enemies = 2
  print(f"enemies inside function: {enemies}")

increase_enemies()
print(f"enemies outside function: {enemies}")


#Local Scope - within function 

def drink_potion():
  potion_strength = 2
  print(potion_strength)

drink_potion()  
#print(potion_strength) # error for this
# Traceback (most recent call last):
#   File "/home/ajay/Desktop/Python/Angela_Yu/Order_of_program/Day 12.1 - Scopes.py", line 20, in <module>
#     print(potion_strength)
# NameError: name 'potion_strength' is not defined

#When you create a new variable or indeed a new function inside another function,
# it's only accessiable you can only use it when you're inside that function because it has local scope.


#Global Scope - you can access this any function when variable its outside

player_health = 10 #Global Variable

def drink_potion():
  global player_health
  potion_strength = 2  # Local Variable
  print(player_health)
  added = player_health + 20
  return print(added)
drink_potion()
#print(player_health)