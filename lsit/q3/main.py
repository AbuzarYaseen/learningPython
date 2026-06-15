# Find the grater number in the list

x = [12, 32, 33, 43, 11]

greater = x[0]
index = 0

for i in range(len(x)):
    if x[i] > greater:
        greater = x[i]
        index = i

print(f"Index containing largest value : {index}")
