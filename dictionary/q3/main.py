# Count the frequency of each element in list

x = [1,1,1,2,4,5,7,6,4,3,21,12,3,1,3,5,6,4]

dict = {}

for i in x:
    if i in dict.keys():
        dict[i] += 1
    else:
        dict[i] = 1

print(dict)

