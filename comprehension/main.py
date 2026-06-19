l = []

for i in range(1, 21):
    if i%2 == 0:
        (l.append(i))

print(l)

# Above lines can also be written as below and this is list comprehension

l1= [i for i in range(1,41) if i%2 == 0]


print(l1)

# Below is dictionary comprehension

l2 = {i : i**2 for i in range(1,21) if i%2 == 0}

print(l2)