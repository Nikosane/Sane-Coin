from utils import encrypt_with_key

DEFAULT_KEY = "default_key"  # Predefined secret key (hidden from the player)

def encrypt_chunks(chunks, random_key):
    encrypted_chunks = []
    for i, chunk in enumerate(chunks):
        # Encrypt 3 chunks with the random key and 3 with the default key
        if i < 3:
            encrypted_chunks.append(encrypt_with_key(chunk, random_key))
        else:
            encrypted_chunks.append(encrypt_with_key(chunk, DEFAULT_KEY))
    return encrypted_chunks

def decrypt_chunks(encrypted_chunks, key):
    decrypted_chunks = [encrypt_with_key(chunk, key) for chunk in encrypted_chunks]
    return decrypted_chunks
