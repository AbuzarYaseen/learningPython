# Check wether the number is prime or not

n = int(input("Enter any number : "))
count = 0

for i in range(1, n+1):
    if(n % i == 0):
        count = count+1

if(count < 3):
    print("Entered number is a prime number")
else:
    print("Entered number is not a prime number")
