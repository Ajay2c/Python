from HigherLowerGameData import data 
from art import vs,higherlower
import random

#print(higherlower)
#print(vs)
score = 0
# took the total length array in testdata
length = len(data)
#print(length)

#generate a number to took the dictinary

comp_gen = random.randint(0,length-1)
#print(number_gen)

print(data[comp_gen])

def computer_generate():
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

Compare_A = computer_generate()

user_gen = random.randint(0,length-1)

def user_generate():
    getdata_from_dictonary = data[user_gen]
    name = getdata_from_dictonary["name"]
    print(name)
    description = getdata_from_dictonary["description"]
    print(description)
    country = getdata_from_dictonary["country"]
    print(country)
    folllower_count = getdata_from_dictonary["follower_count"]
    print(folllower_count)
    return folllower_count

Against_B = user_generate()

print(f"Compare A: {computer_generate()}.")
print(vs)
print(f"Against B: {user_generate()}.")
    
guess = input("Who has more followers? Type 'A' or 'B': ").lower()
a_follower_count = account_a["follower_count"]
b_follower_count = account_b["follower_count"]


if a_follower_count > b_follower_count and :
     
     
     

elif Compare_A == Against_B:
        user_generate()




