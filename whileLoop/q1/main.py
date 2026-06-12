# Separate each digit of a number and print it on a new line

x = int(input("Enter any number : "))

while x > 0 :
    print(x % 10)
    x = x // 10