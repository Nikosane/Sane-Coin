from text_file_processor import generate_chunks
from encryption import encrypt_chunks, decrypt_chunks
from key_generator import generate_random_key
from word_selector import select_word
from game_logic import start_game

def main():
    # Load words and generate chunks
    words = generate_chunks("words.txt")
    
    # Generate a random encryption key
    encryption_key = generate_random_key()
    
    # Encrypt chunks
    encrypted_chunks = encrypt_chunks(words, encryption_key)
    
    # Select a random word as the desired word
    desired_word = select_word(words)
    
    # Start the game logic
    start_game(encrypted_chunks, desired_word)

if __name__ == "__main__":
    main()
