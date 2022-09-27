#Write your code below this row 👇

# method 1
x = 0
for i in range(0, 101, 2):
    x  += i
print(x)

# method 2
x = 0
for i in range(0, 101):
    if i % 2 == 0:
        x += i
print(x)
