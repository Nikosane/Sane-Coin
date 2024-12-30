import random
import string

def generate_random_key():
    letters = random.choices(string.ascii_lowercase, k=3)
    digits = random.choices(string.digits, k=2)
    key = ''.join(letters + digits)
    return key
