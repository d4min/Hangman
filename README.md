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

- Defined what happens if the guessed letter is in the word that is being guessed

```python
if guess in self.word:
            print(f"Good guess! {guess} is in the word.")
            for i in range(len(self.word)):
                if self.word[i] == guess:
                    self.word_guessed[i] = guess
            print(self.word_guessed)
            self.num_letters -= 1
```
1. Text is printed letting the user know that the letter they guessed is in the word.

1. The word_guessed list is updated to reveal the correct letter/s and then printed.

1. The number of unique letters left to be guessed is reduced by one.

- Defined what happens if the guessed letter is not in the word that is being guessed

```python
else:
        print(f"Sorry, {guess} is not in the word.")
        self.num_lives -= 1
        print(f"You have {self.num_lives} lives left.")
```
1. A line is printed letting the user know that their guess was wrong.

1. The number of lives the user has are reduced by one.

1. The number of remaining lives is printed to the user. 

##  Milestone 5

- Integrated the logic required to play the game into the code by defining the play_game() function outside of the Hangman class. 

```python
def play_game(word_list):

    num_lives = 5
    game = Hangman(word_list, num_lives)

    while True:
        if game.num_lives == 0:
            print("You lost!")
            break
        elif game.num_letters > 0:
            game.ask_for_input()
        else:
            print("Congratulations. You won the game!")
            break
```
The function takes in a list of words as an argument. Instantiates a Hangman object as 'game' and then uses a while loop to add the logic.

The loop works as follows:

1. Checks if the number of lives are zero. If so, a line is printed letting the user know they have lost the game and the loop is exited. 

1. Checks if the variable num_letters is greater than zero. If so, it means there are still letters to be guessed so the ask_for_input() function is called again allowing the user to input a guess.

1. If neither previous conditions are met this means the user has won the game because they have more than zero lives and there aren't any more unique letters to be guessed. The script prints out a congratulations message and then breaks out of the loop. 

