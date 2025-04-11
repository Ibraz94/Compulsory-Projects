import random

def computer_guessing_game():
    # Generate a random number between 1 and 100
    target_number = random.randint(1, 100)
    print(f"Computer has generated a random number between 1 and 100.")
    
    # Initialize variables for binary search
    low = 1
    high = 100
    attempts = 0
    
    while True:
        # Computer makes a guess using binary search
        guess = (low + high) // 2
        attempts += 1
        
        print(f"\nComputer's guess #{attempts}: {guess}")
        
        if guess == target_number:
            print(f"Computer found the number {target_number} in {attempts} attempts!")
            break
        elif guess < target_number:
            print("Too low!")
            low = guess + 1
        else:
            print("Too high!")
            high = guess - 1

if __name__ == "__main__":
    print("Welcome to the Computer Number Guessing Game!")
    print("The computer will try to guess a random number between 1 and 100.")
    computer_guessing_game()
