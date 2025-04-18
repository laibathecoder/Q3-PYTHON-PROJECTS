import random
import string

print("Welcome to your Password Generator")

lenght = int(input("Enter the lenght of your password please: "))
paswrd_number = int(input("Enter the amount of passwords to generate: "))


latters = string.ascii_letters
digits = string.digits
symbols = string.punctuation

all_chars = latters + digits + symbols


for user_input in range(paswrd_number):
    password : str = ""
    for amount in range(lenght):
        random_chars = random.choice(all_chars)
        password += random_chars

    print(f"\nYour Generated Passwords: {password}")



