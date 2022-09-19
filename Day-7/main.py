#!/usr/bin/python3
import random
from hangman_art import stages, logo
from hangman_words import word_list
#replit causes an error because it isn't a module
# but it works on the Replit platform
from replit import clear

print(logo)

game_is_finished = False 
lives = len(stages) - 1

# previous words used to test
#word_list = ["happy", "frustration", "giving"]

# randomly choose a word from the word_list and assign
# it to a varibale called chosen_word
chosen_word = random.choice(word_list)

word_length = len(chosen_word)

display = []

for _ in range(word_length):
    display += "_"

while not game_is_finished:
    guess = input("Guess a letter:").lower()

# using the clear function from replit to clear the output between guesses
    clear()

    if guess in display:
        print(f"You've already guessed {guess}")

#using a Forloop to check if the user guessed the right letter

for position in range(word_length):
    letter = chosen_word[position]
    if letter == guess:
        display[position] = letter
print(f"{' '.join(display)}")

if guess not in chosen_word:
    print(f"You guessed {guess}, that's not in the word. You lose a life")
    lives -= 1
    if lives == 0:
        game_is_finished = True
        print("You lose.")
    if not "_" in display:
        game_is_finished = True
        print("You win.")
