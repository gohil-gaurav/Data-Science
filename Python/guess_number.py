import random 

num = random.randint(1, 100)
tries = 0
guess = -1


while guess != num:
    guess = int(input("Guess a number between 1 nd 100: "))
    if guess > num:
        print("Your guess is above the number.")
        tries += 1
    elif guess < num:
        print("Your guess is below the number.")
        tries += 1
    else:
        print("You guessed the number.")
        tries += 1

print(f"You found the number {num} in {tries} tries.")
