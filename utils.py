def encrypt_with_key(text, key):
    # Simple substitution encryption (you can replace this with a more complex method)
    encrypted_text = ''.join(chr(ord(char) + len(key)) for char in text)
    return encrypted_text
