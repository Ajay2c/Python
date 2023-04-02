from art import type_somthing 
print(type_somthing)

import random

computer_selected = 0
def correct_answer():
    global computer_selected
    number_list = []
    for i in range(1,101):
        number_list.append(i)
    computer_selected = random.choice(number_list)
    return int(computer_selected)
correct_answer() # Step-1

#Step -4
def attempts_cal(easy_attempts):
    start_game = True
    while start_game: 
        global computer_selected
        print(f"You have {easy_attempts} attempts remaining to guess the number.")
        easy_guess = int(input("Make a guess: "))
        if easy_guess == computer_selected:
            print(f"You got it! The answer was{computer_selected}")
            start_game = False
        elif easy_guess > computer_selected:
            print("Too high")
            easy_attempts -= 1
            print("Guess again.")
            if easy_attempts == 0:
                print("You used all your attempts, game over")
                start_game = False
        
        elif easy_guess < computer_selected:
            print("Too low")
            easy_attempts -= 1
            print("Guess again.")
            if easy_attempts == 0:
                print("You used all your attempts, game over")
                start_game = False
            
# Step-2
print("Welcome to the number Guessing Game!")
print("I'm thinking of a number between 1 and 100. ")
print(f"Psst, the correct answer is {computer_selected}")
user_choice = input("Choose a difficulty. Type 'easy' or 'hard': ")    

#Step-3
if user_choice == "easy":
        attempts_cal(5)   
else:
     attempts_cal(10)

