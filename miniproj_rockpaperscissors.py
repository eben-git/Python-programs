import random

user_win = 0
ai_win = 0
r_draw = 0

options = ["rock", "paper", "scissors"]

while True:
    user_input = input("pick rock/paper/scissors or q to quit: ").lower()
    if user_input == "q":
        break
    elif user_input not in options:
        continue

    random_number = random.randint(0,2)
    # rock=0,paper=1,scissors=2
    ai_input = options[random_number]
    print("Computer picked", ai_input + ".")

    if user_input == "rock" and ai_input == "scissors":
        print("you win")
        user_win += 1

    elif user_input == "paper" and ai_input == "rock":
        print("you win")
        user_win += 1

    elif user_input == "scissors" and ai_input == "paper":
        print("you win")
        user_win += 1

    elif user_input == ai_input:
        print("it was a draw")
        r_draw += 1

    else :
        print("AI wins")
        ai_win += 1

print("you won", user_win, "times.")
print("AI won", ai_win, "times.")
print("you drew", r_draw, "times.")
print("goodbye")

