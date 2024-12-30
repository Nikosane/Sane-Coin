import random

def select_word(words):
    # Randomly select a word and ensure it is a valid word (verb/noun)
    desired_word = random.choice([word for word in words if is_valid_word(word)])
    return desired_word

def is_valid_word(word):
    # Add basic check for valid verbs/nouns (for now, we can check length or use a dictionary)
    return len(word) > 3  # A placeholder check, refine as needed
