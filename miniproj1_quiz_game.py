print("Welcome to the football quiz")

answer = input("do you want to continue? ")
if answer.lower() != "yes":
    quit()

score = 0

answer = input(" i)Who is the GOAT? ")
if answer.lower() == "cristiano ronaldo":
    print("you got that correct")
    score+=1
else :
    print("you got that incorrect")

answer = input("ii) Who won the ballon d'or 6 times? ")
if answer.lower() == "cristiano ronaldo":
    print("you got that correct")
    score+=1
else :
    print("you got that incorrect")

answer = input("iii) Who is the other GOAT? ")
if answer.lower() == "lionel messi":
    print("you got that correct")
    score+=1
else :
    print("you got that incorrect")

answer = input("iv) Who is the best young talent currently? ")
if answer.lower() == "kylian mbappe":
    print("you got that correct")
    score+=1
else :
    print("you got that incorrect")

answer = input("Who is the best young talent at Real Madrid? ")
if answer.lower() == "vinicius juniour":
    print("you got that correct")
    score+=1
else :
    print("you got that incorrect")

print("You got " + str(score) + " out of 5 questions correct")
print("Thanks for playing HALA MADRID!!")


