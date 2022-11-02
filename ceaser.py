import ceaser_alphabet as ca

direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n")
text = input("Type your message:\n").lower()
shift = int(input("Type the shift number (1-50):\n"))


#Combine the encrypt() and decrypt() functions into a single function called caesar(). 

def ceaser(text, shift):
    # shift each letter of the 'text' forwards in the alphabet by the shift amount and print the encrypted text.
    shifted_text = []
    for character in text:
        position = ca.alphabet.index(character)
        if direction == "encode":
            new_position = position + shift
        else:
            new_position = position - shift
        shifted_text += ca.alphabet[new_position]

    print(f"The {direction}d text is {''.join(shifted_text)}")

#Call the caesar() function, passing over the 'text', 'shift' and 'direction' values.
ceaser(text, shift)

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