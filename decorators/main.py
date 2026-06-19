# Decorators example
def decorate(func):
    def wrapper(*x, **y):
        print("THe substraction to your numbers are  ")
        func(*x, **y)
        print("thank you, hope you liked it")

    return wrapper

@decorate
def substraction(*a, **b):
    print(f"Your answer is {a - b} ")

substraction(12, 43)

# args are for accepting multiple/unknown arguments from users and * is the representing symbol
def addition(*args):
    sum = 0
    for i in args:
        sum = sum+i

    return sum


print(addition(12,21,432,54,65))

# kewords arguments are for accepting multiple kay valye pair arguments and ** is the representing symbol

def information(**kwargs):
    print("Your info is : \n\n")
    for i in kwargs:
        print(f"{i} : {kwargs[i]}")


information(name = "Abuzar", age =12, role="Engineer") 