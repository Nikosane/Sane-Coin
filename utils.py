def encrypt_with_key(text, key):
    """Encrypts the given text using the provided key."""
    encrypted_text = ''.join(
        chr(ord(char) + len(key)) if char.isalnum() else char for char in text
    )
    return encrypted_text

def decrypt_with_key(text, key):
    """Decrypts the given text using the provided key."""
    decrypted_text = ''.join(
        chr(ord(char) - len(key)) if char.isalnum() else char for char in text
    )
    return decrypted_text

def load_words(filename):
    """Load words from a file and return a list of words."""
    with open(filename, 'r') as file:
        words = file.read().splitlines()  # Assuming words are one per line
    return words