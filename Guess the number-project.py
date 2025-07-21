import random

def guess_my_number():
    print("Welcome to Guess My Number")
    print("I'm thinking of a number between 1 and 30.")
    secret_number = random.randint(1, 30)
    attempts = 0
    max_attempts = 5
    while attempts < max_attempts:
     try:
         guess = int(input("Enter your guess:"))
         attempts += 1
         if guess < secret_number:
            print("Too low")
         elif guess > secret_number:
             print("Too high")
         else:
            print(f"Correct You guessed it in {attempts} attempts")
            break
     except ValueError:
        print("Please enter a valid number")
    else:
        print(f"You've used all {max_attempts} attempts. The number was {secret_number}")
guess_my_number()

