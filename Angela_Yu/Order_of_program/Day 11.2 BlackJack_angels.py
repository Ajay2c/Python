import random 
cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
def deal_cards(cards):
    new_card = random.choice(cards)
    return new_card

user_cards = []
computer_cards = []

user_score = 0
computer_score = 0
def add_cards():
    for split in range(2):
        user_cards.append(deal_cards())
        computer_cards.append(deal_cards())
    return 

def calculate():
    user_score = sum(user_cards)
    computer_score = sum(computer_cards)
    return user_score, computer_score

def drawanother_card():
        user_cards.append(deal_cards())
        computer_cards.append(deal_cards())
        blackjack_check()

def blackjack_check():
    if 11 in user_cards and 10 in user_cards:
        print("User has blackjack, computer lose ")
    elif 11 in computer_cards and 10 in computer_cards:
        print("Computer won the game, user lose")
    elif user_score > 21 or computer_score > 21:
        if 11 not in user_cards and 11 not in computer_cards:
            print("you Lose")
        elif 11 in user_cards and len(user_cards) == 2:
            print("you won, computer lose")
        elif 11 in computer_cards and len(computer_cards) == 2:
            print("You won, user lose")
    else:
        play_again = input("Type 'y' to get another card, or type 'n' to pass: ")
        if play_again == 'y':
            drawanother_card()
        elif play_again == 'n':
            if computer_score > 17:
                computer_cards.append(deal_cards)
            elif computer_score > 21:
                print("you won, computer lose")
            else:
                if user_score == computer_score:
                    print("Draw match")
                elif user_score > computer_score:
                    print("Win")
                elif user_score < computer_score:
                    print("Lose")            

start_game = True
while start_game:
        
    want_to_play = input("Do you want to play a game of Blackjack? Type 'y' or 'n' ")
    if want_to_play == "y":
        add_cards()
        calculate()
        blackjack_check()
    else:
        start_game = False    








    



print(add_cards(),calculate())



