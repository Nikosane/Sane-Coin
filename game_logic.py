# import random
# import os

# def load_words(file_path="words.txt"):
#     """Load words from a file and return as a list."""
#     try:
#         with open(file_path, 'r') as f:
#             words = [line.strip() for line in f]
#         if len(words) < 600:
#             raise ValueError("The file must contain at least 600 unique words.")
#         return words
#     except FileNotFoundError:
#         print("Error: 'words.txt' file not found.")
#         exit()
#     except ValueError as e:
#         print(f"Error: {e}")
#         exit()

# def get_random_words(word_list, count=10):
#     """Get a random sample of words from the list."""
#     return random.sample(word_list, count)

# def chunkify_words(word_list, chunk_size=100):
#     """Divide the list into 6 chunks of specified size."""
#     random.shuffle(word_list)
#     return [word_list[i:i + chunk_size] for i in range(0, chunk_size * 6, chunk_size)]

# def generate_keys():
#     """Generate 6 random keys."""
#     return [f"key{i+1}" for i in range(6)]

# def encrypt_chunks(chunks, keys):
#     """Encrypt chunks by associating each with a key."""
#     encrypted_chunks = {}
#     for i, chunk in enumerate(chunks):
#         encrypted_chunks[keys[i]] = chunk
#     return encrypted_chunks

# def decrypt_chunk(key, encrypted_chunks):
#     """Decrypt a chunk using the key."""
#     return encrypted_chunks.get(key, None)

# def start_game():
#     print("Welcome to the Word Encryption Game!")

#     # Load words
#     words = load_words()

#     # Word selection phase
#     while True:
#         print("\nSelect a word from the list to play:")
#         random_words = get_random_words(words)
#         for i, word in enumerate(random_words, start=1):
#             print(f"{i}. {word}")
#         print("0. Pass (Get new set of words)")

#         try:
#             choice = int(input("Enter the number corresponding to your chosen word: "))
#             if choice == 0:
#                 continue  # Get new set of words
#             elif 1 <= choice <= 10:
#                 desired_word = random_words[choice - 1]
#                 print(f"You selected: {desired_word}\n")
#                 break
#             else:
#                 print("Invalid choice. Please select again.")
#         except ValueError:
#             print("Invalid input. Please enter a number.")

#     # Chunk creation phase
#     chunks = chunkify_words(words)
#     print("6 chunks of words have been created.")

#     # Key generation phase
#     keys = generate_keys()
#     encrypted_chunks = encrypt_chunks(chunks, keys)
#     print("6 keys have been generated and associated with chunks.")

#     # User selection phase
#     print("\nChunks are labeled as Chunk1 to Chunk6, and keys as Key1 to Key6.")
#     selected_chunks = []
#     for i in range(3):
#         while True:
#             try:
#                 chunk_choice = int(input(f"Select Chunk {i+1} (1-6): "))
#                 if 1 <= chunk_choice <= 6 and chunk_choice not in selected_chunks:
#                     selected_chunks.append(chunk_choice)
#                     break
#                 else:
#                     print("Invalid choice or chunk already selected. Try again.")
#             except ValueError:
#                 print("Invalid input. Please enter a number.")

#     selected_keys = []
#     for i in range(3):
#         while True:
#             try:
#                 key_choice = int(input(f"Select Key {i+1} (1-6): "))
#                 if 1 <= key_choice <= 6 and key_choice not in selected_keys:
#                     selected_keys.append(keys[key_choice - 1])
#                     break
#                 else:
#                     print("Invalid choice or key already selected. Try again.")
#             except ValueError:
#                 print("Invalid input. Please enter a number.")

#     # Decryption phase
#     print("\nDecrypting selected chunks...")
#     for key in selected_keys:
#         print(f"Using {key}...")
#         for chunk_num in selected_chunks:
#             decrypted_chunk = decrypt_chunk(key, encrypted_chunks)
#             if decrypted_chunk and desired_word in decrypted_chunk:
#                 print(f"Success! The desired word '{desired_word}' was found in Chunk{chunk_num}.")
#                 return
    
#     print("Game Over! The desired word could not be found with the selected keys.")

# if __name__ == "__main__":
#     start_game()

import random
import os

def load_words(file_path="words.txt"):
    """Load words from a file and return as a list."""
    try:
        with open(file_path, 'r') as f:
            words = [line.strip() for line in f]
        if len(words) < 600:
            raise ValueError("The file must contain at least 600 unique words.")
        return words
    except FileNotFoundError:
        print("\033[91mError: 'words.txt' file not found.\033[0m")
        exit()
    except ValueError as e:
        print(f"\033[91mError: {e}\033[0m")
        exit()

def get_random_words(word_list, count=10):
    """Get a random sample of words from the list."""
    return random.sample(word_list, count)

def chunkify_words(word_list, chunk_size=100):
    """Divide the list into 6 chunks of specified size."""
    random.shuffle(word_list)
    return [word_list[i:i + chunk_size] for i in range(0, chunk_size * 6, chunk_size)]

def generate_keys():
    """Generate 6 random keys."""
    return [f"Key{i+1}" for i in range(6)]

def encrypt_chunks(chunks, keys):
    """Encrypt chunks by associating each with a key."""
    encrypted_chunks = {}
    for i, chunk in enumerate(chunks):
        encrypted_chunks[keys[i]] = chunk
    return encrypted_chunks

def decrypt_chunk(key, encrypted_chunks):
    """Decrypt a chunk using the key."""
    return encrypted_chunks.get(key, None)

def start_game():
    print("\033[96m" + "=" * 40)
    print("     Welcome to Sane Coins Mine!")
    print("=" * 40 + "\033[0m")

    # Load words
    words = load_words()

    # Word selection phase
    while True:
        print("\n\033[93mSelect a word from the list to play:\033[0m")
        random_words = get_random_words(words)
        for i, word in enumerate(random_words, start=1):
            print(f"\033[94m{i}.\033[0m {word}")
        print("\033[94m0.\033[0m Pass (Get new set of words)")

        try:
            choice = int(input("\nEnter the number corresponding to your chosen word: \033[92m"))
            if choice == 0:
                continue  # Get new set of words
            elif 1 <= choice <= 10:
                desired_word = random_words[choice - 1]
                print(f"\n\033[92mYou selected: {desired_word}\033[0m\n")
                break
            else:
                print("\033[91mInvalid choice. Please select again.\033[0m")
        except ValueError:
            print("\033[91mInvalid input. Please enter a number.\033[0m")

    # Chunk creation phase
    chunks = chunkify_words(words)
    print("\033[93m6 chunks of words have been created.\033[0m")

    # Key generation phase
    keys = generate_keys()
    encrypted_chunks = encrypt_chunks(chunks, keys)
    print("\033[93m6 keys have been generated and associated with chunks.\033[0m")

    # User selection phase
    print("\n\033[93mChunks are labeled as Chunk1 to Chunk6, and keys as Key1 to Key6.\033[0m")
    selected_chunks = []
    for i in range(3):
        while True:
            try:
                chunk_choice = int(input(f"Select Chunk {i+1} (1-6): \033[92m"))
                if 1 <= chunk_choice <= 6 and chunk_choice not in selected_chunks:
                    selected_chunks.append(chunk_choice)
                    print(f"\033[92mChunk{chunk_choice} selected.\033[0m")
                    break
                else:
                    print("\033[91mInvalid choice or chunk already selected. Try again.\033[0m")
            except ValueError:
                print("\033[91mInvalid input. Please enter a number.\033[0m")

    selected_keys = []
    for i in range(3):
        while True:
            try:
                key_choice = int(input(f"Select Key {i+1} (1-6): \033[92m"))
                if 1 <= key_choice <= 6 and key_choice not in selected_keys:
                    selected_keys.append(keys[key_choice - 1])
                    print(f"\033[92m{keys[key_choice - 1]} selected.\033[0m")
                    break
                else:
                    print("\033[91mInvalid choice or key already selected. Try again.\033[0m")
            except ValueError:
                print("\033[91mInvalid input. Please enter a number.\033[0m")

    # Decryption phase
    print("\n\033[93mDecrypting selected chunks...\033[0m")
    for key in selected_keys:
        print(f"\033[96mUsing {key}...\033[0m")
        for chunk_num in selected_chunks:
            decrypted_chunk = decrypt_chunk(key, encrypted_chunks)
            if decrypted_chunk and desired_word in decrypted_chunk:
                print(f"\033[92mSuccess! The desired word '{desired_word}' was found in Chunk{chunk_num}.\033[0m")
                print("\033[96mCongratulations! You mined the Sane Coin!\033[0m")
                return
    
    print("\033[91mGame Over! The desired word could not be found with the selected keys.\033[0m")

if __name__ == "__main__":
    start_game()
