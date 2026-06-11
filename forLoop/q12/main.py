# Check if a string is pallindrome or not

a = input("Enter any string : ")

b = ""

for i in range(len(a)-1, -1, -1):
    b = b + a[i]

if a == b:
    print("Entered string is a palindrome")
else:
    print("Entered string is not a palindrome")