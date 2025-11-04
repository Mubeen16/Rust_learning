import random

print("Guess the number!")

# Step 1: generate random number between 1 and 100
secret_number = random.randint(1, 100)

# Uncomment this line for testing
print(f"(Debug) The secret number is: {secret_number}")

while True:
    # Step 2: ask user for input
    guess = input("Please input your guess: ")

    # Step 3: handle invalid input
    if not guess.isdigit():
        print("Please type a number!")
        continue

    guess = int(guess)

    # Step 4: compare with secret number
    if guess < secret_number:
        print("Too small!")
    elif guess > secret_number:
        print("Too big!")
    else:
        print("You win!")
        break
