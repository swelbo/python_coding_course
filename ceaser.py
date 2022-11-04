import ceaser_alphabet as ca
import art

# function dor encoding and decoding
def ceaser(start_text, shift_amount, cipher_direction):
    # shift each letter of the 'text' forwards in the alphabet by the shift amount and print the encrypted text.
    end_text = []
    
    for character in start_text:
        if character not in ca.alphabet:
            end_text += character
        else:
            position = ca.alphabet.index(character)

            if direction == "encode":
                new_position = position + shift_amount
            else:
                new_position = position - shift_amount

            end_text += ca.alphabet[new_position]

    print(f"The {cipher_direction}d text is {''.join(end_text)}")

# Print the logo 
print(art.logo)

# global restart program variable
restart = "yes"

# loop until user no longer wants to use program
while restart == "yes": 

    direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n")
    text = input("Type your message:\n").lower()
    shift = int(input("Type the shift number: "))
    
    # allows user to enter shift number higher than alphabet length
    shift = shift % 26

    # call function
    ceaser(start_text = text, shift_amount = shift, cipher_direction = direction)
    
    restart = input("Would you like to encode/decode again? ").lower()

print("OK, goodbye")

'''
### OLD VERSION

# defining function called encrypt
def encrypt(text, shift):
    # shift each letter of the 'text' forwards in the alphabet by the shift amount and print the encrypted text.  
    shifted_text = []
    for character in text:
        position = ca.alphabet.index(character)
        new_position = position + shift
        shifted_text += ca.alphabet[new_position]
    
    print(f"The encoded text is {''.join(shifted_text)}")

# defining function called encrypt decrypt
def decrypt(text, shift):
    # shift each letter of the 'text' backwards in the alphabet by the shift amount and print the encrypted text.
    reversed_text = []
    for character in text:
        position = ca.alphabet.index(character)
        new_position = position - shift
        reversed_text += ca.alphabet[new_position]
    
    print(f"The decrypted text is {''.join(reversed_text)}")

# Check if the user wanted to encrypt or decrypt the message by checking the 'direction' variable. 
if direction == "encode":
    encrypt(text, shift)
else:
    decrypt(text, shift)

'''