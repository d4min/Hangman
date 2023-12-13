import random

class Hangman:
    
    def __init__(self, word_list, num_lives = 5):
        self.word = random.choice(word_list)
        self.word_guessed = ["_" for i in self.word]
        self.num_letters = len(set(self.word))
        self.num_lives = num_lives
        self.word_list = word_list
        self.list_of_guesses = []

    def ask_for_input(self):
        while True:
            guess = input("Please enter your first guess as a single character")

            if len(guess) != 1 or guess.isalpha() == False:
                print("Invalid input. Please, enter a single alphabetical character.")
            elif guess in self.list_of_guesses:
                print("You already tried that letter!")
            else:
                self.list_of_guesses.append(guess)
                self.check_guess(guess)
                break

    def check_guess(self, guess):
        guess = guess.lower()
        if guess in self.word:
            print(f"Good guess! {guess} is in the word.")

            for i in range(len(self.word)):
                if self.word[i] == guess:
                    self.word_guessed[i] = guess

            self.num_letters -= 1
        else:
            print(f"Sorry, {guess} is not in the word.")
            self.num_lives -= 1
            print(f"You have {self.num_lives} lives left.")