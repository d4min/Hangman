import random

word_list = ['pineapple', 'peaches', 'mango', 'watermelon', 'banana']
print(word_list)

word = random.choice(word_list)
print(word)

guess = input("Please enter your first guess as a single character")

if len(guess) == 1 and guess.isalpha():
    print("Good guess!")
else:
    print("Oops! That is not a valid input.")

