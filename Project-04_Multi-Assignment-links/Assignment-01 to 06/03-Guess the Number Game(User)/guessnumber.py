import random

low = 1 
high = 20
feedback = ""

print("\nThink a number between 1 to 20 then Computer will guess it :\n")

while True:
    if feedback != "yes":
        guess = random.randint(low , high)
        print(f"Computer Guess is {guess}\n")
    
    feedback = input(f"Is this {guess} is (H) 'too high' ? or is this {guess} is (L) 'too low' ? or (C) 'correct'? 'yes': ").lower()


    if feedback == "l":
        low = guess +1
        
    elif feedback == "h":
        high = guess -1
    
    elif feedback == "c":
        print("\nWaoo! Computer guessed the correct number! 👍\n")
        break        


        

