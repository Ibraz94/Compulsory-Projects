def get_word(prompt):
    """Get a word from the user with validation."""
    while True:
        word = input(prompt).strip()
        if word:
            return word
        print("Please enter a word!")

def main():
    print("Welcome to Mad Libs!")
    print("Please provide the following words:\n")
    
    # Get words from the user
    adjective = get_word("Enter an adjective: ")
    noun = get_word("Enter a noun: ")
    verb = get_word("Enter a verb: ")
    adverb = get_word("Enter an adverb: ")
    
    # The story template
    story = f"""
    Once upon a time, there was a {adjective} {noun}.
    It loved to {verb} {adverb} every day.
    The end.
    """
    
    print("\nHere's your Mad Libs story:")
    print(story)

if __name__ == "__main__":
    main()
