# text_file_processor.py
import random

def generate_chunks(file_path):
    # Load words from file
    with open(file_path, 'r') as f:
        words = [line.strip() for line in f.readlines()]
    
    # Ensure there are enough words (600)
    if len(words) < 600:
        raise ValueError("Not enough words in the file!")

    # Randomly sample 600 words and create 6 chunks of 100 words
    random.shuffle(words)
    chunks = [words[i:i + 100] for i in range(0, len(words), 100)]
    
    return chunks
