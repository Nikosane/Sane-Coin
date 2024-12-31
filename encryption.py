from utils import encrypt_with_key

DEFAULT_KEY = "default_key"  # Predefined secret key (hidden from the player)

def encrypt_chunks(chunks, key):
    """Encrypts a list of chunks using the provided key."""
    encrypted_chunks = []
    for chunk in chunks:
        # Join the list of words into a single string if needed
        if isinstance(chunk, list):
            chunk = ' '.join(chunk)
        encrypted_chunks.append(encrypt_with_key(chunk, key))
    return encrypted_chunks


def decrypt_chunks(encrypted_chunks, key):
    decrypted_chunks = [encrypt_with_key(chunk, key) for chunk in encrypted_chunks]
    return decrypted_chunks
