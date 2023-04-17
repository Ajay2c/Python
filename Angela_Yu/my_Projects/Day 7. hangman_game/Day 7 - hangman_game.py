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

word_list = ["ardvark", "baboon", "camel"]

choosen_random = random.randint(0,2)

choosen_word = word_list[choosen_random]

choosen_word_len = len(choosen_word)

print(f"{choosen_word},{choosen_word_len}")

space_contain_words = []

for letter_length in range(choosen_word_len):
    space_contain_words += "_"
    #print(letter_length)

lives = 7 

print("Hi welcome to the hangman challenge!!!!")
while not lives == 0:
    if "_" in space_contain_words:    
        user_guess = input(f"please enter the letter to check what word you going to find:").lower()

        if user_guess not in choosen_word:
                    lives -= 1
                    print(stages[lives])
                    print(f"You made mistake, now you have {lives} lives only")


        for check_positon in range(choosen_word_len):
            if user_guess == choosen_word[check_positon]:
                space_contain_words[check_positon] = user_guess        
            
        print(space_contain_words)      
    
    if lives == 0:
                print("You lost all you lifes")
    if "_" not in space_contain_words:
          lives = False
          print("You won")


