# Sort the list in ascending order


x = [12, 10, 32, 33, 43, 11]

temp = x[0]

for i in range(len(x)):
    for j in range(len(x)-1):
        if x[j] > x[j+1]:
            temp = x[j]
            x[j] = x[j+1]
            x[j+1] = temp
print(x)
