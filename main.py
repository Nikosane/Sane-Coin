from game_logic import play_game 
from utils import load_words

def main():

    # Load words from word.txt
    words = load_words("words.txt")

    
    # Start the game logic
    play_game()

if __name__ == "__main__":
    main()

