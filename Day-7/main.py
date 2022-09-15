import random
import hangman_art import stages, logo
from hangman_words import word_list
from replit import clear

word_list = ["happy", "frustration", "giving"]

# randomly choose a word from the word_list and assign
# it to a varibale called chosen_word
chosen_word = random.choice(word_list)

#used the input() function to ask the user to guess a letter, then I assigned
# their answer to the variable guess, I made it lowercase
guess = input("Guess a letter: ").lower()

#using a Forloop to check if the user guessed the right letter

for letter in chosen_word:
    if letter == guess:
        print("Right")
    else:
        print("Wrong")



print(f"you entered {value}" )
