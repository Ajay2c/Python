# Password Generator Project
import random
letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y',
           'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

print("Welcome to the PyPassword Generator!")
nr_letters = int(input("How many letters would you like in your password?\n"))
nr_symbols = int(input(f"How many symbols would you like?\n"))
nr_numbers = int(input(f"How many numbers would you like?\n"))

# Eazy Level - Order not randomised:
# e.g. 4 letter, 2 symbol, 2 number = JduE&!91


# Hard Level - Order of characters randomised:
# e.g. 4 letter, 2 symbol, 2 number = g^2jk8&P


# password = ""

# for char in range(1, nr_letters + 1):
#     password += random.choice(letters)


# for symb in range(1, nr_symbols + 1):
#     password += random.choice(symbols)

# for numb in range(1, nr_numbers + 1):
#     password += random.choice(numbers)

# random.shuffle(int(float(password)))
# print(password)


# --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------


# Hard Level - Order of characters randomised:
# e.g. 4 letter, 2 symbol, 2 number = g^2jk8&P


# We are going to use Random.shuffle so we need to create a list to store the looped datas
password_list = []

# on here we use Append (or) += to store the String value on the Password_List[]
for char in range(1, nr_letters + 1):
    password_list.append(random.choice(letters))  # password_list =[char]

for symb in range(1, nr_symbols + 1):
    password_list += random.choice(symbols)  # password_list =[char,symb]

for numb in range(1, nr_numbers + 1):
    password_list += random.choice(numbers)  # password_list =[char,symb,numb]

print(password_list)  # ['i', 'y', 'o', 'E', '%', '+', '2']

random.shuffle(password_list)

print(password_list)  # ['%', '+', '2', 'o', 'i', 'y', 'E']

# need to store from this ['%', '+', '2', 'o', 'i', 'y', 'E']  to  this %+2oiyE
new_char = ""

for i in password_list:
    new_char += i
    print(i)
print(new_char)

















