file = open("books.txt", "r") 

#your code goes here 
f = file.readlines()
for line in f:
    letter = line[0]
    num = len(line.strip())
    print(f"{letter}{num}")
file.close()

file = open("books.txt", "r") # reopen file - once reaadlines has cycled through the files it doesn't reset until you've closed the file
f = file.readlines()
for line in f:
    print(line.strip())
file.close()