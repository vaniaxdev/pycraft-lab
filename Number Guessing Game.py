import random

print("===== NUMBER GUESSING GAME =====")
print("I have chosen a number between 1 and 20.")

secret_number = random.randint(1, 20)
attempts = 0

while True:
    guess = int(input("Enter your guess: "))
    attempts += 1

    if guess < secret_number:
        print("Too low! Try again.")

    elif guess > secret_number:
        print("Too high! Try again.")

    else:
        print("Congratulations! You guessed correctly!")
        print("The secret number was:", secret_number)
        print("Number of attempts:", attempts)
        break

