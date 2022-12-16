
from enum import IntEnum

class x(IntEnum): # Action here could be anything. This class allows us to add or remove samples.  
    test = 0 
    this = 1
    out = 2

s = int(input("Please guess a number between 1 and 10 "))

y = x(s)

print(y.name)

# yeah baby 


