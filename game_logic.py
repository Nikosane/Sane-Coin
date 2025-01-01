import random
import hashlib

def terminal_display():
    print("=================== Welcome to Sane Coin Mine! =========================")


def load_words(filename):
    """Load words from a file and return a list of words."""
    with open(filename, 'r') as file:
        words = file.read().splitlines()  # Assuming words are one per line
    return words


def select_words_from_list(words, num=5):
    """Select a random set of words from the list."""
    return random.sample(words, num)

def prompt_user_for_word_selection(words):
    """Prompt the user to select a word from the provided list."""
    print("Here are your 5 words to choose from:")
    for i, word in enumerate(words, 1):
        print(f"{i}. {word}")
    
    while True:
        selection = input("Do you want to select a word from the list? (y/n): ").strip().lower()
        if selection == 'y':
            selected_word = input("Please enter the word you have selected: ").strip().lower()  # Convert to lowercase
            # Compare the selected word in lowercase for case-insensitivity
            if selected_word in [word.lower() for word in words]:  # Convert words to lowercase for comparison
                # Get the exact word from the list (case-sensitive)
                for word in words:
                    if word.lower() == selected_word:
                        return word
            else:
                print("Invalid word selected. Please select a word from the list.")
        elif selection == 'n':
            print("You chose to skip. A new set of words will be provided.")
            return None
        else:
            print("Invalid input. Please enter 'y' to select or 'n' to skip.")

def split_words_into_chunks(words, chunk_size=100):
    """Split the words into chunks of `chunk_size` words each."""
    random.shuffle(words)  # Shuffle the words to ensure random chunks
    chunks = [words[i:i + chunk_size] for i in range(0, len(words), chunk_size)]
    return chunks  # Return all chunks

import hashlib
import random

def generate_keys(num_keys=3):
    """Generate `num_keys` random keys."""
    keys = []
    for _ in range(num_keys):
        key = hashlib.sha256(str(random.randint(0, 10000)).encode()).hexdigest()[:16]  # Generate 16-character keys
        keys.append(key)
    return keys

def encrypt_chunk(chunk, key):
    """Encrypt a chunk using a simple XOR encryption (for illustration)."""
    encrypted = ''.join(chr(ord(c) ^ ord(key[i % len(key)])) for i, c in enumerate(chunk))
    return encrypted

def mine_logic(selected_chunks, encrypted_chunks, desired_word, chunk_key_map):
    """Process the selected chunks and attempt to find the desired word."""
    print("\n========== Mine Process Begins ==========")

    # Track key usage
    key_usage_count = {"key_1": 0, "key_2": 0, "key_3": 0}
    used_keys = []  # List to track the keys that have been used

    # For feedback: Store where the desired word was found
    correct_chunk_with_word = None

    # Iterate through the available keys (user tries key_1, key_2, key_3)
    for key in ["key_1", "key_2", "key_3"]:
        print(f"\nAttempting to decrypt chunks with {key}...")

        # Track if any chunk was decrypted with the current key
        chunk_decrypted = False

        # Iterate through the selected chunks
        for chunk_index in selected_chunks:
            encrypted_chunk = encrypted_chunks[chunk_index - 1]  # Get the encrypted chunk
            correct_key = chunk_key_map.get(chunk_index, None)  # Find the correct key for this chunk

            if correct_key == key:  # This chunk is encrypted with the current key
                print(f"\nAttempting to decrypt Chunk {chunk_index}...")

                # Decrypt the chunk using the provided key
                decrypted_chunk = decrypt_chunk(encrypted_chunk, key)

                if decrypted_chunk:  # If decryption is successful
                    print(f"Chunk {chunk_index} decrypted successfully!")

                    # Check if the desired word is in the decrypted content
                    if desired_word.lower() in decrypted_chunk.lower():
                        print(f"\n🎉 Congratulations! The desired word '{desired_word}' was found in Chunk {chunk_index}.")
                        correct_chunk_with_word = chunk_index
                        print("💰 You win the Sane Coin! 💰")
                        return

                    else:
                        print(f"The desired word '{desired_word}' was not found in Chunk {chunk_index}.")
                    chunk_decrypted = True  # Mark that we decrypted a chunk
                    break  # Stop after successfully decrypting one chunk for this key

        # If no chunk was decrypted with the current key, proceed to the next key
        if not chunk_decrypted:
            print(f"\nNo chunk was decrypted with {key}. Proceeding to the next key...")

    # If no chunk was decrypted with any key, end the game
    if not correct_chunk_with_word:
        print("\nUnfortunately, none of the keys could decrypt the selected chunks to find the desired word.")
        print(f"Better luck next time! The desired word '{desired_word}' was found in Chunk {correct_chunk_with_word}.")

def start_game(words):
    terminal_display()
    """Start the game logic where the user selects a word and continues."""
    while True:
        selected_words = select_words_from_list(words)
        desired_word = prompt_user_for_word_selection(selected_words)
        
        if desired_word:
            print(f"The desired word for this round is: {desired_word}")
            
            # Ask user if they want to proceed with key generation
            proceed = input("\nDo you want to proceed with the key generation process? (y/n): ").strip().lower()
            if proceed == 'y':
                break
            elif proceed == 'n':
                print("Key generation process skipped. Exiting the game.")
                return
            else:
                print("Invalid response. Exiting the game.")
                return
        else:
            print("Let's try again with a new set of words.\n")
    
    # Now, process the words into chunks
    chunks = split_words_into_chunks(words)
    
    # Generate 3 keys for encryption
    keys = generate_keys()
    print(f"\n*******************************************************\n\nYour 3 public keys are: \n{keys}")
    
    # Private key for the program (not shared with user)
    program_key = "defaultprivatekey"  # This is the private key for encryption that won't be shared
    
    # Encrypt the chunks: First 3 chunks with public keys, remaining with private key
    encrypted_chunks = []
    encrypted_chunk_info = []

    # Encrypt first 3 chunks with public keys
    for i in range(min(3, len(chunks))):  # Ensure we don't go out of bounds
        encrypted_chunks.append(encrypt_chunk(' '.join(chunks[i]), keys[i]))
        encrypted_chunk_info.append("public")  # Mark the encryption method as "public"
    
    # Encrypt the remaining chunks with the private program key
    for i in range(3, len(chunks)):
        encrypted_chunks.append(encrypt_chunk(' '.join(chunks[i]), program_key))
        encrypted_chunk_info.append("private")  # Mark the encryption method as "private"
    
    # Shuffle the encrypted chunks and their associated information
    encrypted_chunks_with_info = list(zip(encrypted_chunks, encrypted_chunk_info))
    random.shuffle(encrypted_chunks_with_info)
    
    # Display the list of chunks without showing the actual encrypted content
    print("\n===================The Process of chunk encryption has started!=================")
    for i, (_, encryption_method) in enumerate(encrypted_chunks_with_info):
        print(f"Encrypted chunk {i + 1}: is encrypted with the secret key")

    # Now, the user selects 3 chunks to proceed with the game
    print("\nSelect 3 chunks to proceed with:")
    selected_chunks = []
    while len(selected_chunks) < 3:
        try:
            selection = int(input(f"Enter the number of chunk to select (1-{len(encrypted_chunks)}): "))
            if selection < 1 or selection > len(encrypted_chunks):
                print(f"Please enter a number between 1 and {len(encrypted_chunks)}.")
            elif selection not in selected_chunks:
                selected_chunks.append(selection)
            else:
                print("You have already selected this chunk.")
        except ValueError:
            print("Invalid input. Please enter a number.")
    
    # Once the user selects 3 chunks, proceed with the next step
    print(f"\n*******************************************************\n\nYou have selected the following chunks: \n{selected_chunks}")
    print("You can proceed with the game now.")
    
    # Map which key encrypted which chunk
    chunk_key_map = {i + 1: encrypted_chunk_info[i] for i in range(len(encrypted_chunk_info))}
    
    # Start the decryption attempt logic
    mine_logic(selected_chunks, [chunk for chunk, _ in encrypted_chunks_with_info], desired_word, chunk_key_map)

# Example usage (assuming words.txt exists)
if __name__ == "__main__":
    words = load_words("words.txt")  # Make sure to provide the correct path to the words file
    start_game(words)