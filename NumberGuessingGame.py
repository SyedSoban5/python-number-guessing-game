import random

def playgame():

    number = random.randint(1, 100)
    print("---- Number Guessing Game ----")

    count = 5

    while count > 0:
        guess = int(input("Enter your guess: "))

        if guess == number:
            print("Correct! You won!")
            break
        elif guess > number:
            print("Too high!")
        else:
            print("Too low!")

        count -= 1
        print("Remaining attempts:", count)

    if count == 0:
        print("You lose!")

    print("The random number was:", number)

playgame()