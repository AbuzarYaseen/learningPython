# Print positive and negative elements of an list

l = [-23, -32, -43, 45, 64, -23]

print("Positive numbers are : ")
for i in l:
    if(i >= 0):
        print(i)
    
print("Negative number are : ")
for i in l:
    if(i < 0):
        print(i)