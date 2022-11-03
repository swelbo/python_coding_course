import ceaser_alphabet as ca
import art

def ceaser(text, shift, direction):
    # shift each letter of the 'text' forwards in the alphabet by the shift amount and print the encrypted text.
    end_text = []
    
    for character in text:
        if character not in ca.alphabet:
            end_text.append(character)
        else:
            position = ca.alphabet.index(character)
            if direction == "encode":
                new_position = position + shift
            else:
                new_position = position - shift
            end_text += ca.alphabet[new_position]

    print(f"The {direction}d text is {''.join(end_text)}")

# Print the logo 
print(art.logo)

restart = "yes"
while restart == "yes": 

    direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n")
    text = input("Type your message:\n").lower()
    shift = int(input("Type the shift number (1-50):\n"))

    #TODO-2: What if the user enters a shift that is greater than the number of letters in the alphabet?
    #Try running the program and entering a shift number of 45.
    #Add some code so that the program continues to work even if the user enters a shift number greater than 26. 
    #Hint: Think about how you can use the modulus (%).
    ceaser(text, shift, direction)
    
    restart = input("play again? ")

print("Goodbye")

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