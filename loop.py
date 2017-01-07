import random

print("Welcome To Guess the Number! Please select a number from 1 to 6")

y = random.randint(1,6)

while True:
    x = int(input("Please input a Number: "))
    if x != y:
        print("You did not guess the correct number!")
    elif x == y:
        print("You guessed the correct number!")
        break

