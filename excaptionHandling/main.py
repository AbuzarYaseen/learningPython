a = int(input("Enter any number : "))

try: 
    print(10/a)
except Exception as err:
    print(f"Sorry there is an err as {err}")

print("ok I've done the division")