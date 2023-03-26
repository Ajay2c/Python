import random

rock =("""
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
""")

paper =("""
     _______
---'    ____)____
           ______)
          _______)
         _______)
---.__________)
""")

scissor = ("""
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
""")

values = input("Please select 0 for Rock, 1 for Paper, or 2 for Scissors: ")

if values not in ["0", "1", "2"]:
    print("Invalid input. Please select 0 for Rock, 1 for Paper, or 2 for Scissors.")
else:
    if values == "0":
        print(f"You chose Rock:\n{rock}")
    elif values == "1":
        print(f"You chose Paper:\n{paper}")
    else:
        print(f"You chose Scissors:\n{scissor}")

    computer_choice = str(random.randint(0,2))
    
    if computer_choice == "0":
        print(f"Computer chose Rock:\n{rock}")
    elif computer_choice == "1":
        print(f"Computer chose Paper:\n{paper}")
    else:
        print(f"Computer chose Scissors:\n{scissor}")
    
    if computer_choice == values:
        print("It's a draw! Do you want to play again?")
    elif (computer_choice == "0" and values == "2") or (computer_choice == "1" and values == "0") or (computer_choice == "2" and values == "1"):
        print("Computer wins! Do you want to play again?")
    else:
        print("You win! Do you want to play again?")
