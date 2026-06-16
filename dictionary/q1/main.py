# Write a script to merge two python dictionaries

d1 = {1:20, 2:30, 4:40}
d2 = {4:50, 5: 60, 6:70}

for i in d2:
    if i in d1.keys():
        d1[i] += d2[i]
    else:
        d1[i] = d2[i]

print(d1)