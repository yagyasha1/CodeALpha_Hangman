
import random

# Step 1: Create a list of 5 words
words = ["python", "apple", "computer", "school", "coding"]

# Step 2: Select a random word
word = random.choice(words)

# Step 3: Create variables
guessed_letters = []
incorrect_guesses = 0
max_attempts = 6

print("===== WELCOME TO HANGMAN GAME =====")

# Step 4: Start the game
while incorrect_guesses < max_attempts:

    # Display the guessed word
    display_word = ""

    for letter in word:
        if letter in guessed_letters:
            display_word += letter + " "
        else:
            display_word += "_ "

    print("\nWord:", display_word)
    print("Incorrect guesses:", incorrect_guesses)
    print("Attempts left:", max_attempts - incorrect_guesses)

    # Check whether the word is complete
    if all(letter in guessed_letters for letter in word):
        print("\nCongratulations! You guessed the word:", word)
        break

    # Step 5: Take input from the player
    guess = input("Guess a letter: ").lower()

    # Validate input
    if len(guess) != 1 or not guess.isalpha():
        print("Please enter only one alphabet!")
        continue

    if guess in guessed_letters:
        print("You already guessed this letter!")
        continue

    guessed_letters.append(guess)

    # Step 6: Check the guess
    if guess in word:
        print("Correct guess!")
    else:
        print("Wrong guess!")
        incorrect_guesses += 1

# Step 7: Check game result
if incorrect_guesses == max_attempts:
    print("\nGame Over! You lost.")
    print("The correct word was:", word)

print("\n===== THANK YOU FOR PLAYING =====")
