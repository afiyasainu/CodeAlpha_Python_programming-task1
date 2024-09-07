import random

# List of possible words
WORDS = ["python", "hangman", "challenge", "programming", "developer", "algorithm", "function", "variable", "exception", "inheritance"]

# Hangman stages
HANGMAN_PICS = [
    """
      +---+
          |
          |
          |
         ===
    """,
    """
      +---+
      O   |
          |
          |
         ===
    """,
    """
      +---+
      O   |
      |   |
          |
         ===
    """,
    """
      +---+
      O   |
     /|   |
          |
         ===
    """,
    """
      +---+
      O   |
     /|\\  |
          |
         ===
    """,
    """
      +---+
      O   |
     /|\\  |
     /    |
         ===
    """,
    """
      +---+
      O   |
     /|\\  |
     / \\  |
         ===
    """
]

def get_random_word():
    """Returns a random word from the WORDS list."""
    return random.choice(WORDS)

def display_current_progress(word, guessed_letters):
    """Displays the current progress of the word being guessed."""
    return " ".join([letter if letter in guessed_letters else "_" for letter in word])

def hangman():
    word_to_guess = get_random_word()
    guessed_letters = set()
    incorrect_guesses = set()
    attempts_remaining = len(HANGMAN_PICS) - 1

    print("Welcome to Hangman!")

    while attempts_remaining > 0:
        print(HANGMAN_PICS[len(HANGMAN_PICS) - attempts_remaining - 1])
        print(f"Word to guess: {display_current_progress(word_to_guess, guessed_letters)}")
        print(f"Incorrect guesses: {' '.join(sorted(incorrect_guesses))}")
        print(f"Attempts remaining: {attempts_remaining}")

        guess = input("Guess a letter: ").lower()

        if len(guess) != 1 or not guess.isalpha():
            print("Invalid input. Please enter a single letter.")
            continue

        if guess in guessed_letters or guess in incorrect_guesses:
            print("You've already guessed that letter. Try again.")
            continue

        if guess in word_to_guess:
            guessed_letters.add(guess)
            print(f"Good guess! '{guess}' is in the word.")
            if all(letter in guessed_letters for letter in word_to_guess):
                print(f"Congratulations! You guessed the word '{word_to_guess}'!")
                break
        else:
            incorrect_guesses.add(guess)
            attempts_remaining -= 1
            print(f"Sorry, '{guess}' is not in the word.")

        if attempts_remaining == 0:
            print(HANGMAN_PICS[-1])
            print(f"Game Over! The word was '{word_to_guess}'.")

if __name__ == "__main__":
    hangman()
