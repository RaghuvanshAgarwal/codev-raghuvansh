import art
import os

alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 
            'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'a', 'b', 'c', 'd', 
            'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 
            't', 'u', 'v', 'w', 'x', 'y', 'z']

def caesar(plain_text,shift_amount,direction):
  if direction == "encode" or direction == "decode":
      shift_amount %= 25
      caesar_text = ""
      new_position = 0
      position = 0
      if(direction == "decode"):
        shift_amount *=-1
      for letter in plain_text:
        if letter in alphabet:
          position = alphabet.index(letter)
          new_position = position + shift_amount
          caesar_text += alphabet[new_position]
        else:
          caesar_text  += letter
      print(f"The {direction}d text is {caesar_text}")
  else:
    print("Invalid Direction")


os.system("cls")
user_choice = "yes"
while user_choice == "yes":
    print(art.logo)
    direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n")
    text = input("Type your message:\n").lower()
    shift = int(input("Type the shift number:\n"))
    caesar(text,shift,direction)
    user_choice = input("Do You Want To Continue?\nType 'yes' for Yes and 'no' for No : ").lower()
    os.system("cls")

print("Goodbye, Thanks for using Caesar Cipher\nKeeping your secrets safe")