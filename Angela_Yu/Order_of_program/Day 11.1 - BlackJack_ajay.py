import random
logo = '''
 _     _            _    _            _    
| |   | |          | |  (_)          | |   
| |__ | | __ _  ___| | ___  __ _  ___| | __
| '_ \| |/ _` |/ __| |/ / |/ _` |/ __| |/ /
| |_) | | (_| | (__|   <| | (_| | (__|   < 
|_.__/|_|\__,_|\___|_|\_\ |\__,_|\___|_|\_\
                       _/ |                
                      |__/                 
'''

cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
user_card = []
comp_card = []

user_score = 0
comp_score = 0

def gen_card():
    new_card = random.choice(cards)
    return new_card

def addcards():
    for i in range(2):    
        user_card.append(gen_card())
        comp_card.append(gen_card())
    return

def score():
    global user_score
    global comp_score
    user_score = sum(user_card)
    comp_score = sum(comp_card)

    if user_score == 21 and len(user_card) == 2 or comp_score == 21 and len(comp_card) == 2:
        return 0
    if 11 in user_card and user_score > 21:
        user_card.remove(11)
        user_card.append(1)
        return sum(user_card)
    elif 11 in comp_card and comp_score > 21:
        comp_card.remove(11)
        comp_card.append(1)
        return sum(comp_card)
    
def compare(user_score,comp_score):
    if user_score > 21 and comp_score > 21:
        return "You went over. You lose 😤"
    if user_score == comp_score:
        return "Draw 🙃"
    elif comp_score == 0:
        return "Lose, opponent has Blackjack 😱"
    elif user_score == 0:
        return "Win with a Blackjack 😎"
    elif user_score > 21:
        return "You went over. You lose 😭"
    elif comp_score > 21:
        return "Opponent went over. You win 😁"
    elif user_score > comp_score:
        return "You win 😃"
    else:
        return "You lose 😤"

def start_game():
    global user_card
    global comp_card
    global user_score
    global comp_score

    user_card = []
    comp_card = []
    user_score = 0
    comp_score = 0

    addcards()
    score()

    print(f"   Your cards: {user_card}, current score: {user_score}")
    print(f"   Computer's first card: {comp_card[0]}")

    play_game = True

    while play_game:
        if user_score == 0 or comp_score == 0 or user_score > 21:
            play_game = False
        else:
            user_should_deal = input("Type 'y' to get another card, type 'n' to pass: ")
            if user_should_deal == "y":
                user_card.append(gen_card())
                score()
                print(f"   Your cards: {user_card}, current score: {user_score}")
                print(f"   Computer's first card: {comp_card[0]}")
            else:
                play_game = False

    while comp_score < 17 and comp_score != 0:
        comp_card.append(gen_card())
        score()

    print(f"   Your final hand: {user_card}, final score: {user_score}")
    print(f"   Computer's final hand: {comp_card}, final score: {comp_score}")
    print(compare(user_score, comp_score))

while input("Do you want to play a game of Blackjack? Type 'y' or 'n': ") == "y":
    start_game()