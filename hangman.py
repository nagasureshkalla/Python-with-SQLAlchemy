"""
HW 2
Problem 3
Author : Kalla Naga Suresh

"""

import random  # Import the random module to choose a word randomly from the list

# List of words for the game
words = ["write", "that", "program", "hangman", "python", "coding", "challenge"]

# Function to choose a random word from the list
def choose_word():
    return random.choice(words)

# Function to display the word with guessed letters
def display_word(word, guessed_letters):
    displayed = ""
    for letter in word:
        if letter in guessed_letters:
            displayed += letter
        else:
            displayed += "*"
    return displayed

# Main game function
if __name__ == "__main__":
    play_again = "y"

    while play_again.lower() == "y":
        word = choose_word()  # Choose a random word from the list
        guessed_letters = []  # Initialize an empty list for guessed letters
        misses = 0  # Initialize the misses count
        print("Try to guess the word letter by letter.")

        while True:
            current_display = display_word(word, guessed_letters)  # Display the current state of the word
            print(f"(Guess) Enter a letter in word {current_display}")
            guess = input("> ").lower()  # Get the user's letter guess and convert it to lowercase

            if len(guess) != 1 or not guess.isalpha():  # Check if the input is a single letter
                print("Please enter a single letter.")
                continue

            if guess in guessed_letters:  # Check if the letter has already been guessed
                print(f"{guess} is already in the word.")
            elif guess in word:  # Check if the guess is correct
                guessed_letters.append(guess)  # Add the guessed letter to the list
                if set(guessed_letters) == set(word) or len(guessed_letters)==len(word):  # Check if all letters have been guessed
                    print(f"The word is {word}. You missed {misses} time")
                    break
            else:
                guessed_letters.append(guess)  # Add the guessed letter to the list
                misses += 1  # Increment the misses count
        play_again = input("Do you want to guess another word? Enter y or n> ")