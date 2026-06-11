# Count all letters, digits and special symbols from a given string

str = "HelloP@$thon3"

char = 0
digit = 0
spchr = 0
for i in range(0, len(str), 1):
    if str[i].isdigit():
        digit = digit +1
    elif str[i].isalpha():
        char = char+1
    else:
        spchr = spchr+1

print("Alphabets = ", char)
print("Digits : ", digit)
print("Special Characters : ", spchr)