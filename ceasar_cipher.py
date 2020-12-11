from art import logo
from replit import clear

alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

def caesar(start_text, shift_amount, cipher_direction):
  end_text = ""
  if cipher_direction == "decode":
    shift_amount *= -1
  for char in start_text:
    if char not in alphabet:
        end_text += char
    else:
        position = alphabet.index(char)
        new_position = position + shift_amount
        end_text += alphabet[new_position]
  clear() 
  print(logo) 
  print(f"Here's the {cipher_direction}d result: {end_text}")
 
ceasar = True
while(ceasar):
    print(logo)
    ceasar = False
    direction = input("Type 'encode' to encrypt, type 'decode' to decrypt: ")
    text = input("Type your message: ").lower()
    shift = int(input("Type the shift number: "))

    shift = shift % 26
    caesar(start_text=text, shift_amount=shift, cipher_direction=direction)
    ans = input("\nDo you want to encode or decode again?\nType 'yes' if yes or anything else if no: ")
    if ans == 'yes':
        ceasar = True
        clear()
    clear()
        
