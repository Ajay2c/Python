def start_cipher(plain_text, shift_position, cipher_direction):
    end_game = ""
    if cipher_direction == "decode":
        shift_position = shift_position * -1
    for letter in plain_text:
        if letter not in alphabet:
            end_game += letter
        else:
            position_of_el = alphabet.index(letter)
            new_position_of_el = position_of_el + shift_position
            cipher_text_el = alphabet[new_position_of_el]
            end_game += cipher_text_el
    print(end_game)


alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n")
text = input("Type your message:\n").lower()
shift = int(input("Type the shift number:\n"))

the_game = True

while the_game:

    if direction != "encode" and direction != "decode":
        print("Invalid data passed, please enter a valid message.")
    elif shift > 26:
        new_shift = shift % 26 
        start_cipher(plain_text=text, shift_position=new_shift, cipher_direction=direction)
        play_again = input(
            "Type 'yes' if you want to go again. Otherwise type 'no'\n").lower()
        if play_again == "no":
            the_game = False
            print("Game over")
    else:
        start_cipher(plain_text=text, shift_position=shift, cipher_direction=direction)
        play_again = input(
            "Type 'yes' if you want to go again. Otherwise type 'no'\n").lower()
        if play_again == "no":
            the_game = False
            print("Game over")

    

