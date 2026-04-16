# Sum upto n numbers

n = int(input("Enter any number : "))

a = 11
a+=1
sum = 0
for i in range(1, n+1):
    sum = i+sum
    
print(sum)