
def encrypt(plain_text,shift_position):
        cipher_text = ""
        for each_letter in plain_text:
            position_of_el = alphabet.index(each_letter)
            new_position_of_el = position_of_el + shift_position
            cipher_text_el = alphabet[new_position_of_el]
            cipher_text += cipher_text_el
        print(cipher_text)

def decrypt(plain_text,shift_position):
        cipher_text = ""
        for letter in plain_text:
            position_of_el = alphabet.index(letter)
            new_position_of_el = position_of_el - shift_position
            cipher_text_el = alphabet[new_position_of_el]
            cipher_text += cipher_text_el  
        print(cipher_text)   
            

alphabet=['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z','a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n")
text = input("Type your message:\n").lower()
shift = int(input("Type the shift number:\n"))

if direction == "encode":
    encrypt(plain_text=text,shift_position=shift)
elif direction == "decode":
    decrypt(plain_text=text,shift_position=shift)