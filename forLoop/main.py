# range function accepts 3 things
# (start, stop, steps)
# range function is used in for loops

# Print from 1 to 20 using range function
# for i in range(1, 21):
#     print(i)

# # Print from 16 to 1
# for i in range(16, 0, -1):
#     print(i)

# Print from -3 to -15
# for i in range(-3, -16, -1):
#     print(i)

# accept number from user and print that table
# n = int(input("Enter number to print its table : "))
# for i in range(n , (n*10)+1, n):
#     print(i)

# Loops for strings
a = "Abuzar"


for i in range(0, len(a), 1):
    print(a[i])


x = "Abuzar is learning python"
for i in x:
    print(i)