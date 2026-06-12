# Create a random number guessing game.

import random

num = random.randint(1,100)
userTries = 0



while True:
    guess = int(input("Guess your number between 1-100 : "))

    if num == guess:
        print("Number guessed successfully")
        print(f"Total tries taken : {userTries}")
        break

    elif num < guess:
        print("Entered number is greater")
        userTries = userTries+1
    elif num > guess:
        print("Entered number is smaller")
        userTries = userTries+1
    else:
        userTries = userTries+1
        print("Your are wrong")
        print(f"Tries taken : {userTries}")

