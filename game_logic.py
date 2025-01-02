import random
import os
import time
from pyfiglet import figlet_format

# Helper Functions
def slow_print(text, delay=0.05):
    for char in text:
        print(char, end='', flush=True)
        time.sleep(delay)
    print()

def clear_screen():
    os.system('cls' if os.name == 'nt' else 'clear')

# Load words from words.txt
def load_words():
    try:
        with open('words.txt', 'r') as file:
            words = [line.strip() for line in file.readlines() if len(line.strip()) >= 6]
        return words
    except FileNotFoundError:
        print("Error: 'words.txt' file not found. Make sure it is in the same directory.")
        exit()

def split_into_chunks(word):
    chunk_size = len(word) // 6
    chunks = [word[i:i+chunk_size] for i in range(0, 6 * chunk_size, chunk_size)]
    return chunks

def generate_keys():
    return [f"key{i}" for i in range(1, 7)]

def associate_keys_with_chunks(keys, chunks):
    random.shuffle(keys)
    random.shuffle(chunks)
    return dict(zip(keys, chunks))

# Main Game Logic
def play_game():
    clear_screen()
    print(figlet_format("Chunk Encryption", font="slant"))

    words = load_words()
    slow_print("Welcome to the Chunk Encryption Game!\n")

    slow_print("Select a word from the list to play:\n")
    for idx, word in enumerate(words[:10], start=1):
        print(f"{idx}. {word}")

    selected_word = None
    while not selected_word:
        try:
            choice = int(input("Enter the number corresponding to your chosen word: "))
            if 1 <= choice <= len(words[:10]):
                selected_word = words[choice - 1]
            else:
                print("Invalid choice. Please select a valid number.")
        except ValueError:
            print("Invalid input. Please enter a number.")

    slow_print(f"You selected: {selected_word}\n")

    # Split word into chunks
    chunks = split_into_chunks(selected_word)

    # Generate keys and associate them randomly with chunks
    keys = generate_keys()
    key_chunk_map = associate_keys_with_chunks(keys, chunks)

    slow_print("The word has been split into 6 chunks and encrypted with random keys.\n")
    slow_print("Now, select 3 keys to decrypt their corresponding chunks.\n")

    random.shuffle(keys)  # Shuffle keys for user selection

    print("Available keys:")
    for key in keys:
        print(key, end='  ')
    print()

    selected_keys = []
    while len(selected_keys) < 3:
        key = input(f"Select key {len(selected_keys) + 1}: ").strip()
        if key in keys and key not in selected_keys:
            selected_keys.append(key)
        else:
            print("Invalid or duplicate key. Please try again.")

    slow_print("\nDecrypting selected keys...\n")

    for key in selected_keys:
        chunk = key_chunk_map[key]
        slow_print(f"{key} decrypts to chunk: {chunk}")

    slow_print("\nThe game is based on luck. Did you uncover meaningful parts of the word?\n")
    slow_print("Thank you for playing!\n")

if __name__ == "__main__":
    play_game()
