#GENERATE A RANDOM NUMBER
import random

random_number = random.randint(1,100)

max_try = 7
current_try = 0
guess_history = []


#START GUSSING THE NUMBER
while current_try < max_try:

    if guess_history:
        print(f"Your guess history so far: {guess_history}")
        print("=" * 50)

    number_guess = input("please guess a number below 100: ")     #ASK THE USER TO INPUT A NUMBER
    number_guess = int(number_guess)

    if number_guess in guess_history:
        print("You have already guessed this number")
        continue
        print("-" * 50)

    if number_guess > random_number:
        print("Too High")
        current_try += 1
        guess_history.append(number_guess)
        print(f"current_try = {current_try}")
        print("-" * 50)
    elif number_guess < random_number:
        print("Too Low")
        current_try += 1
        guess_history.append(number_guess)
        print(f"current_try = {current_try}")
        print("-" * 50)
    else:
        print("Succeed")
        break

else:
    print("Game Over")
    print(f"The number is {random_number}")
    print(f"Your guess were {guess_history}")

print("Thanks for participating the game!")



