# Split string method
names_string = input("Give me everybody's names, separated by a comma. ")
names = names_string.split(", ")
# 🚨 Don't change the code above 👆

#Write your code below this line 👇

import random


x = len(names) - 1

new_names = random.randint(0,x)


new_names_2 = names[new_names]

print(f"{new_names_2} is going to buy the meal today!")

# import random

# random_index = random.randint(0, len(names) - 1)
# random_name = names[random_index]
# print(f"{random_name} is going to buy the meal today!")