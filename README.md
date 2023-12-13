# Hangman
Hangman is a classic game in which a player thinks of a word and the other player tries to guess that word within a certain amount of attempts.

This is an implementation of the Hangman game, where the computer thinks of a word and the user tries to guess it. 

## Milestone 1

- Creates a remote github repository for this project to version control the software as well as practice the use of github.

- Connects the remote repository to a local clone using the command line.

```bash
git clone https://github.com/d4min/hangman.git
```

## Milestone 2

- Defines the variable 'word_list' which is a list of words that the python script will use as the word to be guessed during the Hangman game. 

- Imports the random library in python to allow the script to assign the variable 'word' a random word from the pre-defined list of words.
```python
import random

word = random.choice(word_list)
```

- Takes a character as user input as their first guess. Validates the input using an if statement to ensure it was a single alphabetical character. 

```python
guess = input("Please enter your first guess as a single character")

if len(guess) == 1 and guess.isalpha():
    print("Good guess!")
else:
    print("Oops! That is not a valid input.")
```

## Milestone 3

- Builds on the previous validation code and implements a while loop to iteratively check user inputs until a valid input is received. 

- Checks whether the character the user guesses is in the randomly chosen word to be guessed and prints the relevent statement. 

```python
if guess in word:
        print(f"Good guess! {guess} is in the word.")
    else:
        print(f"Sorry, {guess} is not in the word. Try again.")
```
- Defined functions for both of the checks listed above.

## Milestone 4

- Created the Hangman class in accordance with OOP principles and defined the constructor of the class with the relevant attributes.

```python
def __init__(self, word_list, num_lives = 5):
        self.word = random.choice(word_list)
        self.word_guessed = ["_" for i in self.word]
        self.num_letters = len(set(self.word))
        self.num_lives = num_lives
        self.word_list = word_list
        self.list_of_guesses = []
```
Constructor takes in a list of words and the number of lives as arguments.
### Attributes:
1. **word**: string - A randomly chosen word from the list of words.

1. **word_guessed**: list - A list of the letters of the word, with _ for each letter not yet guessed. For example, if the word is 'apple', the word_guessed list would be ['\_', '\_', '\_', '\_', '\_']. If the player guesses 'a', the list would be ['a', '\_', '\_', '\_', '\_'].

1. **num_letters**: int - The number of unique letters in the word that have not been guessed yet.

1. **num_lives**: int - The number of lives the player has at the start of the game. 

1. **word_list**: list - A list of words.

1. **list_of_guesses**: list - A list of the guesses that have already been tried.

- Incorporated the functions created in previous milestone as methods in the Hangman class. 

- Defined what happens if the guessed letter is in the word that is being guessed