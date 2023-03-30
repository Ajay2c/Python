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
    

    
    
    if user_score == 21 and len(user_score) == 2:
        return 0
    if 11 in user_card and user_score > 21:
        user_card.remove(11)
        user_card.append(1)
        return
    





gen_card()
addcards()
score()

print(user_card,comp_card)
print(user_score,comp_score)