# HANGMAN GAME BY PYTHON

import random
from words import words_list

def get_random_word():
    words = random.choice(words_list)
    return words.lower()

def display_words(word , guess_letter):
    result = []
    for letter in word:
        if letter in guess_letter:
            result.append(letter)

        else:
            result.append("_")
    return " _" .join(result)

def hangman():
    word = get_random_word()
    guess_letter = []
    lifes = 6 

    print("🎮 Welcome to Hangman!")
    print("_ " * len(word))

    while lifes > 0 :
        print(" ")
        print("Words:" + display_words(word , guess_letter))
        print("Lifes left :", lifes)
        guess = input("Guess a letter: ").lower()

        if len(guess) != 1 or not guess.isalpha():
            print("❗ Please enter one valid letter.")
            continue

        if guess in guess_letter:
            print("You already guessed that letter.")
            continue

        guess_letter.append(guess)

        if guess in word :
            print("✅ Good guess!")
        else :
            print("❌ Wrong guess.")
            lifes = lifes - 1

        all_guessed = True
        for letter in word:
            if letter not in guess_letter:
                all_guessed = False
                break

        if all_guessed:
            print("")
            print("You won! The word was:🎉 ", word)
            break

        if lifes == 0:
            print("")
            print("You died! The word was:💀 ", word)

if __name__ == "__main__":
    hangman()





