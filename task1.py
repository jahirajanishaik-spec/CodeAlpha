import random

def play_hangman():
    # List of 5 predefined words
    words = ["python", "code", "alpha", "intern", "developer"]
    word_to_guess = random.choice(words)
    guessed_letters = []
    incorrect_guesses = 0
    max_incorrect = 6

    print("Welcome to Hangman!")
    print(f"You have {max_incorrect} incorrect guesses allowed.")

    while incorrect_guesses < max_incorrect:
        # Display current word progress
        display_word = "".join([letter if letter in guessed_letters else "_" for letter in word_to_guess])
        print(f"\nWord: {display_word}")

        if display_word == word_to_guess:
            print("Congratulations! You guessed the word correctly!")
            break

        guess = input("Guess a letter: ").lower()

        if len(guess) != 1 or not guess.isalpha():
            print("Please enter a single valid alphabetical letter.")
            continue

        if guess in guessed_letters:
            print("You already guessed that letter. Try a different one.")
            continue

        guessed_letters.append(guess)

        if guess in word_to_guess:
            print(f"Good job! '{guess}' is in the word.")
        else:
            incorrect_guesses += 1
            print(f"Incorrect! '{guess}' is not in the word. Remaining incorrect guesses: {max_incorrect - incorrect_guesses}")

    else:
        print(f"\nGame Over! The word was: {word_to_guess}")

if __name__ == "__main__":
    play_hangman()