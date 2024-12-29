# SaneCoin: A Decryption-Based Coin Collection Game

SaneCoin is a Python-based game where users can collect "SaneCoins" by decrypting encrypted chunks of text. The game involves selecting a predefined word from randomly encrypted chunks, which will grant a coin if found. The project showcases key generation, text encryption/decryption, and a word-selection-based game, which offers a fun challenge to the players.

## Project Overview

In this game:
- The user will be provided with 6 chunks of text, each containing 100 words.
- Three of these chunks are encrypted with a randomly generated key, while the other three are encrypted using a default encryption key that is only available to the program.
- The user needs to select one chunk to decrypt using the correct key and then find a desired word from the chunk.
- The user will select a random word from the list of available words and claim it as the desired word they want to search for.
- If the correct word is found in the selected chunk, the player earns one SaneCoin.

## Key Features
- **Text Chunk Creation**: 6 chunks of 100 words each, randomly generated from a predefined word list.
- **Random Word Selection**: A random word is selected from the chunks, and the user must claim it to proceed.
- **Encryption**: A basic encryption algorithm to encrypt three chunks using a random key and three chunks using a default key.
- **Key Generation**: Random keys consisting of 3 letters and 2 numbers.
- **Gameplay Logic**: User selects and decrypts chunks, then attempts to find the correct word to earn coins.

## File Structure

The project is organized into multiple Python files for better modularity and readability:

- `main.py`: Entry point of the game where everything ties together and the game starts.
- `game_logic.py`: Contains the main game logic, managing chunk selection, decryption attempts, and coin reward.
- `text_file_processor.py`: Processes the `words.txt` file to create the 6 chunks of words for the game.
- `key_generator.py`: Generates the random encryption keys (user-specific and default).
- `encryption.py`: Handles the encryption and decryption logic using the generated keys.
- `word_selector.py`: Handles the selection of a random word from the word list and allows the user to select their desired word.
- `utils.py`: Contains utility functions like word validation, encryption helpers, etc.
- `words.txt`: A text file containing 600 unique English words, used to generate the text chunks for the game.

## Requirements

- Python 3.x
- Random and os modules (standard Python libraries)
  
## Setup

1. Clone the repository:
    ```bash
    git clone https://github.com/yourusername/sanecoin.git
    cd sanecoin
    ```

2. Populate the `words.txt` file with 600 unique English words. Make sure they are legitimate words.

3. Run the game:
    ```bash
    python main.py
    ```

4. The game will start, and you will be prompted to select a chunk to decrypt. Find the correct word to earn a SaneCoin!

## How It Works

- **Step 1: Word Selection**: The user is asked to select a random word from the 600 available words. This word is the one they will search for in the encrypted chunks.
  
- **Step 2: Chunk Generation**: The 600 words from `words.txt` are randomly selected and divided into 6 chunks, each containing 100 words. Three chunks are encrypted with the random key, and the other three are encrypted using the default encryption key.

- **Step 3: Decryption**: The user selects one chunk to decrypt, but only 3 out of the 6 chunks can be decrypted using the random key.

- **Step 4: Finding the Desired Word**: After decrypting the selected chunk, the user must search for the word they selected earlier. If the word is found, they earn 1 SaneCoin.

- **Step 5: Game Over**: The game ends when the user finds the desired word and earns the coin.

## Example Flow

1. The user selects the desired word from a random list of 600 words.
2. The game presents 6 chunks, out of which 3 are encrypted with the program’s key, and 3 are encrypted with a default key.
3. The user selects one chunk to decrypt.
4. If the user successfully decrypts the chunk and finds the desired word, they earn 1 SaneCoin.

## Contributions

Feel free to fork the repository, open issues, and create pull requests. Contributions are always welcome!

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

---

**Note**: The default encryption method used in this project is a basic cipher for the sake of simplicity. You can explore more advanced encryption techniques for further enhancement.

