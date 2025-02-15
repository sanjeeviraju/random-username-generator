import random
import os
import sys

# Constants
SPECIAL_CHARS = ['!', '@', '#', '$', '%', '^', '&', '*', '?', '-']
DEFAULT_ADJECTIVES = [
    'quick', 'lazy', 'happy', 'silly', 'brave', 'calm', 'eager', 'gentle', 'jolly', 'kind',
    'bold', 'clever', 'daring', 'witty', 'merry', 'noble', 'proud', 'fierce', 'lively', 'wild',
    'quiet', 'swift', 'tough', 'vivid', 'zesty', 'angry', 'busy', 'chill', 'dapper', 'epic',
    'fancy', 'gloomy', 'hasty', 'icy', 'jovial', 'keen', 'mighty', 'nifty', 'odd', 'peppy',
    'quirky', 'radiant', 'sly', 'tricky', 'upbeat', 'vivid', 'witty', 'excited', 'young', 'zealous'
]
DEFAULT_NOUNS = [
    'tiger', 'dragon', 'eagle', 'wolf', 'bear', 'shark', 'phoenix', 'lion', 'fox', 'owl',
    'panther', 'raven', 'hawk', 'falcon', 'viper', 'scorpion', 'rhino', 'buffalo', 'goat', 'snake',
    'spider', 'knight', 'wizard', 'giant', 'thief', 'pirate', 'ninja', 'samurai', 'mage', 'warrior',
    'king', 'queen', 'prince', 'princess', 'robot', 'alien', 'ghost', 'zombie', 'vampire', 'demon',
    'angel', 'dwarf', 'elf', 'orc', 'goblin', 'troll', 'sphinx', 'griffin', 'unicorn', 'pegasus',
    'gladiator', 'sorcerer', 'assassin', 'monk', 'cleric', 'bard', 'ranger', 'paladin', 'berserker',
    'necromancer', 'warlock', 'archer', 'captain', 'commander', 'jester', 'merchant', 'smith', 'alchemist'
]

def load_words(filename):
    """Load words from a file or return None if not found."""
    try:
        with open(filename, 'r') as file:
            return [line.strip().lower() for line in file if line.strip()]
    except FileNotFoundError:
        return None

def generate_username(adjectives, nouns, use_numbers, num_digits, use_special):
    """Generate a single username with given parameters."""
    adjective = random.choice(adjectives).capitalize()
    noun = random.choice(nouns).capitalize()
    username = adjective + noun
    
    if use_numbers:
        max_num = 10 ** num_digits - 1
        numbers = str(random.randint(0, max_num)).zfill(num_digits)
        username += numbers
    
    if use_special:
        username += random.choice(SPECIAL_CHARS)
    
    return username

def get_int_input(prompt, min_val=0, max_val=None):
    """Get validated integer input from user."""
    while True:
        try:
            value = int(input(prompt))
            if value < min_val:
                print(f"Value must be at least {min_val}.")
            elif max_val is not None and value > max_val:
                print(f"Value must be at most {max_val}.")
            else:
                return value
        except ValueError:
            print("Please enter a valid integer.")

def get_yes_no_input(prompt):
    """Get yes/no input from user."""
    while True:
        response = input(prompt).strip().lower()
        if response in ('y', 'yes'):
            return True
        elif response in ('n', 'no'):
            return False
        else:
            print("Please enter 'y' or 'n'.")

def save_to_file(usernames):
    """Save generated usernames to a file."""
    # Get the directory where the script is located
    script_dir = os.path.dirname(os.path.abspath(__file__))
    
    while True:
        filename = input("\nEnter filename to save (or Enter to skip): ").strip()
        if not filename:
            return
        if not filename.lower().endswith('.txt'):
            filename += '.txt'
            
        # Create full path in same directory as script
        filepath = os.path.join(script_dir, filename)

        mode = 'w'
        if os.path.exists(filepath):
            overwrite = get_yes_no_input(f"'{filename}' exists. Overwrite? (y/n): ")
            if not overwrite:
                append = get_yes_no_input("Append to file? (y/n): ")
                mode = 'a' if append else 'w'

        try:
            with open(filepath, mode) as file:
                for uname in usernames:
                    file.write(uname + '\n')
            print(f"Saved {len(usernames)} usernames to {filepath}")
            break
        except IOError as e:
            print(f"Error saving file: {e}. Try another name.")

def main():
    print("=== Random Username Generator ===")
    print("Creates unique gaming/social media usernames\n")
    
    # Load word lists
    adjectives = load_words('adjectives.txt') or DEFAULT_ADJECTIVES
    nouns = load_words('nouns.txt') or DEFAULT_NOUNS
    
    if not adjectives or not nouns:
        print("Error: Missing word lists!", file=sys.stderr)
        sys.exit(1)
    
    # Get user preferences
    num = get_int_input("Number of usernames to generate (1-1000): ", 1, 1000)
    use_nums = get_yes_no_input("Include numbers? (y/n): ")
    num_digits = 0
    if use_nums:
        num_digits = get_int_input("Number of digits (1-4): ", 1, 4)
    use_special = get_yes_no_input("Include special characters? (y/n): ")
    
    # Generate unique usernames
    generated = set()
    attempts = 0
    max_attempts = num * 100  # Prevent infinite loop
    
    while len(generated) < num and attempts < max_attempts:
        attempts += 1
        username = generate_username(adjectives, nouns, use_nums, num_digits, use_special)
        generated.add(username)
    
    # Display results
    print("\n=== Generated Usernames ===")
    for i, uname in enumerate(generated, 1):
        print(f"{i}. {uname}")
    
    # Save to file
    save_to_file(generated)

if __name__ == "__main__":
    main()