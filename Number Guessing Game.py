import random

secret_number = random.randint(1, 20)
max_attempts = 3
attempts = 0

print("Guess the number between 1 and 20")
print(f"You have {max_attempts} attempts")

while attempts < max_attempts:
    guess = int(input("Enter your guess: "))
    attempts += 1

    if guess == secret_number:
        print(f"Correct Guessed")
        break
    elif guess < secret_number:
        print("Too low!")
    else:
        print("Too high!")

#condition for game over 
if attempts == max_attempts and guess != secret_number:
    print("Game Over!")
    print(f"The correct number was {secret_number}")
