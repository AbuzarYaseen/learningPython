# Print the sum of all even and odd numbers in a range separately of the given number

n = int(input("Enter any number : "))

evenSum = 0
oddSum = 0

for i in range (1, n+1):
    if(i % 2 == 0):
        evenSum = evenSum+i
    else:
        oddSum = oddSum+i
print("Sum of all even numbers = ", evenSum)
print("Sum of all odd numbers = ", oddSum)