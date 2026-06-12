# Accept a number and check weather it is a pallendrome or not

x = int(input("Enter any number : "))

originalNmbr = x

rev = 0

while x > 0:
    rev = rev*10 + x % 10
    x = x // 10

print(rev)

if(originalNmbr == rev):
    print("Entered number is a pallendrome")
else:
    print("Entered number is not a pallendrome")
