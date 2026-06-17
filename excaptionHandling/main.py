a = int(input("Enter any number : "))

try: 
    print(10/a)
except Exception as err:
    print(f"Sorry there is an err as {err}")

print("ok I've done the division")

# raise throughs manually error

age = int(input("Enter your age : "))

try:
    if age < 10 or age > 18:
        raise ValueError("your age must be in between 10-18")
    else:
        print("Your are allowed to get the adminssion")
except Exception as err:
    print(f"an error occured as {err}")