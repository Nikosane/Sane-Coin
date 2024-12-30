from encryption import decrypt_chunks
from word_selector import select_word

def start_game(encrypted_chunks, desired_word):
    print("Welcome to SaneCoin! Try to find the desired word!")
    
    # Show the encrypted chunks
    for idx, chunk in enumerate(encrypted_chunks):
        print(f"Chunk {idx + 1}: {chunk[:20]}...")  # Display part of the chunk
    
    # Ask the player to select 3 chunks
    selected_chunks = []
    while len(selected_chunks) < 3:
        selection = int(input("Select a chunk to decrypt (1-6): ")) - 1
        if selection not in selected_chunks:
            selected_chunks.append(selection)
    
    # Decrypt the selected chunks
    decrypted_chunks = decrypt_chunks([encrypted_chunks[i] for i in selected_chunks], input("Enter the key: "))
    
    # Display the decrypted chunks and allow the player to find the desired word
    print("Decrypted Chunks:")
    for chunk in decrypted_chunks:
        print(chunk)
    
    guess = input(f"Guess the desired word from these chunks: ")
    
    if guess == desired_word:
        print("Congratulations! You found the desired word!")
        return True
    else:
        print("Sorry, that's not the right word. Try again!")
        return False
