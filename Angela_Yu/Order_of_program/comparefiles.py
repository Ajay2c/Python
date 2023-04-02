from difflib import Differ
  
with open('Order_of_program/Day 11.1 - BlackJack_ajay.py') as file_1, open('Order_of_program/Day 11.2 BlackJack_angels.py') as file_2:
    differ = Differ()
  
    for line in differ.compare(file_1.readlines(), file_2.readlines()):
        print(line)