# Hangman game 

# import modules
import random

word_list = ["aardvark", "baboon", "camel"]

# other method (old)
#x = random.randint(0,2)
#chosen_word = word_list[x]

# choose random work
chosen_word = random.choice(word_list)
word_length = len(chosen_word)

# Testing code
print(chosen_word)
print(len(chosen_word))


# TODO - list comprehension here instead of for loop!
# generate a list of "_" representing the length of the word
display = []
for i in range(word_length):
    display += "_"
print(display)


#TODO-1: - Use a while loop to let the user guess again. The loop should only stop once the user has guessed all the letters in the chosen_word and 'display' has no more blanks ("_"). Then you can tell the user they've won.

end_of_game = False
while not end_of_game:

# while "_" in display: # old while loop that seems easier to understand but might be wrong

    #get user to guess a letter and save to variable
    guess = input("Guess a letter: ").lower()
    print(guess)

    # loop through the chose word to see if guessed letter is there? 
    #  reveals letter in the display at that position
    for position in range(word_length):
        letter = chosen_word[position]
        if letter == guess:
            display[position] = letter

    #  old first attempt but works 
    ''' 
    count = 0
    for letter in chosen_word:
        if guess == letter:
            display[count] = guess
        count += 1
    '''

    # print display with guesses added 
    print(display)

    if "_" not in display:
        end_of_game = True
        print("you win")