# Fond the second largest number


x = [12, 10, 32, 33, 43, 11]

large = x[0]
secondLarge = x[0]

for i in x:
    if i > large:
        secondLarge = large
        large = i
    elif i > secondLarge:
        secondLarge = i

print(secondLarge)
        

