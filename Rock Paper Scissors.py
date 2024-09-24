import random
options=[ "Rock","Paper", "Scissors"]
user_choice=input("Choose Rock,Paper,or Scissors:")
computer_choice=random.choice(options)
print("You chose:", user_choice)
print("Computer chose", computer_choice)

if user_choice==computer_choice:
    print("It is a tie")

elif user_choice=="Rock" and computer_choice=="Scissors":
    print("Rock smashes paper you win!")
elif user_choice=="Scissors" and computer_choice=="Paper":
    print("Scissors cut Paper you win!")
elif user_choice=="Paper" and computer_choice=="Rock":
    print("Paper covers Rock you win!")
else:
    print("You lose!")