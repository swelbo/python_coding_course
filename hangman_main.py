# Hangman game 

# import modules
#from replit import clear
import os
import random
import hangman_art
import hangman_words

# Game logo from hangman_art
print(hangman_art.logo)

# List of words
word_list = hangman_words.word_list

# Variables 
chosen_word = random.choice(word_list) # other method "x = random.randint(0,2) #chosen_word = word_list[x]"
word_length = len(chosen_word)
lives = 6

# generate a list of "_" representing the length of the word TODO IDEA! - list comprehension here instead of for loop!
display = []
for i in range(word_length):
    display += "_"

# print the list joined (removes quotes)
print(f"{' '.join(display)}\n")

# end of game variable plus while loop until game over
end_of_game = False
while not end_of_game:     # while "_" in display: # old while loop that seems easier to understand but might be wrong

    #get user to guess a letter and save to variable
    guess = input("Guess a letter: ").lower()
   
    # the screen after each loop
    # define function that will clear the screen after each loop 
    def clear():
        os.system("clear")
    clear()

    #TODO-4: - If the user has entered a letter they've already guessed, print the letter and let them know.
    if guess in display:
        print(f"You have already guessed {guess}. Guess again!")

    # loop through the chose word to see if guessed letter is there? 
    #  reveals letter in the display at that position
    for position in range(word_length):
        letter = chosen_word[position]
        if letter == guess:
            display[position] = letter
    #  old first attempt but works 
    #count = 0
    #for letter in chosen_word:
        #if guess == letter:
            #display[count] = guess
        #count += 1

    # print display with guesses added if any
    print(f"{' '.join(display)}")
    
    # If guess is not in the chosen word the player looses a life
    if guess not in chosen_word:
        lives -= 1
        print(f"{guess} is not in the word. You lose a life! \nYou have {lives} lives remaining") # show the user how many lives they have remaining  
        #if lives == 0:
            #end_of_game = True
            #print("You have zero lives remaining, YOU LOSE!")

    # End game control 
    if "_" not in display:
        end_of_game = True
        print("you win")
    elif lives == 0:
        end_of_game = True
        print(f"Oh man! you lose. The word was {chosen_word}")

    # print the ascii art after each guesss (even if correct). Import from hangman_art.
    print(hangman_art.stages[lives])