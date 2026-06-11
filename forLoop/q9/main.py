# Accept a number and check if it a perfect number or not

n = int(input("Enter any number : "))

sum = 0

for i in range (1, n):
    if(n%i == 0):
        sum = sum+i
if(sum == n):
    print("Entered number is a perfect number.")
else:
    print("Entered number is not a perfect number.")