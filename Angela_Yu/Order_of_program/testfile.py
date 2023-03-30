import random
cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]

numberof_times_genarate = 2

dealer_card_list = []
user_card_list = []

dealer_score = 0
user_score = 0

def deal_card():
    dealer_random_selected = random.randint(0,12) # generating a new random number
    dealer_card_select = cards[dealer_random_selected] # selecting the a card by using a random number
    dealer_card_list.append(dealer_card_select) # adding the card 
def user_card():
    user_random_selected = random.randint(0,12) # generating a new random number
    user_card_select = cards[user_random_selected] # selecting the a card by using a random number
    user_card_list.append(user_card_select) # adding the card 

def calculator():
    global dealer_score
    global user_score   

    for d_score in dealer_card_list:
        dealer_score += d_score

    for u_score in user_card_list:
        user_score += u_score

def game_start():
    global numberof_times_genarate
    for deal in range(0,numberof_times_genarate):
        deal_card()
        user_card()
    #print(dealer_card_list)
    #print(user_card_list)
    calculator()

def addcard():
    card = random.choice(cards)
    user_card_list.append(card)
    dealer_card_list.append(card)


   
start_game = True
while start_game:
        
    want_to_play = input("Do you want to play a game of Blackjack? Type 'y' or 'n' ")

    if want_to_play == 'y':
        game_start()
        play_again = input("Type 'y' to get another card, or type 'n' to pass: ")
        if play_again == 'y':
            addcard()
        else:
            start_game = False    
    elif want_to_play == "n":
        start_game = False



print(dealer_card_list)
print(user_card_list)
print(f"Your card:{user_card_list}, current score: {user_score}") 
print(f"Computer's first card: {dealer_card_list[0]}, computer score: {dealer_score}")
