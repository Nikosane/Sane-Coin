from game_logic import start_game 
from utils import load_words

def main():

    # Load words from word.txt
    words = load_words("words.txt")

    
    # Start the game logic
    start_game(words)

if __name__ == "__main__":
    main()

