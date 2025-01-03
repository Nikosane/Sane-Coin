# Sane Coins Mine

## Introduction
Sane Coins Mine is an engaging command-line game that combines elements of randomness, encryption, and strategy. Players navigate through encrypted chunks of data using keys to locate their chosen word, referred to as "mining the Sane Coin." This game challenges players' luck and strategy in a fun and interactive way.

---

## Features

- **Word Selection**:
  - A `words.txt` file contains at least 600 unique words.
  - At the start of the game, players are presented with 10 random words.
  - Players can either select a word or pass to get a new set of 10 words.

- **Chunk Creation**:
  - The words from the file are divided into 6 randomized chunks, each containing 100 words.
  - Chunks are shuffled for fairness.

- **Key Generation**:
  - Six unique encryption keys (`Key1` to `Key6`) are generated and associated with chunks.

- **Player Choices**:
  - Players select 3 chunks and 3 keys.
  - Both strategy and luck play a role in these selections.

- **Decryption Challenge**:
  - Selected keys are used to decrypt chunks to find the chosen word.
  - If the desired word is found, the player wins and "mines the Sane Coin."
  - If all keys are exhausted without success, the game ends.

---

## Installation

1. **Clone the Repository**:
   ```bash
   git clone https://github.com/Nikosane/sane-coins-mine.git
   cd sane-coins-mine
   ```

2. **Install Dependencies**:
   - Ensure Python 3.7 or higher is installed.
   - Install the `pyfiglet` library:
     ```bash
     pip install pyfiglet
     ```

3. **Prepare the `words.txt` File**:
   - Add a file named `words.txt` in the project directory containing at least 600 unique words, one per line.

---

## How to Play

1. **Start the Game**:
   ```bash
   python sane_coins_mine.py
   ```

2. **Gameplay Flow**:
   - A welcome screen introduces the game.
   - Players select a word from a random set of 10 words or pass to get a new set.
   - The game creates 6 randomized chunks of words and generates 6 encryption keys.
   - Players choose 3 chunks and 3 keys.
   - Selected keys decrypt the chosen chunks, searching for the selected word.
   - Feedback is provided, declaring success or failure.

3. **Win Condition**:
   - If the selected word is found during decryption, the player wins and "mines the Sane Coin."

---

## Example Gameplay Session

- **Welcome Screen**:
  ```
  Sane Coins Mine
  Welcome to Sane Coins Mine!
  ```

- **Word Selection**:
  ```
  Select a word from the list to play:
  1. apple
  2. orange
  3. banana
  ...
  0. Pass (Get new set of words)
  ```

- **Chunk and Key Selection**:
  ```
  Select Chunk 1 (1-6): 2
  Chunk2 selected.
  Select Key 1 (1-6): 3
  Key3 selected.
  ```

- **Decryption Phase**:
  ```
  Decrypting selected chunks...
  Using Key3...
  Success! The desired word 'apple' was found in Chunk2.
  Congratulations! You mined the Sane Coin!
  ```

---

## Requirements

- Python 3.7+
- `pyfiglet` library
- A `words.txt` file with at least 600 unique words

---

## Contributing

Contributions are welcome! Please fork the repository and create a pull request for improvements or bug fixes.

---

## License

This project is licensed under the MIT License. See the LICENSE file for details.

