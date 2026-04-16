# Print factorial of a number

n = int(input("Enter number to print its factorial: "))

fact = 1

for i in range(n, 1, -1):
    fact = fact*i
    
print(f"factorial of {n} = {fact}")