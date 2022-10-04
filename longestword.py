## Find the longest word

# A string of words seperated by white space and commas
x  = "This is a string, and i need to find out, what the long word is"

# remove all apperance of "," using replace() method
s = x.replace(',', '')

# check data 
print(s)

# Split the string into a list of individual words 
list_of_words = s.split()

# Check the list 
print(list_of_words)

# Check for the longest word 
# use the length of thr words replacing the longest word 
# each time length of word is > the length of the previous word
length_of_word = 0
longest_word = None
for word in list_of_words:
    leni = len(word)
    if leni > length_of_word:
        length_of_word = leni
        longest_word = word

# Print the outcome
print(f"Longest word is {longest_word}")