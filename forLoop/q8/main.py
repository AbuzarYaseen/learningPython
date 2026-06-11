# Accept a number and check if it is a perfect number or not.

n = int(input("Which number factors you want to find : "))

for i in range (1, n+1):
    if(n % i == 0):
        print(i)
    
