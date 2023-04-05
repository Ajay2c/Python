from HigherLowerGameData import data 
from art import vs,higherlower
import random

#print(higherlower)
#print(vs)
score = 0
# took the total length array in testdata
length = len(data)
#print(length)

def computer_generate():
    comp_gen = random.randint(0,length-1)
    getdata_from_dictonary = data[comp_gen]
    name = getdata_from_dictonary["name"]
    print(name)
    description = getdata_from_dictonary["description"]
    print(description)
    country = getdata_from_dictonary["country"]
    print(country)
    folllower_count = getdata_from_dictonary["follower_count"]
    print(folllower_count)
    return folllower_count

def user_generate():
    user_gen = random.randint(0,length-1)
    getdata_from_dictonary = data[user_gen]
    name = getdata_from_dictonary["name"]
    print(name)
    description = getdata_from_dictonary["description"]
    print(description)
    country = getdata_from_dictonary["country"]
    print(country)
    folllower_count = getdata_from_dictonary["follower_count"]
    print(folllower_count)
    print(f"Compare A: {name}, a {description}, from {country}.")
    return folllower_count

a_follower_count = computer_generate()
print(vs)
b_follower_count = user_generate()

guess = input("Who has more followers? Type 'A' or 'B': ").lower()

if b_follower_count > a_follower_count and guess == 'b':
     score += 1
     a_follower_count = b_follower_count
     b_follower_count = user_generate()
elif a_follower_count > b_follower_count and guess == 'a':
     score += 1
     b_follower_count = a_follower_count
     a_follower_count = computer_generate()
else:
     b_follower_count = user_generate()

print(f"Your current score is: {score}.")
