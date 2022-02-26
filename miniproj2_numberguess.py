import random

number_ceil = input("Enter a number: ")

if number_ceil.isdigit():
    number_ceil = int(number_ceil)
    if number_ceil <= 0:
        print("enter a number greater than 0")
        quit()
else:
    print("enter a number please")
    quit()

random_number = random.randint(0, number_ceil)
guess_count=0
guess_limit=5

while True:
    if guess_count >= guess_limit:
        print("you ran out of guesses!! Try Again!!")
        quit()
    guess_count += 1
    user_guess = input("make a guess")
    if user_guess.isdigit():
        user_guess = int(user_guess)
    if user_guess == random_number:
        print("you got it")
        break
    elif user_guess > random_number:
        print("guess lower")
    else:
        print("guess higher")
        continue

print("you got it in", guess_count,"guesses" )
