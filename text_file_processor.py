import random

def generate_chunks(file_name):
    with open(file_name, 'r') as file:
        words = [line.strip() for line in file.readlines()]
    # Ensure that there are exactly 600 words
    assert len(words) == 600, "File must contain exactly 600 words."
    
    # Shuffle and split into 6 chunks of 100 words each
    random.shuffle(words)
    chunks = [words[i:i + 100] for i in range(0, 600, 100)]
    
    return chunks
