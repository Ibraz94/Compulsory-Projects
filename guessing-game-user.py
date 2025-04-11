import random

def play_guessing_game():
    # Generate a random number between 1 and 100
    secret_number = random.randint(1, 100)
    attempts = 0
    
    print("Welcome to the Number Guessing Game!")
    print("I'm thinking of a number between 1 and 100.")
    
    while True:
        try:
            # Get user's guess
            guess = int(input("\nEnter your guess: "))
            attempts += 1
            
            # Check if the guess is correct
            if guess < secret_number:
                print("Too low! Try a higher number.")
            elif guess > secret_number:
                print("Too high! Try a lower number.")
            else:
                print(f"\nCongratulations! You've guessed the number {secret_number} correctly!")
                print(f"It took you {attempts} attempts.")
                break
                
        except ValueError:
            print("Please enter a valid number between 1 and 100.")

if __name__ == "__main__":
    play_guessing_game() 