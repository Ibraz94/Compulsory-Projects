import random
import os

def clear_screen():
    os.system('cls' if os.name == 'nt' else 'clear')

def get_random_word():
    words = [
        "python", "programming", "computer", "keyboard", "mouse",
        "monitor", "internet", "software", "hardware", "algorithm",
        "database", "network", "security", "developer", "application"
    ]
    return random.choice(words)

def display_hangman(tries):
    stages = [
        """
           --------
           |      |
           |      O
           |     \\|/
           |      |
           |     / \\
           -
        """,
        """
           --------
           |      |
           |      O
           |     \\|/
           |      |
           |     /
           -
        """,
        """
           --------
           |      |
           |     \\|/
           |      |
           |      |
           |
           -
        """,
        """
           --------
           |      |
           |      O
           |     \\|
           |      |
           |
           -
        """,
        """
           --------
           |      |
           |      O
           |      |
           |      |
           |
           -
        """,
        """
           --------
           |      |
           |      O
           |
           |
           |
           -
        """,
        """
           --------
           |      |
           |
           |
           |
           |
           -
        """
    ]
    return stages[tries]

def play_hangman():
    word = get_random_word()
    word_letters = set(word)
    alphabet = set('abcdefghijklmnopqrstuvwxyz')
    used_letters = set()
    tries = 6

    while len(word_letters) > 0 and tries > 0:
        clear_screen()
        print(display_hangman(tries))
        print("\nWord: ", end="")
        for letter in word:
            if letter in used_letters:
                print(letter, end=" ")
            else:
                print("_", end=" ")
        
        print("\n\nUsed letters: ", " ".join(used_letters))
        print(f"Tries left: {tries}")
        
        user_letter = input("\nGuess a letter: ").lower()
        
        if user_letter in alphabet - used_letters:
            used_letters.add(user_letter)
            if user_letter in word_letters:
                word_letters.remove(user_letter)
            else:
                tries -= 1
                print("\nWrong letter!")
        elif user_letter in used_letters:
            print("\nYou've already used that letter!")
        else:
            print("\nInvalid input! Please enter a single letter.")
        
        input("\nPress Enter to continue...")
    
    clear_screen()
    if tries == 0:
        print(display_hangman(tries))
        print(f"\nYou lost! The word was: {word}")
    else:
        print(f"\nCongratulations! You won! The word was: {word}")

def main():
    while True:
        clear_screen()
        print("Welcome to Hangman!")
        print("1. Play Game")
        print("2. Exit")
        
        choice = input("\nEnter your choice (1-2): ")
        
        if choice == "1":
            play_hangman()
        elif choice == "2":
            print("\nThanks for playing! Goodbye!")
            break
        else:
            print("\nInvalid choice! Please try again.")
            input("\nPress Enter to continue...")

if __name__ == "__main__":
    main()
