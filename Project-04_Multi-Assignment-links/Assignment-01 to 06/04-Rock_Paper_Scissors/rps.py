
# rock beats scissors 
# scissors beats paper
# paprer beats rock

import random

choices : list[str] = ["rock" , "paper" , "scissors"]

while True:
    user_chioce = input('Enter "rock" , "paper" , "scissors" and ("q for quite")": ').lower()

    if user_chioce == "q":
        print("Game Over. Thanks for playing! 😊")
        break
    
    if user_chioce not in choices:
        print("Invaild input! please Try again..")
        continue

    
    computer_choice = random.choice(choices)
    print(f"Computer Choice : {computer_choice}")

    if computer_choice == user_chioce:
        print("It's a  Tie!😕")

    elif (user_chioce == "rock" and computer_choice == "scissors") or \
         (user_chioce == "scissors" and computer_choice == "paper") or\
         (user_chioce == "paper" and computer_choice == "rock"):
        print("Yay ! You win 🎉")

    else:
        print("You loss!😢")

    print("-" * 30)
