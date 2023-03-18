
import random

stages = ['''
  +---+
  |   |
  O   |
 /|\  |
 / \  |
      |
=========
''', '''
  +---+
  |   |
  O   |
 /|\  |
 /    |
      |
=========
''', '''
  +---+
  |   |
  O   |
 /|\  |
      |
      |
=========
''', '''
  +---+
  |   |
  O   |
 /|   |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
  |   |
      |
      |
=========
''', '''
  +---+
  |   |
  O   |
      |
      |
      |
=========
''', '''
  +---+
  |   |
      |
      |
      |
      |
=========
''']

logo = ''' 
 _                                             
| |                                            
| |__   __ _ _ __   __ _ _ __ ___   __ _ _ __  
| '_ \ / _` | '_ \ / _` | '_ ` _ \ / _` | '_ \ 
| | | | (_| | | | | (_| | | | | | | (_| | | | |
|_| |_|\__,_|_| |_|\__, |_| |_| |_|\__,_|_| |_|
                    __/ |                      
                   |___/    '''


word_list = [
'abruptly', 
'absurd', 
'abyss', 
'affix', 
'askew', 
'avenue', 
'awkward', 
'axiom', 
'azure', 
'bagpipes', 
'bandwagon', 
'banjo', 
'bayou', 
'beekeeper', 
'bikini', 
'blitz', 
'blizzard', 
'boggle', 
'bookworm' 
]


print(logo)

chosen_word = random.choice(word_list)

word_length = len(chosen_word)

end_of_game = False
lives = 6

print(f"The computer choosen word {chosen_word}")

display = []
for _ in range(word_length):
    display += "_"
print(display)


while not end_of_game:
    guess = input("Guess the word that you have chose: ").lower()

    if guess in display:
        print(f"You chosen word is already in the box {guess}")
    elif guess in chosen_word:
        print("You are correct keep going")    


    for position in range(word_length):
        letter = chosen_word[position]
        
        if letter == guess:
            display[position] = letter
   
    if guess not in chosen_word:
        print(f"You have total 6 lives lost one lives, current lives in {lives} ")
        lives -= 1
        if lives == 0:
            print("You Loose Computer win ")
            end_of_game = True

    print(display)

    if "_" not in display:
        end_of_game = True
        print("You Win")


    print(stages[lives])


















