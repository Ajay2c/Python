import random
# Rock
#from multiprocessing.sharedctypes import Value

rock =("""
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
""")

# Paper
paper =("""
     _______
---'    ____)____
           ______)
          _______)
         _______)
---.__________)
""")

# Scissors
scissor = ("""
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
""")


Values = input("Please select the mentioned number to start the game 0 for Rock , 1 for Paper or 2 for Scissor ")


if Values == "0":
    print(f"You choose the Rock: {rock}")
elif Values == "1":
    print(f"You choose the Paper: {paper}")
elif Values == "2":
    print(f"You choose the Scissor: {scissor}")

computer_choise = str(random.randint(0,2))


if computer_choise == "0":
    print(f"Computer choose the Rock: {rock}")
elif computer_choise == "1":
    print(f"Computer choose the Paper: {paper}")
elif computer_choise == "2":
    print(f"Computer choose the Scissor: {scissor}")
else:
    print("Select the correct value")

if computer_choise == "0" and Values =="0":
    print("You both are choosen as same stuff, Match is Draw, You want to Play again")
elif computer_choise == "1" and Values =="1":
    print("You both are choosen as same stuff, Match is Draw, You want to Play again")
elif computer_choise == "2" and Values =="2":
    print("You both are choosen as same stuff, Match is Draw, You want to Play again")
elif computer_choise == "0" or Values =="1":
    print("Computer won the game, You want to Play again")
elif computer_choise == "1" or Values =="2":
    print("Computer won the game, You want to Play again")
elif computer_choise == "2" or Values =="0":
    print("Computer won the game, You want to Play again")
elif computer_choise == "1" or Values =="0":
    print("You won the game, You want to Play again")
elif computer_choise == "2" or Values =="1":
    print("You won the game, You want to Play again")
elif computer_choise == "0" or Values =="2":
    print("You won the game, You want to Play again")


















