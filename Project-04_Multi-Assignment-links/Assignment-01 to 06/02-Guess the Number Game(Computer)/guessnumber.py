# Guess the Number Game Python project(Computer) by Laiba Naz
import random

select_number = random.randint(1 ,20)

while True:
    guess = int(input("Guess a number between 1 , 20:\n" ))

    if guess > select_number:
        print("Please try again..Its too high! \n")

    elif guess < select_number:
        print("Please try again.. Its too Low!\n")

    else:
        print(f"\nCongratulations! You guessed the number {guess} correctly!🎉🎉\n")
        break
    

