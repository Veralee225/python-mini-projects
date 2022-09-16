import random
import hangman_art import stages, logo
from hangman_words import word_list
from replit import clear


word_list = ["happy", "frustration", "giving"]

# randomly choose a word from the word_list and assign
# it to a varibale called chosen_word
chosen_word = random.choice(word_list)

display = []
word_length = len(chosen_word)

for _ in range(word_length):
    display += "_"
print(display)

end_of_game = False

while not end_of_game:
guess = input("Guess a letter: ").lower()

#using a Forloop to check if the user guessed the right letter

for position in range(word_length):
    letter = chosen_word[position]
    print(f"Current position: {position}\n
    Current letter: {letter}\n 
    Guessed letter: {guess}")
    if letter == guess:
        display[position] = letter
        
print(f"you entered {chosen_word}." )
print(display)
